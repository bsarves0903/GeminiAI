import streamlit as st
import os
import pathlib
import textwrap

from IPython.display import display
from IPython.display import Markdown

def to_markdown(text):
     text = text.replace('•', '  *')
     return Markdown(textwrap.indent(text,'>',predicate=lambda _:True))

os.environ['GEMINI_API_KEY'] = 'AIzaSyCfVF_sOMwGO31uxab5zoIAGBFJ0nm-EvE'

import google.generativeai as genai
genai.configure(api_key=os.environ['GEMINI_API_KEY'])

def get_gemini_response(question):
     model = genai.GenerativeModel('gemini-pro')
     response = model.generate_content(question)
     return response.text

st.set_page_config(page_title="Q&A Demo")

st.header("Gemini AI BOT Application")

input=st.text_input("Input: ",key="input")


submit=st.button("I can help on your question")

## If ask button is clicked

if submit:
     response = get_gemini_response(input)
     st.subheader("The Response is")
     st.write(response)

    

