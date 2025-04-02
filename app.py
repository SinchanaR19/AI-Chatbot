import os
import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

# Load API Key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize Chat Model
llm = ChatOpenAI(api_key=api_key, model_name="gpt-4")

st.title("💬 AI Chatbot with LLM Integration")
st.write("Chat with the AI! Ask anything!")

# Chat History Management
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display Previous Messages
for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).write(msg["content"])

# Chat Input
user_input = st.chat_input("Say something...")

if user_input:
    st.session_state["messages"].append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    # AI Response
    response = llm([HumanMessage(content=user_input)])
    bot_response = response.content
    st.session_state["messages"].append({"role": "assistant", "content": bot_response})
    st.chat_message("assistant").write(bot_response)