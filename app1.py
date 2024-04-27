##Conversational Q&A Chatbot

import streamlit as st
from langchain.schema import HumanMessage,SystemMessage,AIMessage
from langchain.chat_models import ChatOpenAI
import os


##Streamlit UI
st.set_page_config(page_title="Conversational Q&A Chatbot")
st.header("Hey!! lets do code")

from dotenv import load_dotenv
load_dotenv()



chat = ChatOpenAI(temperature=0.6,openai_api_key=os.getenv('OPEN_API_KEY'))

if 'flowmesages' not in st.session_state:
    st.session_state['flowmessages']=[
        SystemMessage(content="you are a comedian AI assistent")
    ]

##function to load OpenAI model and get responses

def get_chatmodel_response(question):
    
    st.session_state['flowmessages'].append(HumanMessage(content=question))
    answer=chat(st.session_state['flowmessages'])   
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))
    
    return answer.content



input = st.text_input("Input: ",key= "input")
submit= st.button("Ask a question")


if submit:
    response = get_chatmodel_response(input)
    st.subheader("The response is")
    st.write(response)








