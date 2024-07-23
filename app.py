import streamlit as st

# data = [1,2,3]
url = 'https://naver.com'

# 입력화면- HTML/CSS/JS 로 최종적으로 변환
val1 = st.button("강아지")
val2 = st.button("고양이")
val3 = st.button("포차코")

# 동작 - HTML/CSS/JS 로 최종적으로 변환
if val1:
    st.image('./data/강아지.jpg')
elif val2:
    st.image('./data/고양이.jpg')
else:
    st.image('./data/포차코.jpg')

# 출력 
st.write(val1)