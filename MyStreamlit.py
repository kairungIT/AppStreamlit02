import streamlit as st

st.image('./pic/kairung.jfif')
col1, col2 = st.columns(2)
with col1:
  st.header('ไก้รุ่ง เฮงพระพรหม')
with col2:
  st.subheader('สาขาวิชาวิทยาการข้อมูล')
  st.text('คณะวิทยาศาสตร์และเทคโนโลยี')

  html_1 = """
<div style="background-color:#76D7C4;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h4>การทำนายข้อมูลดอกไม้เบื้องต้น</h4></center>
</div>
"""
st.markdown(html_1, unsafe_allow_html=True)
st.markdown("")