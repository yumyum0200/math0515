import streamlit as st

# 1. 페이지 설정 및 디자인
st.set_page_config(page_title="YUM♡MATH 이차방정식 탐구", layout="wide")

st.markdown("""
    <style>
    .brand { position: fixed; top: 10px; right: 20px; font-size: 14px; color: #888888; font-weight: bold; z-index: 999; }
    .problem-box {
        font-size: 30px !important; line-height: 1.8; padding: 2.5rem;
        background-color: #f0f7ff; border-radius: 25px; border-left: 15px solid #a2d2ff; color: #1e1e1e; margin-bottom: 20px;
    }
    .highlight { background-color: #fff3cd; font-weight: 900; padding: 0 5px; border-radius: 5px; color: #d63384; }
    .stButton>button { width: 100%; height: 3em; font-size: 20px !important; font-weight: bold !important; border-radius: 12px; }
    .stSelectbox label, .stRadio label { font-size: 22px !important; font-weight: 600; }
    </style>
    <div class="brand">YUM♡MATH</div>
    """, unsafe_allow_html=True)

# 2. 세션 관리
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
    col1, col2, col3 = st.columns(3)
    if col1.button("1] 유기견 문제"): reset_mission(1); st.rerun()
    if col2.button("2] 상자 문제"): reset_mission(2); st.rerun()
    if col3.button("3] 감귤 문제"): reset_mission(3); st.rerun()

