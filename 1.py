import streamlit as st

st.title("入门演示")
st.header("一级标题")
st.subheader("二级标题")
# 引入文字
st.write("高高兴兴一家人")
st.write("欢迎小王")
st.image("./第一节/图片/吴海洋本科学位.jpg")
password = st.text_input("请输入姓名")
st.write(f"您输入的姓名:{password}")

st.radio("请输入性别",["男","女"])