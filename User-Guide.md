# 심플한 이용자 가이드

멀티에이전트 소설 창작 시스템 사용법을 가장 쉽게 설명합니다.

---

## 시작하기 전에: 파일 위치 이해하기

프로젝트 폴더 구조는 이렇습니다:

```
cr-lab-storytelling/
├── workflow/
│   ├── prompts/                    ← 실행 프롬프트 (단계별 지침)
│   │   ├── 00-start-guide.md       ← 시작 가이드
│   │   ├── 01-researcher.md        ← Step 0: 도메인 리서처
│   │   ├── 02-philosopher.md       ← Step 1: 철학자
│   │   ├── 03-novelist-synopsis.md ← Step 2: 시놉시스
│   │   ├── 04-novelist-critic.md   ← Step 3: 구조적 비평
│   │   ├── 05-novelist-draft.md    ← Step 4: 초고 작성
│   │   ├── 06-editor.md            ← Step 5: 편집
│   │   ├── 07-novelist-revision.md ← Step 6: 수정고
│   │   ├── 08-literary-critic.md   ← Step 7: 문학적 비평
│   │   ├── 09-novelist-final.md    ← Step 8: 최종본
│   │   ├── 10-touchup.md           ← Step 9: 터치업 (선택)
│   │   └── R1-revision-mode.md     ← 재작성 모드
│   │
│   ├── inputs/                     ← 소재 입력
│   │   └── input.md                ← 여기에 소재 작성
│   │
│   ├── outputs/                    ← 결과물 저장
│   │   └── story-[이름]/           ← 작품별 폴더 자동 생성
│   │       ├── 08-final.md         ← 최종 완성본
│   │       ├── 09-polished.md      ← 터치업 완성본 (선택)
│   │       └── ...
│   │
│   ├── references/                 ← 참조 자료
│   │   ├── TOUCHUP_GUIDE.md        ← 문장 리듬 가이드
│   │   ├── NARRATIVE_GUIDE.md      ← 서사 기법 가이드
│   │   ├── [References] Korean Short Stories/  ← 레퍼런스 작품 17편
│   │   └── cr-knowledge/           ← 언론 도메인 지식베이스
│   │       ├── 01-problem-awareness.md   ← 언론 문제 인식
│   │       ├── 02-journalism-reality.md  ← 언론 현장의 실제
│   │       ├── 03-problematic-patterns.md ← 119개 문제 패턴
│   │       ├── 04-citizen-solution.md    ← 윤리규범 + 시민 해결책
│   │       └── 05-cr-depiction-guide.md  ← CR 묘사 가이드
│   │
│   └── project_context.md          ← 프로젝트 철학
│
└── User-Guide.md                   ← 이 파일
```

---

## 케이스 1: 처음부터 새로 작성하기

### 1단계: 소재 파일 작성하기

`workflow/inputs/input.md` 파일을 열고 소재를 적으세요.

**예시 1 (간단하게)**:
```markdown
# 소재 입력

## 기본 아이디어
내부고발을 결심한 기자의 이야기
```

**예시 2 (자세하게)**:
```markdown
# 소재 입력

## 기본 아이디어
대형 언론사에서 일하는 중견 기자가 회사의 부정을 발견했다.
양심과 생계 사이에서 고민하다가 결국 내부고발을 결심한다.
하지만 그 과정에서 예상치 못한 배신과 진실을 마주하게 된다.

## 도메인
언론/탐사보도

## 원하는 분위기
긴장감 있는, 묵직한

## 주인공 힌트
40대 중견 기자, 양심과 생존 사이에서 갈등

## 피하고 싶은 것
해피엔딩, 권선징악
```

### 2단계: Claude Code에서 실행하기

Claude Code를 열고 다음과 같이 요청하세요:

#### 방법 A: 전체 프로세스 한 번에 실행

```
workflow/prompts/00-start-guide.md를 읽고,
workflow/inputs/input.md의 소재로 전체 프로세스를 실행해줘.
도메인은 "언론/탐사보도"야.
작품 이름은 "story-01"로 해줘.
```

#### 방법 B: 단계별 실행

각 단계를 하나씩 확인하며 진행하고 싶다면:

```
Step 1: workflow/prompts/02-philosopher.md를 읽고 화두를 도출해줘.
        입력은 workflow/inputs/input.md야.
        결과는 workflow/outputs/story-01/01-theme.md에 저장해줘.

Step 2: workflow/prompts/03-novelist-synopsis.md를 읽고 시놉시스를 작성해줘.
        ...
```