# ---------------------------------------------------------
# [문제 풀이 페이지]
# ---------------------------------------------------------
else:
    # 상단 네비게이션
    nav_col1, nav_col2, nav_col3, nav_spacer = st.columns([1.5, 1.5, 1.5, 5.5])
    if nav_col1.button("🏠 홈"): st.session_state.mission = 0; st.rerun()
    if st.session_state.page > 1:
        if nav_col2.button("⬅️ 뒤로"): move_page(-1)
    if st.session_state.page < 5:
        if nav_col3.button("다음 ➡️"): move_page(1)
    st.divider()

    # 데이터 설정
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

    # --- [2페이지] Step 1. 구하려는 것 (3:7 비율) ---
    elif st.session_state.page == 2:
        col_l, col_r = st.columns([3, 7])
        with col_l: st.info(p_text)
        with col_r:
            st.header("Step 1. 구하려는 것 파악하기")
            if st.button("💡 힌트"): st.warning("문제를 꼼꼼하게 다시 읽어보세요! 문제 속에 답이 있어요")
            target = "전체 유기견의 수" if st.session_state.mission == 1 else ("처음 종이의 한 변의 길이" if st.session_state.mission == 2 else "x의 값")
            ans = st.selectbox("이 문제에서 구하려고 하는 것은?", ["선택하세요", "상자의 높이", "전체 비스킷 수", target, "감귤의 무게"])
            if ans == target: st.success("정답입니다!")

    # --- [3페이지] Step 2. 식 세우기 ---
    elif st.session_state.page == 3:
        col_l, col_r = st.columns([3, 7])
        with col_l: st.info(p_text)
        with col_r:
            st.header("Step 2. 식 세우기")
            if st.session_state.mission == 1:
                st.selectbox("2-(1) 문제 이해하기: 전체 유기견의 수가 40마리일 때 한 마리당 비스킷 수는?", ["선택하세요", "13개", "27개", "67개"])
                st.selectbox("2-(2) 단서 찾기: 전체 유기견의 수가 x마리 일 때, 한 마리당 비스킷의 수를 x로 나타내면?", ["선택하세요", "x + 27", "x - 27", "27 - x"])
                st.selectbox("2-(3) 식 세우기:", ["선택하세요", "x + (x - 27) = 90", "x × (x - 27) = 90", "x - 27 = 90"])
            elif st.session_state.mission == 2:
                st.selectbox("2-(0) 기초 상식: 상자모양의 부피를 구하는 식은?", ["선택하세요", "(가로)×(세로)×(높이)", "(가로)+(세로)+(높이)", "(밑넓이)×2"])
                st.selectbox("2-(1) 문제 이해하기: 처음 한 변의 길이가 20cm라 하면 상자의 한 변의 길이는?", ["선택하세요", "10cm", "15cm", "5cm"])
                st.selectbox("2-(2) 단서 찾기: 처음 한 변의 길이를 xcm라 하면 상자의 한 변의 길이는?", ["선택하세요", "(x - 5)cm", "(x - 10)cm", "(x - 20)cm"])
                st.selectbox("2-(3) 식 세우기:", ["선택하세요", "(x-10) × (x-10) × 5 = 4500", "(x-5) × (x-5) × 5 = 4500"])
            else:
                st.selectbox("2-(1) 문제 이해하기: 전체 감귤의 양은 얼마일까?", ["선택하세요", "2000 × 4200", "2000 + 4200", "4200 ÷ 2000"])
                st.selectbox("2-(2) 단서 찾기: 한 상자에 들어가는 감귤의 양은?", ["선택하세요", "2000 + x", "2000 - x", "2000x"])
                st.selectbox("2-(3) 단서 찾기: 만들 수 있는 상자의 개수는?", ["선택하세요", "4200 - 2x", "4200 + 2x", "4200 - x"])
                st.selectbox("2-(4) 식 세우기:", ["선택하세요", "(2000+x)×(4200-2x)=2000×4200", "(2000+x)+(4200-2x)=8400000"])

    # --- [4페이지] Step 3. 방정식 풀기 ---
    elif st.session_state.page == 4:
        col_l, col_r = st.columns([3, 7])
        with col_l:
            if st.session_state.mission == 1: st.latex(r"x^2 - 27x - 90 = 0")
            elif st.session_state.mission == 2: st.latex(r"5(x-10)^2 = 4500")
            else: st.latex(r"(2000+x)(4200-2x) = 8400000")
        with col_r:
            st.header("3단계 : 방정식 풀기")
            if st.session_state.mission == 1:
                st.selectbox("3-(1) 위 식을 인수분해 하면?", ["선택하세요", "(x + 3)(x - 30) = 0", "(x - 3)(x + 30) = 0", "(x - 9)(x - 10) = 0"])
                st.selectbox("3-(2) 이 방정식의 해는?", ["선택하세요", "x = -3 또는 x = 30", "x = 3 또는 x = -30", "x = 30"])
                st.selectbox("3-(3) 생각하기: 왜 x = -3은 답이 될 수 없을까요?", ["선택하세요", "유기견 수는 자연수(양수)여야 하므로", "비스킷이 부족해서", "계산 착오"])
            elif st.session_state.mission == 2:
                st.selectbox("3-(1) 위 식을 제곱근을 이용하여 해를 구하는 과정에서 바른 식은?", ["선택하세요", "x - 10 = ±30", "x - 10 = ±900", "x - 10 = 30"])
                st.selectbox("3-(2) 위 방정식의 해는?", ["선택하세요", "x = -20 또는 x = 40", "x = 20 또는 x = -40", "x = 40"])
                st.selectbox("3-(3) 생각하기: 왜 x = -20은 답이 될 수 없을까요?", ["선택하세요", "길이는 양수여야 하므로", "종이가 찢어져서", "부피가 너무 커서"])
            else:
                st.selectbox("3-(1) 앞에서 구한 이차방정식을 바르게 정리한 것은?", ["선택하세요", "x^2 - 100x = 0", "x^2 + 100x = 0", "x^2 - 200x = 0"])
                st.selectbox("3-(2) 위 식을 바르게 인수분해 한 것은?", ["선택하세요", "x(x - 100) = 0", "x(x + 100) = 0", "(x - 100)(x + 100) = 0"])
                st.selectbox("3-(3) 생각하기: 인수분해 결과를 보고 해를 고르면?", ["선택하세요", "x = 0 또는 x = 100", "x = 0 또는 x = -100", "x = 100"])

    # --- [5페이지] Step 4. 확인하기 ---
    elif st.session_state.page == 5:
        st.header("Step 4. 확인하기")
        if st.session_state.mission == 1:
            c1, c2 = st.columns(2)
            v1 = c1.number_input("유기견의 수 (x)", min_value=0, key="m1_1")
            v2 = c2.number_input("한 마리당 비스킷 수 (x - 27)", min_value=0, key="m1_2")
            if st.button("결과 확인"):
                res = v1 * v2
                st.markdown(f"### 계산된 비스킷 수: {res}개")
                if res == 90: st.balloons(); st.success("문제를 바르게 해결했습니다! 수고하셨습니다!")
                else: st.error("값이 90이 되지 않습니다. 다시 확인해 보세요!")
        elif st.session_state.mission == 2:
            c1, c2 = st.columns(2)
            v1 = c1.number_input("처음 종이의 한 변의 길이", min_value=0, key="m2_1")
            v2 = c2.number_input("상자 밑면의 한 변의 길이 (x - 10)", min_value=0, key="m2_2")
            if st.button("결과 확인"):
                res = v2 * v2 * 5
                st.markdown(f"### 계산된 상자 부피: {res}㎤")
                if res == 4500: st.balloons(); st.success("문제를 바르게 해결했습니다! 수고하셨습니다!")
                else: st.error("부피가 4500이 되지 않습니다. 다시 확인해 보세요!")
        else:
            c1, c2 = st.columns(2)
            v1 = c1.number_input("한 상자에 더 넣는 귤의 양 (x)", min_value=0, key="m3_1")
            v2 = c2.number_input("상자의 개수 (4200 - 2x)", min_value=0, key="m3_2")
            if st.button("결과 확인"):
                res = (2000 + v1) * v2
                st.markdown(f"### 계산된 전체 귤의 양: {res}g")
                if res == 8400000: st.balloons(); st.success("문제를 바르게 해결했습니다! 수고하셨습니다!")
                else: st.error("전체 양이 8,400,000이 되지 않습니다. 다시 확인해 보세요!")