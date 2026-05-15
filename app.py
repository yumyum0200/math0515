import streamlit as st

# 1. 페이지 설정 (최상단 배치)
st.set_page_config(page_title="YUM♡MATH 이차방정식 탐구", layout="wide")

# 2. 모든 페이지 공통 스타일 및 브랜드명 주입 (CSS Fixed 사용)
st.markdown("""
    <style>
    /* 우측 상단 브랜드 로고 상시 고정 */
    .brand-sticker {
        position: fixed;
        top: 20px;
        right: 30px;
        font-size: 16px;
        color: #d63384; /* 선생님의 브랜드를 돋보이게 할 색상 */
        font-weight: bold;
        z-index: 10000; /* 어떤 요소보다도 위에 표시 */
        background-color: rgba(255, 255, 255, 0.7); /* 배경을 살짝 투명하게 */
        padding: 4px 8px;
        border-radius: 8px;
    }
    .problem-box {
        font-size: 30px !important; line-height: 1.8; padding: 2.5rem;
        background-color: #f0f7ff; border-radius: 25px; border-left: 15px solid #a2d2ff; color: #1e1e1e; margin-bottom: 20px;
    }
    .highlight { background-color: #fff3cd; font-weight: 900; padding: 0 5px; border-radius: 5px; color: #d63384; }
    .stButton>button { width: 100%; height: 3em; font-size: 20px !important; font-weight: bold !important; border-radius: 12px; }
    .stSelectbox label, .stRadio label { font-size: 22px !important; font-weight: 600; }
    .side-problem {
        padding: 15px; background-color: #f8f9fa; border-radius: 10px; border: 1px solid #dee2e6; font-size: 18px; line-height: 1.6;
    }
    </style>
    <div class="brand-sticker">YUM♡MATH</div>
    """, unsafe_allow_html=True)

# 3. 세션 관리 초기화
if 'mission' not in st.session_state: st.session_state.mission = 0
if 'page' not in st.session_state: st.session_state.page = 1
if 'kw_on' not in st.session_state: st.session_state.kw_on = False

def reset_mission(m_idx):
    st.session_state.mission = m_idx
    st.session_state.page = 1
    st.session_state.kw_on = False

def move_page(delta):
    st.session_state.page += delta
    st.rerun()

# ---------------------------------------------------------
# [메인 페이지]
# ---------------------------------------------------------
if st.session_state.mission == 0:
    st.title("📐 이차방정식의 활용 미션")
    st.write("풀고 싶은 미션을 선택해 주세요!")
    col1, col2, col3 = st.columns(3)
    if col1.button("1] 유기견 문제"): reset_mission(1); st.rerun()
    if col2.button("2] 상자 문제"): reset_mission(2); st.rerun()
    if col3.button("3] 감귤 문제"): reset_mission(3); st.rerun()

