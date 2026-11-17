
import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

# Load environment variables from .env
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI Study Notes Summarizer",
    page_icon="📚",
    layout="centered"
)

# App heading
st.title("📚 AI Study Notes Summarizer")
st.write(
    "Turn long study notes into clear summaries, key points, "
    "and quick revision questions using the Gemini API."
)

st.divider()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error(
        "Gemini API key not found. Add GEMINI_API_KEY "
        "to your .env file and restart the app."
    )
    st.stop()

# Initialize Gemini client
try:
    client = genai.Client(api_key=api_key)
except Exception:
    st.error("Could not initialize the Gemini API client.")
    st.stop()

# User input
st.subheader("📝 Enter Your Study Notes")

notes = st.text_area(
    "Paste your study notes here:",
    height=250,
    placeholder="Example: Photosynthesis is the process by which green plants..."
)

# Summary detail
level = st.selectbox(
    "Choose summary detail:",
    ["Short", "Medium", "Detailed"]
)

# Generate summary
if st.button("✨ Summarize Notes", type="primary", use_container_width=True):

    if not notes.strip():
        st.warning("Please enter your study notes first.")

    else:
        prompt = f"""
You are a helpful and accurate study assistant.

Use the supplied notes to create a {level.lower()} study guide.

Include these sections:

1. SUMMARY
Explain the main ideas clearly.

2. KEY POINTS
List the most important information in bullet points.

3. IMPORTANT TERMS
Explain important terms and their meanings.

4. REVISION QUESTIONS
Create five short questions with answers based on the notes.

Use simple, student-friendly language.
Do not invent facts that are not supported by the notes.
If information is missing or unclear, mention that.

STUDY NOTES:
{notes}
"""

        try:
            with st.spinner("Generating your study guide..."):

                response = client.models.generate_content(
                    model="gemini-3.8-flash",
                    contents=prompt
                )

            if response.text:
                st.success("Your study guide is ready!")

                st.divider()
                st.subheader("📖 Your Study Guide")
                st.markdown(response.text)

                st.caption(
                    "Review important facts against your textbook "
                    "or class materials."
                )

            else:
                st.warning(
                    "The AI returned an empty response. Please try again."
                )

        except Exception as error:
            error_message = str(error)

            if "503" in error_message or "UNAVAILABLE" in error_message:
                st.error(
                    "The Gemini service is temporarily busy. "
                    "Please wait a little and try again."
                )

            elif "429" in error_message or "RESOURCE_EXHAUSTED" in error_message:
                st.error(
                    "The API request limit may have been reached. "
                    "Please wait before trying again."
                )

            elif "401" in error_message or "403" in error_message:
                st.error(
                    "There may be a problem with your API key or its permissions. "
                    "Check your local .env file."
                )

            else:
                st.error(
                    "Something went wrong while generating your study guide."
                )

            with st.expander("Technical details"):
                st.code(error_message)

st.divider()

# Footer
st.caption(
    "SWYNEX Task 2 Prototype | Python • Streamlit • Gemini API"
)
