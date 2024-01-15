import streamlit as st
import pandas as pd
from pandasai import SmartDatalake
from pandasai.llm import HuggingFaceTextGen

# Below is your plaground example CSVs
employees_data = {
    'EmployeeID': [1, 2, 3, 4, 5],
    'Name': ['John', 'Emma', 'Liam', 'Olivia', 'William'],
    'Department': ['HR', 'Sales', 'IT', 'Marketing', 'Finance']
}

salaries_data = {
    'EmployeeID': [1, 2, 3, 4, 5],
    'Salary': [5000, 6000, 4500, 7000, 5500]
}

employees_df = pd.DataFrame(employees_data)
salaries_df = pd.DataFrame(salaries_data)

# Now setup the Streamlit App
st.set_page_config(
    page_title="Demo",
    page_icon=":sales:",
    layout="wide",
    )

st.header("Simple Demo Chatbot")
user_question = st.text_input("Ask me a question about your data.")

# Bring up your LLM
llm = HuggingFaceTextGen(inference_server_url="http://127.0.0.1:8080", max_new_tokens=1024)

sdl = SmartDatalake([employees_df, salaries_df], config={
    "llm": llm,
    "verbose":False, 
    "enable_cache": True, 
    "enforce_privacy": True, 
    "save_logs": False,})

# Make your streamlit look a little bit nicer
st.empty()
st.divider()
st.table(data=salaries_df)
st.divider()
st.table(data=employees_data)
st.divider()

# Glue things together
if user_question is not None and user_question != "":
    output = sdl.chat(user_question)
    st.write(output)