# ---------------------------------------------------------
# [문제 풀이 페이지 공통 구조]
# ---------------------------------------------------------
else:
    # 상단 네비게이션 버튼 (홈, 뒤로, 앞으로)
    nav_col1, nav_col2, nav_col3, nav_spacer = st.columns([1.5, 1.5, 1.5, 5.5])
    if nav_col1.button("🏠 홈"): st.session_state.mission = 0; st.rerun()
    if st.session_state.page > 1:
        if nav_col2.button("⬅️ 뒤로"): move_page(-1)
    if st.session_state.page < 5:
        if nav_col3.button("다음 ➡️"): move_page(1)
    st.divider()

    # 데이터 설정 (각 미션별 텍스트)
    if st.session_state.mission == 1:
        title, p_text = "유기견 보호소 비스킷 나눔", "어느 유기견 보호소에서는 간식용 비스킷 90개를 전체 유기견에게 똑같이 나누어 주려고 한다. 유기견 한 마리 당 나누어 준 비스킷의 개수가 전체 유기견의 수보다 27만큼 작다고 할 때, 전체 유기견의 수를 구하시오."
        keywords = ["비스킷 90개", "한 마리랑 비스킷 개수가 전체 유기견의 수보다 27만큼 작다", "전체 유기견의 수"]
    elif st.session_state.mission == 2:
        title, p_text = "정사각형 종이 상자 만들기", "정사각형 모양의 종이가 있다. 이 종이의 네 귀퉁이를 한 변의 길이가 5cm인 정사각형 모양으로 잘라내어 포장 상자를 만들 때, 포장 상자의 부피가 4500㎤가 되도록 하는 처음 종이의 한 변의 길이를 구하시오."
        keywords = ["한 변의 길이가 5cm", "포장 상자의 부피가 4500㎤", "처음 종이의 한 변의 길이"]
    else:
        title, p_text = "감귤 농장 상자 포장", "어느 감귤 농장에서는 한 상자에 2000g씩 포장하면 4200개의 상자를 채울 수 있는 양을 생산하였다고 한다. 한 상자에 x g씩 더 넣으면 상자는 2x개만큼 줄어든다고 할 때, x의 값을 구하시오. (단, 상자의 무게는 생각하지 않는다.)"
        keywords = ["한 상자에 2000g씩 포장하면 4200개의 상자", "한 상자에 x g씩 더 넣으면 상자는 2x개만큼 줄어든다", "x의 값을 구하시오"]

    st.subheader(f"🚀 Mission 0{st.session_state.mission}. {title}")

    # --- [1페이지] 문제 탐색 ---
    if st.session_state.page == 1:
        prob_display = p_text
        if st.session_state.kw_on:
            for kw in keywords: prob_display = prob_display.replace(kw, f"<span class='highlight'>{kw}</span>")
        st.markdown(f'<div class="problem-box">{prob_display}</div>', unsafe_allow_html=True)
        if st.button("🖍️ Key Word"):
            st.session_state.kw_on = not st.session_state.kw_on
            st.rerun()

    # --- [2~5페이지] 3:7 레이아웃 ---
    else:
        col_l, col_r = st.columns([3, 7])
        with col_l:
            st.markdown(f'<div class="side-problem"><b>[문제 원문]</b><br>{p_text}</div>', unsafe_allow_html=True)
            if st.session_state.page >= 3:
                st.write("---")
                st.write("💡 **참고 수식**")
                if st.session_state.mission == 1: st.latex(r"x(x-27)=90")
                elif st.session_state.mission == 2: st.latex(r"5(x-10)^2=4500")
                else: st.latex(r"(2000+x)(4200-2x)=8400000")

        with col_r:
            # --- Step 1 ---
            if st.session_state.page == 2:
                st.header("Step 1. 구하려는 것 파악하기")
                target = "전체 유기견의 수" if st.session_state.mission == 1 else ("처음 종이의 한 변의 길이" if st.session_state.mission == 2 else "x의 값")
                ans = st.selectbox("구하려는 항목은?", ["선택하세요", target, "상자의 높이", "전체 비스킷 수"])
                if ans == target: st.success("정답입니다!")

            # --- Step 2 ---
            elif st.session_state.page == 3:
                st.header("Step 2. 식 세우기")
                if st.session_state.mission == 1:
                    st.selectbox("2-(1) 이해: 유기견이 40마리면 한 마리당 비스킷은?", ["선택하세요", "13개", "27개", "67개"])
                    st.selectbox("2-(2) 단서: 유기견이 x마리면 한 마리당 비스킷 수는?", ["선택하세요", "x-27", "x+27"])
                    st.selectbox("2-(3) 식 세우기:", ["선택하세요", "x(x-27)=90", "x+(x-27)=90"])
                elif st.session_state.mission == 2:
                    st.selectbox("2-(0) 기초: 부피 공식은?", ["선택하세요", "(가로)×(세로)×(높이)", "(가로)+(세로)+(높이)"])
                    st.selectbox("2-(1) 이해: 처음이 20cm면 상자 밑면 한 변은?", ["선택하세요", "10cm", "15cm"])
                    st.selectbox("2-(2) 단서: 처음이 xcm면 상자 밑면 한 변은?", ["선택하세요", "x-10", "x-5"])
                    st.selectbox("2-(3) 식 세우기:", ["선택하세요", "5(x-10)^2=4500", "5(x-5)^2=4500"])
                else:
                    st.selectbox("2-(1) 이해: 전체 감귤 양은?", ["선택하세요", "2000×4200", "2000+4200"])
                    st.selectbox("2-(2) 단서: 한 상자 당 양은?", ["선택하세요", "2000+x", "2000-x"])
                    st.selectbox("2-(3) 단서: 상자 개수는?", ["선택하세요", "4200-2x", "4200+2x"])
                    st.selectbox("2-(4) 식 세우기:", ["선택하세요", "(2000+x)(4200-2x)=8400000"])

            # --- Step 3 ---
            elif st.session_state.page == 4:
                st.header("Step 3. 방정식 풀기")
                if st.session_state.mission == 1:
                    st.selectbox("3-(1) 위 식을 인수분해 하면?", ["선택하세요", "(x+3)(x-30)=0", "(x-3)(x+30)=0"])
                    st.selectbox("3-(2) 이 방정식의 해는?", ["선택하세요", "x=-3 또는 x=30", "x=30"])
                    st.selectbox("3-(3) 왜 x=-3은 안 될까요?", ["선택하세요", "유기견 수는 양수여야 하므로", "비스킷이 부족해서"])
                elif st.session_state.mission == 2:
                    st.selectbox("3-(1) 제곱근 풀이 중 바른 식은?", ["선택하세요", "x-10=±30", "x-10=30"])
                    st.selectbox("3-(2) 위 방정식의 해는?", ["선택하세요", "x=-20 또는 x=40", "x=40"])
                    st.selectbox("3-(3) 왜 x=-20은 안 될까요?", ["선택하세요", "길이는 양수여야 하므로", "부피가 너무 커서"])
                else:
                    st.selectbox("3-(1) 식을 정리하면?", ["선택하세요", "x^2-100x=0", "x^2+100x=0"])
                    st.selectbox("3-(2) 인수분해 하면?", ["선택하세요", "x(x-100)=0", "x(x+100)=0"])
                    st.selectbox("3-(3) 해를 고르면?", ["선택하세요", "x=100", "x=0"])

            # --- Step 4 ---
            elif st.session_state.page == 5:
                st.header("Step 4. 확인하기")
                if st.session_state.mission == 1:
                    v1 = st.number_input("유기견의 수(x)", min_value=0)
                    v2 = st.number_input("한 마리당 비스킷 수(x-27)", min_value=0)
                    if st.button("최종 확인") and v1 * v2 == 90: st.balloons(); st.success("문제를 바르게 해결했습니다! 수고하셨습니다!")
                elif st.session_state.mission == 2:
                    v1 = st.number_input("처음 종이 한 변(x)", min_value=0)
                    v2 = st.number_input("상자 밑면 한 변(x-10)", min_value=0)
                    if st.button("최종 확인") and v2 * v2 * 5 == 4500: st.balloons(); st.success("문제를 바르게 해결했습니다! 수고하셨습니다!")
                else:
                    v1 = st.number_input("더 넣는 귤의 양(x)", min_value=0)
                    v2 = st.number_input("상자의 개수(4200-2x)", min_value=0)
                    if st.button("최종 확인") and (2000+v1)*v2 == 8400000: st.balloons(); st.success("문제를 바르게 해결했습니다! 수고하셨습니다!")