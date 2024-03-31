from langchain.llms import openai
from dotenv import load_dotenv
from langchain import HuggingFaceHub
import streamlit as st
import os

load_dotenv()

""

def get_hugging_response(question):
    llm = HuggingFaceHub(repo_id="google/flan-t5-large",model_kwargs={"temperature":0.5})
    response=llm(question)
    return response


## Initialise our streamlit app
    
st.set_page_config(page_title="Q&A Demo")

st.header("Lanchain Application")

input = st.text_input("Enter the Question")


submit = st.button("Ask the quesion")

if submit:
    response = get_hugging_response(input)
    st.subheader("The Response:")
    st.write(response)