#!/usr/bin/env python3
"""
CR-Story 문장 리듬 분석기
- 단문 연속 패턴 감지
- 장면 전환 후 단문 시작 감지
- 문장 길이 분포 시각화

사용법:
    python analyze_rhythm.py <파일경로>
    python analyze_rhythm.py /path/to/08-final.md
"""

import re
import sys
from collections import Counter
from pathlib import Path


def extract_sentences(text: str) -> list[str]:
    """마크다운 텍스트에서 문장 추출 (인용문, 코드블록 제외)"""
    # 인용문(>) 제거
    text = re.sub(r'^>.*$', '', text, flags=re.MULTILINE)
    # 코드블록 제거
    text = re.sub(r'```[\s\S]*?```', '', text)
    # 헤더 제거
    text = re.sub(r'^#+\s.*$', '', text, flags=re.MULTILINE)
    # 볼드/이탤릭 마크다운 제거 (내용 유지)
    text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)
    text = re.sub(r'\*([^*]+)\*', r'\1', text)
    
    # 문장 분리 (한국어 기준: 다, 요, 까 등으로 끝나는 경우)
    sentences = re.split(r'(?<=[.?!다요까])\s+', text)
    
    # 빈 문장 및 구분선 제거
    sentences = [s.strip() for s in sentences if s.strip() and s.strip() != '---']
    
    return sentences


def classify_sentence_length(sentence: str) -> str:
    """문장 길이 분류"""
    length = len(sentence)
    if length <= 15:
        return 'short'  # 단문
    elif length <= 40:
        return 'medium'  # 중문
    else:
        return 'long'  # 장문


def find_consecutive_short_sentences(sentences: list[str], threshold: int = 3) -> list[dict]:
    """연속 단문 패턴 찾기"""
    issues = []
    consecutive_count = 0
    start_idx = 0
    
    for i, sentence in enumerate(sentences):
        if classify_sentence_length(sentence) == 'short':
            if consecutive_count == 0:
                start_idx = i
            consecutive_count += 1
        else:
            if consecutive_count >= threshold:
                issues.append({
                    'type': 'consecutive_short',
                    'start_line': start_idx + 1,
                    'count': consecutive_count,
                    'sentences': sentences[start_idx:start_idx + consecutive_count],
                    'severity': 'HIGH' if consecutive_count >= 4 else 'MEDIUM'
                })
            consecutive_count = 0
    
    # 마지막 체크
    if consecutive_count >= threshold:
        issues.append({
            'type': 'consecutive_short',
            'start_line': start_idx + 1,
            'count': consecutive_count,
            'sentences': sentences[start_idx:start_idx + consecutive_count],
            'severity': 'HIGH' if consecutive_count >= 4 else 'MEDIUM'
        })
    
    return issues


def find_scene_transition_issues(text: str) -> list[dict]:
    """장면 전환 직후 단문 시작 감지"""
    issues = []
    
    # --- 구분선 찾기
    pattern = r'---\s*\n+([^\n]+)'
    matches = re.finditer(pattern, text)
    
    for match in matches:
        first_line = match.group(1).strip()
        if len(first_line) <= 20 and first_line:  # 매우 짧은 시작
            issues.append({
                'type': 'scene_transition_short',
                'position': match.start(),
                'first_line': first_line,
                'severity': 'HIGH'
            })
    
    return issues


def calculate_statistics(sentences: list[str]) -> dict:
    """문장 통계 계산"""
    lengths = [len(s) for s in sentences]
    classifications = [classify_sentence_length(s) for s in sentences]
    
    return {
        'total_sentences': len(sentences),
        'avg_length': sum(lengths) / len(lengths) if lengths else 0,
        'min_length': min(lengths) if lengths else 0,
        'max_length': max(lengths) if lengths else 0,
        'distribution': Counter(classifications),
        'short_ratio': classifications.count('short') / len(classifications) * 100 if classifications else 0
    }


