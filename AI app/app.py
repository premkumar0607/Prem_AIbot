import streamlit as st
import google.generativeai as genai

st.title("WELCOME TO MY AI BOT INTERGATED WITH GEMINI AI")

genai.configure(api_key="AIzaSyDn6fAJ3CVAa37scoO28pxmC_wUqY-o8Lk")

text = st.text_input("Ask Anything")

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

if st.button("Click Here"):
  response = chat.send_message(text)
  st.write(response.text)