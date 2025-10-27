import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv

load_dotenv()

st.header("📈 Stock Price Predictor")

user_input = st.text_area("Enter the company name or details:")

if st.button("Submit") and user_input:
    # Initialize the model
    model = ChatGroq(
        model="openai/gpt-oss-120b",  # You can replace with another Groq-supported model
        api_key=os.getenv("GROQ_API_KEY")
    )

    # Create the prompt
    prompt = PromptTemplate(
        template=(
            "You are a finance expert who predicts stock prices.\n"
            "Given the company name or description: {user_input},\n"
            "predict the possible stock price trend over the next 5–10 years.\n"
            "Provide only your analytical forecast."
        ),
        input_variables=["user_input"]
    )

    # Create parser
    parser = StrOutputParser()

    # Chain everything together
    chain = prompt | model | parser

    # Run the chain
    response = chain.invoke({"user_input": user_input})

    # Display result
    st.subheader("Predicted Stock Price Trend:")
    st.write(response)
