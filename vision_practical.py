import streamlit as st
import os
from PIL import Image

os.environ['GEMINI_API_KEY'] = '' # use GeminiAPI key

import google.generativeai as genai
genai.configure(api_key=os.environ['GEMINI_API_KEY'])

## Function to load OpenAI model and get respones

def get_gemini_response(input,image):
    model = genai.GenerativeModel('gemini-pro-vision')
    if input!="":
       response = model.generate_content([input,image])
    else:
       response = model.generate_content(image)
    return response.text

##initialize our streamlit app

st.set_page_config(page_title=" Image CREATION ")

st.header("Gemini AI IMAGE APP")
input=st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit=st.button("Explain me about the image")

## If ask button is clicked

if submit:
    
    response=get_gemini_response(input,image)
    st.session_state['chat_history'].append(("You", input))
    st.subheader("The Response is")
    st.session_state['chat_history'].append(("Bot", response))
    st.write(response)


st.subheader("The Chat History is")
    
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")