import streamlit as st
import google.generativeai as genai
import os

# Load API Key securely
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Initialize Gemini model
model = genai.GenerativeModel('gemini-2.0-flash')

st.set_page_config(page_title="MindMirror - AI Therapy", layout="centered")

st.title("🧠 MindMirror: AI-Powered Emotional Support")
st.markdown("Write how you're feeling or share your story, and let the AI help you reflect 💬")
st.markdown('<p style="font-size: 5pt";>By submitting, you agree that your anonymized input may be saved for analysis or research.<p>', unsafe_allow_html=True)

user_input = st.text_area("Your thoughts today...", height=200)

if st.button("Analyze My Emotions") and user_input:
    with st.spinner("Analyzing..."):
        prompt = f"""
        You are a friendly world best therapist. The user has written: "{user_input}"
        1. Detect the emotional tone (anxious, sad, happy, angry, etc.)
        analyze his story (if he shared a story)
        2. Suggest what might be causing it
        3. Provide comforting, practical advice or coping tips
        4. Ask one deep question to help them reflect
        give like a paragraph not like point wise question answer 
        """
        response = model.generate_content(prompt)
        st.markdown("### 🧠 Emotional Insight:")
        st.write(response.text)
