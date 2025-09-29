

import streamlit as st
import random
import pandas as pd

st.set_page_config(page_title="자리배치 웹앱", page_icon=":school:", layout="wide")
st.title(":school: 교실 자리배치 웹앱")
st.caption("학생 명단을 입력하면 무작위로 자리배치를 해줍니다.")

st.header("1. 학생 명단 입력")
names_text = st.text_area(
    "학생 이름을 한 줄에 하나씩 입력하세요.",
    "홍길동\n김철수\n이영희\n박민수\n최지우"
)
names = [name.strip() for name in names_text.split("\n") if name.strip()]

st.header("2. 교실 좌석 설정")
cols = st.number_input("가로(열) 좌석 수", min_value=2, max_value=10, value=5)
rows = st.number_input("세로(행) 좌석 수", min_value=2, max_value=10, value=4)

if st.button("자리배치 시작!"):
    total_seats = int(cols * rows)
    if len(names) > total_seats:
        st.error(f"입력한 학생 수({len(names)})가 좌석 수({total_seats})보다 많아요!")
    else:
        # 자리 무작위 배정
        seat_list = names + [""] * (total_seats - len(names))
        random.shuffle(seat_list)
        seat_matrix = [seat_list[i*int(cols):(i+1)*int(cols)] for i in range(int(rows))]
        st.success("자리배치 결과입니다!")
        st.dataframe(pd.DataFrame(seat_matrix, columns=[f"{i+1}열" for i in range(int(cols))]))
        
        st.header("시각화")
        for r, row in enumerate(seat_matrix):
            cols_ = st.columns(int(cols))
            for c, student in enumerate(row):
                with cols_[c]:
                    st.button(student if student else "빈자리", key=f"{r}-{c}")

st.info("Tip: 학생 명단을 복사/붙여넣기해서 쉽게 입력할 수 있습니다.")