**사용 가능한 도메인 키워드**:
- `언론/탐사보도`, `언론/방송뉴스` ← 언론 문제 지식베이스 자동 로드
- `의료/응급의학`, `의료/외과`
- `법조/형사변호`, `법조/검찰`
- `교육/고등학교`
- `기업/스타트업`

등록 안된 분야도 사용 가능 (예: `광고/카피라이터`)

### 3단계: 완성본 확인하기

**결과 위치**: 
- `workflow/outputs/story-[이름]/08-final.md` (기본 최종본)
- `workflow/outputs/story-[이름]/09-polished.md` (터치업 적용 시)

중간 과정 파일들:
- `00-domain_knowledge.md` - 도메인 지식 (선택)
- `01-theme.md` - 화두
- `02-synopsis.md` - 시놉시스
- `03-feedback.md` - 구조적 피드백
- `04-draft_v1.md` - 초고
- `05-edit_notes.md` - 편집 노트
- `06-draft_v2.md` - 수정본
- `07-critique.md` - 문학적 비평
- `08-final.md` - **최종본**
- `09-touchup-report.md` - 터치업 리포트 (선택)
- `09-polished.md` - **터치업 완성본** (선택)

---

## 케이스 2: 완성본 수정하기

### 1단계: Claude Code에서 재작성 요청하기

```
workflow/prompts/R1-revision-mode.md를 읽고,
workflow/outputs/story-01/08-final.md에 대해 다음 피드백을 반영해서 수정해줘:

"주인공의 내적 갈등이 약해요. 결정 장면에서 더 고민하는 모습이 필요합니다.
결말이 너무 급해요."
```

### 2단계: 수정본 확인하기

**결과 위치**: `workflow/outputs/story-[이름]/revised_final.md`

### 3단계: 추가 수정하기 (선택)

수정본이 마음에 안 들면 계속 수정 가능:

```
workflow/prompts/R1-revision-mode.md를 읽고,
workflow/outputs/story-01/revised_final.md에 대해 다음 피드백을 반영해서 수정해줘:
"추가 피드백 내용"
```

---

## 케이스 3: 터치업 적용하기

최종본(08-final.md)의 문체를 보강하고 싶을 때:

```
workflow/prompts/10-touchup.md를 읽고,
workflow/outputs/story-01/08-final.md에 터치업을 적용해줘.
```

**터치업이 하는 일**:
1. 대화 연속 구간에 서술 단락 삽입
2. 단문 연속 구간의 리듬 조정

**결과 위치**: 
- `workflow/outputs/story-01/09-polished.md` (터치업 완성본)
- `workflow/outputs/story-01/09-touchup-report.md` (터치업 리포트)

---

## 빠른 참고

### 요청 예시 요약

```
# 새로 작성 (전체 프로세스)
workflow/prompts/00-start-guide.md를 읽고,
workflow/inputs/input.md의 소재로 전체 프로세스를 실행해줘.
도메인은 "언론/탐사보도"야.
작품 이름은 "story-01"로 해줘.

# 새로 작성 (도메인 없이)
workflow/prompts/00-start-guide.md를 읽고,
workflow/inputs/input.md의 소재로 전체 프로세스를 실행해줘.
작품 이름은 "my-story"로 해줘.

# 터치업 적용
workflow/prompts/10-touchup.md를 읽고,
workflow/outputs/story-01/08-final.md에 터치업을 적용해줘.

# 수정
workflow/prompts/R1-revision-mode.md를 읽고,
workflow/outputs/story-01/08-final.md에 대해 다음 피드백을 반영해서 수정해줘:
"피드백 내용"
```

### 파일 위치 요약

| 파일 | 위치 | 용도 |
|------|------|------|
| `input.md` | workflow/inputs/ | 소재 작성 |
| `00-start-guide.md` | workflow/prompts/ | 시작 가이드 |
| `10-touchup.md` | workflow/prompts/ | 터치업 모드 |
| `R1-revision-mode.md` | workflow/prompts/ | 재작성 모드 |
| `08-final.md` | workflow/outputs/story-[이름]/ | 최종 완성본 |
| `09-polished.md` | workflow/outputs/story-[이름]/ | 터치업 완성본 |
| `revised_final.md` | workflow/outputs/story-[이름]/ | 수정된 완성본 |
| `TOUCHUP_GUIDE.md` | workflow/references/ | 문장 리듬 가이드 |
| `NARRATIVE_GUIDE.md` | workflow/references/ | 서사 기법 가이드 |

