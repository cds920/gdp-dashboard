

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os



# 한글 폰트 설정 (NanumGothic)
FONT_PATH = os.path.join(os.path.dirname(__file__), '../fonts/NanumGothic-Regular.ttf')
fontprop = fm.FontProperties(fname=FONT_PATH)
plt.rcParams['axes.unicode_minus'] = False

st.title(":bar_chart: 학생 성적 분석")
st.caption("학생별 성적을 입력하면 등수, 평균, 그룹화 결과를 보여줍니다.")

st.header("1. 학생 성적 입력")
example = """이름,국어,영어,수학
홍길동,90,85,95
김철수,80,70,88
이영희,100,95,98
박민수,60,75,70
최지우,85,90,92
"""
csv_text = st.text_area("학생별 성적을 CSV 형식으로 입력하세요.", example, height=150)

import io
try:
	df = pd.read_csv(io.StringIO(csv_text))
except Exception:
	st.error("CSV 형식이 올바르지 않습니다.")
	st.stop()

if not {'이름', '국어', '영어', '수학'}.issubset(df.columns):
	st.error("'이름,국어,영어,수학' 형식으로 입력해주세요.")
	st.stop()

st.subheader("입력 데이터")
st.dataframe(df, use_container_width=True)

# 평균, 총점, 등수 계산
df['총점'] = df[['국어', '영어', '수학']].sum(axis=1)
df['평균'] = df[['국어', '영어', '수학']].mean(axis=1)
df['등수'] = df['총점'].rank(ascending=False, method='min').astype(int)
df = df.sort_values('등수')

st.subheader("등수 및 평균")
st.dataframe(df[['이름', '국어', '영어', '수학', '총점', '평균', '등수']], use_container_width=True)

st.subheader("과목별 평균")
avg_row = pd.DataFrame({
	'이름': ['과목평균'],
	'국어': [df['국어'].mean()],
	'영어': [df['영어'].mean()],
	'수학': [df['수학'].mean()],
	'총점': [df['총점'].mean()],
	'평균': [df['평균'].mean()],
	'등수': ['-']
})
st.table(avg_row)



st.subheader("성적 분포 시각화 (matplotlib)")
fig, ax = plt.subplots(figsize=(7, 4))
df_plot = df.set_index('이름')[['국어', '영어', '수학']]
df_plot.plot(kind='bar', ax=ax)
ax.set_ylabel('점수', fontproperties=fontprop)
ax.set_xlabel('이름', fontproperties=fontprop)
ax.set_title('과목별 성적 분포', fontproperties=fontprop)
ax.legend(prop=fontprop)
for label in ax.get_xticklabels():
	label.set_fontproperties(fontprop)
for label in ax.get_yticklabels():
	label.set_fontproperties(fontprop)
st.pyplot(fig)

st.subheader("그룹화: 평균 90점 이상 우수 그룹")
df['그룹'] = np.where(df['평균'] >= 90, '우수', '일반')
st.dataframe(df[['이름', '평균', '그룹']], use_container_width=True)
