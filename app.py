import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Get API Key
api_key = os.getenv("GEMINI_API_KEY")

# Check API Key
if not api_key:
    st.error("API Key not found! Check your .env file.")
    st.stop()

# Configure Gemini
genai.configure(api_key=api_key)

# Check API Key Loaded


# Load Gemini Model
model = genai.GenerativeModel("gemini-2.5-flash")

# App Title
st.title("AI SQL Query Generator")

# User Input
question = st.text_input("Ask your question")

# Button
if st.button("Generate SQL"):

    if question.strip() == "":
        st.warning("Please enter a question.")

    else:

        prompt = f"""
Convert the following English question into a MySQL query.

Question:
{question}

Return only the SQL query.
"""

        try:
            response = model.generate_content(prompt)

            st.subheader("Generated SQL")
            st.code(response.text, language="sql")

        except Exception as e:
            st.error(f"Error: {e}")