---

## 파이프라인 흐름

```
[소재] → 리서처 → 철학자 → 소설가A(시놉시스)
                              ↓
                         소설가B(비평)
                              ↓
                         소설가A(초고)
                              ↓
                           편집자
                              ↓
                         소설가A(수정)
                              ↓
                           비평가
                              ↓
                         소설가A(최종) → [08-final.md]
                              ↓
                        터치업(선택) → [09-polished.md]
```

각 단계는 이전 단계의 결과물을 입력으로 받아 작업합니다.
모든 상세 지침은 각 프롬프트 파일에 완전히 포함되어 있습니다.

---

## 문장 리듬과 서사 기법 가이드

### 문장 리듬 원칙 (TOUCHUP_GUIDE.md)

한국 중견작가(이청준, 오정희, 박완서, 윤흥길)의 문체 분석 기반:

**핵심**: "단문은 예외, 복문이 기본"

| 문장 유형 | 비율 목표 | 용도 |
|----------|----------|------|
| **장문** (40자+) | 25-35% | 내면 묘사, 분위기 |
| **중문** (16-40자) | 50-60% | 기본 서술 |
| **단문** (15자 이하) | **15-20%** | 절정/충격 순간만 |

**금지 규칙**:
- ❌ 단문 연속 3문장 이상
- ❌ 장면 전환(---) 직후 단문 시작
- ❌ 내면 독백 파편화

### 서사 기법 가이드 (NARRATIVE_GUIDE.md)

이문열, 신경숙, 황석영 등 17편의 한국 현대 단편소설 분석 기반:

**감정 곡선 분량 비율**:
| 구간 | 비율 | 핵심 |
|------|------|------|
| 도입 | 10-15% | 훅, 복선 |
| 전개 | 25-30% | 갈등 표면화 |
| 위기 | 30-35% | **가장 힘 빠지기 쉬움** |
| 절정 | 15-20% | 결정적 순간 |
| 결말 | 10-15% | 여운, 열린 이미지 |

**중반 긴장 유지 5대 기법**:
1. 새로운 장애물 투입
2. 점층적 폭로
3. 기대 뒤집기
4. 시간 압박
5. 내적/외적 갈등 교차

---

## 언론 도메인 지식베이스 (cr-knowledge)

언론 도메인(`언론/탐사보도`, `언론/방송뉴스`) 선택 시 자동으로 로드되는 전문 지식입니다.

### 포함 내용

| 파일 | 내용 | 소설적 활용 |
|------|------|------------|
| `01-problem-awareness.md` | 언론 문제 인식 배경 | 동기 부여, 세계관 |
| `02-journalism-reality.md` | 언론 현장 실제 | 현실적 장면 묘사 |
| `03-problematic-patterns.md` | 119개 문제적 보도 패턴 | 기자의 일상, 편집국 갈등 |
| `04-citizen-solution.md` | 7개 윤리규범 + 시민 해결책 | 윤리적 딜레마 장면 |
| `05-cr-depiction-guide.md` | CR 도구 묘사 가이드 | CR-Check 등장 시 정확한 묘사 |

### 핵심 개념

**1. 자율규제의 역설**
- 언론윤리규범은 법이 아님 (법적 강제력 없음)
- 현실에서는 마감 압박, 속보 경쟁으로 지켜지지 않음
- **시민이 요구하는 것의 의미**: 언론 스스로 못 지키는 규범을 외부에서 환기

**2. 윤리규범의 진화**
- 규범은 고정된 것이 아님, 시대에 따라 변해야 함
- **자살예방 보도준칙의 역설**: 조심스러운 보도가 사회문제를 가림
- **새로운 매체 문제**: 유튜브 뉴스에는 윤리강령이 적용 안 됨

### 소설에서 활용 예시

```
"그거 누가 지켜? 법도 아닌데."
"법이 아니라서 못 지킨다고? 그럼 왜 만들었는데?"

"자살예방 준칙 때문에 보도를 못 했어.
 근데 그래서 아무도 왜 그 아이들이 죽었는지 모르게 됐어."

"유튜버가 우리 기사 짜깁기해서 300만 뷰 찍었는데,
 우리가 뭘 할 수 있어? 걔네한텐 윤리강령이 없잖아."
```

