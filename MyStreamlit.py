import streamlit as st

st.image('./pic/kairung.jfif')
col1, col2 = st.columns(2)
with col1:
  st.header('ไก้รุ่ง เฮงพระพรหม')
with col2:
  st.subheader('สาขาวิชาวิทยาการข้อมูล')
  st.text('คณะวิทยาศาสตร์และเทคโนโลยี')