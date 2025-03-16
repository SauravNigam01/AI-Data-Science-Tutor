
import streamlit as st
import google.generativeai as genai

# Set API Key securely
GOOGLE_API_KEY = "ENTER_YOUR_API_KEY"  
if not GOOGLE_API_KEY:
    st.error("API Key is missing! Please set the GOOGLE_API_KEY environment variable.")
    st.stop()

genai.configure(api_key=GOOGLE_API_KEY)

# Function to get AI response
def get_gemini_response(prompt):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")  
        response = model.generate_content(prompt)
        return response.text if hasattr(response, "text") else "No response received."
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI
st.set_page_config(page_title="AI Data Science Tutor", layout="wide")
st.title("🤖 Your AI Data Science Tutor")


# User input
user_input = st.text_area("Ask a question in Data Science:", "")

if st.button("Tap") and user_input:
    with st.spinner("Collecting Information.."):
        response = get_gemini_response(user_input)
    st.success("Here is your answer")
    st.subheader("AI Tutor:")
    st.write(response)