---

## 레퍼런스 작품 17편

`workflow/references/[References] Korean Short Stories/` 폴더에 한국 현대 단편소설이 참조 자료로 포함되어 있습니다.

| 작가 | 작품 |
|------|------|
| 이문열 | 우리들의 일그러진 영웅 |
| 신경숙 | 빈집 |
| 황석영 | 아우를 위하여 |
| 오정희 | 동경 |
| 박완서 | 꿈꾸는 인큐베이터 |
| 윤흥길 | 장마, 아홉켤레의 구두로 남은 사내 |
| 이청준 | 눈길, 병신과 머저리 |
| 박경리 | 불신 시대 |
| 조세희 | 뫼비우스의 띠 |
| 양귀자 | 비오는 날이면 가리봉동에 가야 한다 |
| 전상국 | 우상의 눈물 |
| 최인호 | 타인의 방 |
| 박상우 | 샤갈의 마을에 내리는 눈 |
| 구효서 | 카프카를 읽는 밤 |
| 박성원 | 유서 |

---

## 자주 묻는 질문

**Q. 소요 시간은?**
A. 약 10-20분 (전체 프로세스 기준), 터치업 추가 시 +5분

**Q. 기존 파일을 덮어쓰나요?**
A. 작품별로 별도 폴더(story-[이름])가 생성되므로 덮어쓰지 않습니다.

**Q. 도메인 없이 써도 되나요?**
A. 네, 기본 모드도 충분합니다.

**Q. 반복 수정 가능한가요?**
A. 네, 무제한 가능합니다.

**Q. 터치업은 필수인가요?**
A. 아니요, 선택입니다. 08-final.md가 이미 충분히 좋다면 생략해도 됩니다.

**Q. 분량 기준이 있나요?**
A. 최소 8,000자 이상, 권장 10,000-15,000자입니다. 장면당 최소 300자 이상으로 요약 없이 구체적으로 전개해야 합니다.

**Q. 문장 리듬 원칙이 뭔가요?**
A. 한국 중견작가 문체 분석 기반으로, 단문(15자 이하)은 20% 이하, 연속 3문장 금지입니다. 자세한 내용은 `workflow/references/TOUCHUP_GUIDE.md` 참조.

**Q. 중반이 힘 빠지는 문제가 있어요.**
A. 서사 기법 가이드(NARRATIVE_GUIDE.md)의 "중반 긴장 유지 5대 기법"을 참조하세요. 새 장애물 투입, 점층적 폭로, 기대 뒤집기, 시간 압박, 내적/외적 갈등 교차 기법이 있습니다.

**Q. 언론 도메인이 특별한 이유가 있나요?**
A. 네, 언론 도메인 선택 시 CR 프로젝트의 전문 지식베이스가 자동으로 로드됩니다:
- **119개 문제적 보도 패턴** (따옴표 저널리즘, 양비론, 받아쓰기 등)
- **7개 언론윤리규범** (언론윤리헌장, 신문윤리강령, 기자윤리강령 등)
- **자율규제의 역설**: 법적 구속력 없는 규범, 시민 참여의 의미
- **CR 묘사 가이드**: CR-Check 도구가 등장할 때 정확한 묘사법

이 지식은 `workflow/references/cr-knowledge/` 폴더에 있습니다.

**Q. 단계별로 확인하며 진행하고 싶어요.**
A. 전체 실행 대신 각 프롬프트 파일을 순서대로 실행하면 됩니다. 각 단계 완료 후 결과를 확인하고 피드백을 줄 수 있습니다.

**Q. 여러 작품을 동시에 작업할 수 있나요?**
A. 네, 작품 이름만 다르게 지정하면 됩니다 (story-01, story-02, my-novel 등).

---

## 가장 간단한 시작법

1. `workflow/inputs/input.md`에 소재 적기
2. Claude Code에서:
   ```
   workflow/prompts/00-start-guide.md를 읽고,
   workflow/inputs/input.md의 소재로 전체 프로세스를 실행해줘.
   작품 이름은 "my-story"로 해줘.
   ```
3. `workflow/outputs/my-story/08-final.md` 확인
4. (선택) 터치업 적용:
   ```
   workflow/prompts/10-touchup.md를 읽고,
   workflow/outputs/my-story/08-final.md에 터치업을 적용해줘.
   ```

**끝!**