def generate_report(file_path: str) -> str:
    """분석 리포트 생성"""
    path = Path(file_path)
    if not path.exists():
        return f"Error: 파일을 찾을 수 없습니다: {file_path}"
    
    text = path.read_text(encoding='utf-8')
    sentences = extract_sentences(text)
    
    # 분석 실행
    consecutive_issues = find_consecutive_short_sentences(sentences)
    transition_issues = find_scene_transition_issues(text)
    stats = calculate_statistics(sentences)
    
    # 리포트 생성
    report = []
    report.append("=" * 60)
    report.append("CR-Story 문장 리듬 분석 리포트")
    report.append("=" * 60)
    report.append(f"\n📄 파일: {path.name}")
    report.append(f"📊 총 문장 수: {stats['total_sentences']}")
    report.append(f"📏 평균 문장 길이: {stats['avg_length']:.1f}자")
    report.append(f"📉 최소/최대: {stats['min_length']}자 / {stats['max_length']}자")
    
    report.append(f"\n📊 문장 길이 분포:")
    report.append(f"   - 단문 (≤15자): {stats['distribution'].get('short', 0)}개 ({stats['short_ratio']:.1f}%)")
    report.append(f"   - 중문 (16-40자): {stats['distribution'].get('medium', 0)}개")
    report.append(f"   - 장문 (>40자): {stats['distribution'].get('long', 0)}개")
    
    # 문제점 리포트
    report.append("\n" + "-" * 60)
    report.append("🚨 발견된 문제")
    report.append("-" * 60)
    
    total_issues = len(consecutive_issues) + len(transition_issues)
    
    if total_issues == 0:
        report.append("✅ 문제가 발견되지 않았습니다.")
    else:
        report.append(f"총 {total_issues}개 문제 발견\n")
        
        # 연속 단문 문제
        if consecutive_issues:
            report.append("【단문 연속 문제】")
            for i, issue in enumerate(consecutive_issues, 1):
                report.append(f"\n  [{issue['severity']}] #{i}: {issue['count']}개 연속 단문")
                for j, sent in enumerate(issue['sentences'][:3]):  # 최대 3개만 표시
                    report.append(f"      → \"{sent[:40]}{'...' if len(sent) > 40 else ''}\"")
                if len(issue['sentences']) > 3:
                    report.append(f"      ... 외 {len(issue['sentences']) - 3}개")
        
        # 장면 전환 문제
        if transition_issues:
            report.append("\n【장면 전환 직후 단문 시작】")
            for i, issue in enumerate(transition_issues, 1):
                report.append(f"\n  [{issue['severity']}] #{i}: \"{issue['first_line']}\"")
    
    # 권장사항
    report.append("\n" + "-" * 60)
    report.append("💡 권장사항")
    report.append("-" * 60)
    
    if stats['short_ratio'] > 30:
        report.append("⚠️  단문 비율이 30%를 초과합니다. 중-장문으로 리듬 개선 필요.")
    
    if stats['avg_length'] < 25:
        report.append("⚠️  평균 문장 길이가 짧습니다. 호흡을 늘려주세요.")
    
    if len(consecutive_issues) > 0:
        report.append(f"⚠️  {len(consecutive_issues)}개의 단문 연속 구간을 수정해주세요.")
    
    if len(transition_issues) > 0:
        report.append(f"⚠️  {len(transition_issues)}개의 장면 전환 시작부를 보완해주세요.")
    
    if total_issues == 0 and stats['short_ratio'] <= 30:
        report.append("✅ 문장 리듬이 양호합니다.")
    
    report.append("\n" + "=" * 60)
    
    return "\n".join(report)


def main():
    if len(sys.argv) < 2:
        print("사용법: python analyze_rhythm.py <파일경로>")
        print("예시: python analyze_rhythm.py ./outputs/story-reply/08-final.md")
        sys.exit(1)
    
    file_path = sys.argv[1]
    report = generate_report(file_path)
    print(report)


if __name__ == "__main__":
    main()
