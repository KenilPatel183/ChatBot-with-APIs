from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

## Langsmith Tracking
os.environ["LANGCHAIN_TRCING_V2"] = "true"

groq_api_key = os.getenv("GROQ_API_KEY")
langchain_api_key = os.getenv("LANGCHAIN_API_KEY")

if not groq_api_key:
    raise ValueError("GROQ_API_KEY is not set in the .env file or environment variables.")
if not langchain_api_key:
    raise ValueError("LANGCHAIN_API_KEY is not set in the .env file or environment variables.")

os.environ["GROQ_API_KEY"] = groq_api_key
os.environ["LANGCHAIN_API_KEY"] = langchain_api_key   

## prompt template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system" ,"You are a helpfull assistant. Please response to the use queries"),
        ("user" ,"Question = {question}")
    ]
)

## Streamlit Framwork


st.title('Langchain demo with Groq api')
input_text = st.text_input("Search with topic you want")

## Groq LLM

llm = ChatGroq(model = "llama-3.3-70b-versatile")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))