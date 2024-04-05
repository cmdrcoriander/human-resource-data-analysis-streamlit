import streamlit as st 
import streamlit.components.v1 as components

with st.container():
   st.write("This is inside the container")

   components.iframe("https://app.spline.design/file/7f0a8d9b-6103-4561-b0eb-af35e9250e24", height=600)
