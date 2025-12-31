# 도메인 자료 저장소

각 하위 디렉토리에 해당 분야의 참고 자료를 마크다운 형식으로 저장합니다.

---

## 디렉토리 구조

```
references/
├── journalism/     ← 언론, 미디어 관련
├── medicine/       ← 의료, 병원 관련
├── law/            ← 법조, 사법 관련
└── (필요에 따라 추가)
```

---

## 자료 유형 권장

| 유형 | 설명 | 예시 파일명 |
|------|------|------------|
| **입문서/개론** | 해당 분야의 기본 구조와 개념 | `basics.md`, `overview.md` |
| **내부자 수기** | 현장 경험, 에세이, 인터뷰 | `memoir.md`, `interviews.md` |
| **사건/사례** | 실제 있었던 일들 | `famous_cases.md`, `incidents.md` |
| **용어집** | 전문 용어와 은어 | `terminology.md`, `jargon.md` |
| **윤리/관행** | 업계 규범과 암묵적 규칙 | `ethics.md`, `practices.md` |

---

## 파일 형식

- **확장자**: 모든 파일은 `.md` (마크다운) 형식
- **인코딩**: UTF-8
- **파일명**: 공백 대신 언더스코어(`_`) 사용
  - 좋은 예: `reporter_daily_life.md`
  - 나쁜 예: `reporter daily life.md`

---

## 권장 자료 구조

각 마크다운 파일은 다음 구조를 권장합니다:

```markdown
# [자료 제목]

## 출처
- [원본 출처 정보]

## 핵심 내용

### [섹션 1]
[내용]

### [섹션 2]
[내용]

## 소설 창작 활용 포인트
- [이 자료에서 소설에 활용할 수 있는 요소들]
```

---

## 사용 방법

도메인 자료를 준비한 후, 다음과 같이 실행합니다:

```bash
# 예: 언론 분야 소설 창작
python run.py --input "소재.txt" --domain "references/journalism/" --auto

# 예: 의료 분야 소설 창작
python run.py --input "소재.txt" --domain "references/medicine/" --interactive
```

---

## 팁

1. **양보다 질**: 방대한 자료보다 핵심적이고 구체적인 자료가 효과적
2. **내부자 시점**: 외부 관찰보다 현장 경험자의 목소리가 중요
3. **감각적 디테일**: 이론보다 현장의 냄새, 소리, 분위기
4. **갈등 포인트**: 해당 분야에서 흔히 발생하는 딜레마와 갈등
5. **클리셰 구분**: 미디어에서 본 이미지 vs. 실제 현장의 차이

---

## 예시: journalism/ 디렉토리 구성

```
journalism/
├── newsroom_basics.md          # 편집국 기본 구조
├── reporter_daily_routine.md   # 기자의 하루
├── terminology.md              # 언론 용어집
├── ethical_dilemmas.md         # 취재 윤리 딜레마 사례
├── famous_scoops.md            # 유명 특종 사례
└── insider_interviews.md       # 현직 기자 인터뷰
```
