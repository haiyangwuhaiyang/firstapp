import streamlit as st

st.title("好好好")
st.header("尝试一个网页")
st.subheader("开始吧")
# 引入文字
st.write("高高兴兴一家人")
st.write("欢迎小王")
st.image("./第一节/cat.jpg")
password = st.text_input("请输入姓名")
st.write(f"您输入的姓名:{password}")

st.radio("请输入性别",["男","女"])