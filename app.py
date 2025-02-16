
import streamlit as st
import nltk
from transformers import pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


chatbot = pipeline("text-generation", model="distilgpt2")

def healthcare_chatbot(user_input):
    if "symptoms" in user_input:
        return "Please consult a Doctor for accurate advice"
    elif "appointment" in user_input:
        return "would you like to schedule an appointment with the doctor"
    elif "medication" in user_input:
        return "it's a important to take prescribe medicines regulary. If you have any concerns please consult a doctor "
    else:
        response = chatbot(user_input,max_length = 500, num_return_sequences=1)
    return response[0]['generated_text']
    
    
def main():
    st.set_page_config(page_title="Healthcare Chatbot", page_icon="💊")
    st.title("Healthcare Assistant Chatbot")
    user_input = st.text_input("How can I assist you today?")
    print(user_input)
    if st.button("submit"):
        if user_input:
            st.write("👩 user : ",user_input)
            with st.spinner("Processing your query,Please wait...."):
                response = healthcare_chatbot(user_input)
            st.write("🌸 Healthcare Assistant :",response)
            print(response)
        else:
            st.write("Please enter a message to get a response")
    

main()


