📈 Stock Price Predictor

A lightweight Streamlit application that uses LangChain and Groq’s LLMs to generate long-term stock price trend predictions based on any company name or description provided by the user.

🚀 Features

LLM-powered financial analysis using Groq’s fast inference API

Simple Streamlit UI for user input and result display

Custom prompt engineering for finance-focused forecasting

Predicts 5–10 year stock price trends

Easy to deploy locally or on cloud platforms

🧠 How It Works

The user enters a company name or business description.

A custom LangChain PromptTemplate converts the input into a structured financial-analysis request.

The prompt is passed to Groq’s GPT-OSS-120B model using the ChatGroq client.

The model returns a text-based analytical forecast, which is shown directly in the Streamlit app.
ChatGroq – Handles communication with the Groq LLM

PromptTemplate – Structures the financial prediction prompt

StrOutputParser – Cleans and formats the model's output

Streamlit UI – Text area for user input and prediction display
