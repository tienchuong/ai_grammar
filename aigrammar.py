# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 09:59:10 2022

@author: ChuongNT
"""


import streamlit as st
import openai

openai.api_key = st.secrets["key"]


@st.cache
def AI_grammar(yourcommand):
  response = openai.Completion.create(
    model="text-davinci-002",
    prompt=yourcommand,
    temperature=0,
    max_tokens=50,
    top_p=1.0,
    frequency_penalty=0.2,
    presence_penalty=0.0
  )
  return response["choices"][0].text

# Add a title and intro text
st.title('Nguyen Tien Chuong _ AI grammar')
yourcommand = st.text_input("Correct this to standard English: \n \n She no went to school")

    
form = st.form(key="my_form")
submit1 = form.form_submit_button(label="AI correct")
if submit1:
    # make prediction from the input text
    result = AI_grammar(yourcommand)
 
    # Display results of the NLP task
    st.header("Results")
    st.write(result)
    
yourcommand2 = st.text_input("test")
submit2 = form.form_submit_button(label="AI correct2")
if submit2:
    # make prediction from the input text
    result2 = AI_grammar(yourcommand2)
 
    # Display results of the NLP task
    st.header("Results2")
    st.write(result2)
