
import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title="Streamlit Elements Showcase", page_icon=":star:", layout="wide")

st.title(":star: Streamlit 요소 총집합 데모")
st.caption("Streamlit에서 제공하는 다양한 UI 요소와 기능을 한 페이지에 모았습니다.")

st.header("기본 텍스트 요소")
st.text("이것은 일반 텍스트입니다.")
st.markdown("**마크다운** _스타일링_ :rainbow:")
st.code("print('Hello, Streamlit!')", language="python")
st.latex(r"""
E = mc^2
""")
st.write("st.write()는 다양한 타입을 자동으로 렌더링합니다.", {"a": 1, "b": 2})

st.header("데이터 표시")
df = pd.DataFrame(np.random.randn(10, 5), columns=list("ABCDE"))
st.dataframe(df, use_container_width=True)
st.table(df.head(3))

st.header("차트와 그래프")
st.line_chart(df)
st.bar_chart(df)
st.area_chart(df)

st.header("상호작용 위젯")
name = st.text_input("이름을 입력하세요:", "홍길동")
age = st.number_input("나이", min_value=0, max_value=120, value=25)
agree = st.checkbox("개인정보 제공에 동의합니다.")
gender = st.radio("성별", ["남성", "여성", "기타"])
color = st.selectbox("좋아하는 색상", ["빨강", "초록", "파랑", "노랑"])
multi = st.multiselect("관심 있는 분야", ["AI", "데이터", "웹", "모바일", "게임"])
date = st.date_input("날짜 선택")
time = st.time_input("시간 선택")
slider = st.slider("점수(0~100)", 0, 100, 50)
file = st.file_uploader("파일 업로드")
st.color_picker("색상 선택", "#00f900")

st.header("버튼과 폼")
if st.button("버튼 클릭!"):
    st.success(f"{name}님, 버튼을 클릭하셨습니다!")

with st.form("my_form"):
    st.write("폼 내부 요소 예시")
    form_text = st.text_input("폼 텍스트 입력")
    submitted = st.form_submit_button("제출")
    if submitted:
        st.info(f"폼 제출: {form_text}")

st.header("상태 표시 및 알림")
st.success("성공 메시지 예시")
st.info("정보 메시지 예시")
st.warning("경고 메시지 예시")
st.error("에러 메시지 예시")
with st.spinner("로딩 중..."):
    import time; time.sleep(0.5)
st.balloons()

st.header("사이드바")
st.sidebar.title("사이드바 제목")
st.sidebar.write("사이드바에 다양한 위젯을 넣을 수 있습니다.")
sidebar_option = st.sidebar.selectbox("옵션 선택", ["옵션1", "옵션2", "옵션3"])

st.header("탭, 컬럼, 익스팬더")
tab1, tab2 = st.tabs(["탭 1", "탭 2"])
with tab1:
    st.write("첫 번째 탭 내용")
with tab2:
    st.write("두 번째 탭 내용")

col1, col2, col3 = st.columns(3)
col1.metric("온도", "23°C", "+1.2°C")
col2.metric("습도", "60%", "-5%")
col3.metric("강수량", "5mm", "+2mm")

with st.expander("더보기/접기 예시"):
    st.write("이곳에 추가 설명이나 옵션을 넣을 수 있습니다.")

st.header("카메라 입력, 오디오, 비디오")
# 카메라 입력은 실제 웹캠이 있을 때만 동작
st.camera_input("사진 촬영")
st.audio(np.random.randn(44100), sample_rate=44100)
st.video("https://www.w3schools.com/html/mov_bbb.mp4")

st.header("진행률, 상태바")
import time
progress = st.progress(0)
for i in range(1, 101, 10):
    time.sleep(0.05)
    progress.progress(i)
st.write("진행 완료!")

st.header("코드 실행 및 예외 처리")
try:
    st.write(1 / 0)
except Exception as e:
    st.exception(e)

st.header("st.session_state 예시")
if 'count' not in st.session_state:
    st.session_state['count'] = 0
if st.button("카운트 증가"):
    st.session_state['count'] += 1
st.write(f"카운트: {st.session_state['count']}")
