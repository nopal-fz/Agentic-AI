import streamlit as st
import tempfile
from pathlib import Path
from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.tools.duckduckgo import DuckDuckGoTools
import time

# page config
st.set_page_config(
    page_title="Agentic Video Summarizer",
    page_icon="🧠",
    layout="centered"
)

st.markdown(
    """
    <div style="text-align: center;">
        <h1>Agentic Video Summarizer 📽️🧠</h1>
        <h2>Summarize any video with Agentic AI!</h2>
    </div>
    """,
    unsafe_allow_html=True
)

@st.cache_resource
def initialize_agent():
    return Agent(
        model=Ollama(id="mistral"),
        name="Video AI Summarizer",
        tools=[DuckDuckGoTools()],
        markdown=True
    )

multimodal_agent = initialize_agent()

video_file = st.file_uploader(
    "Upload a video file", type=["mp4", "mov", "avi"], help="Upload a video file to summarize"
)

if video_file:
    with tempfile.NamedTemporaryFile(delete=False) as temp:
        temp.write(video_file.read())
        video_path = Path(temp.name)

    st.video(video_path, start_time=0)

    user_query = st.text_area(
        "What insight are you seeking from this video?",
        placeholder="Enter a question or topic to summarize the video.",
        help="Provide specific questions or topics to generate a more accurate summary."
    )

    if st.button("🔍 Summarize Video"):
        if not user_query:
            st.warning("Please provide a question or topic to summarize the video.")
        else:
            try:
                with st.spinner("Processing video summary..."):
                    time.sleep(2) 

                    analysis_prompt = (
                        f"""
                        Analyze the uploaded video for content and context.
                        Respond to the following query using video insights and supplementary web research:
                        "{user_query}"
                        
                        Provide a detailed, user-friendly, and informative summary of the video content.
                        """
                    )

                    response = multimodal_agent.run(analysis_prompt)

                st.subheader("Summary Results 📝")
                st.markdown(response.content)

            except Exception as e:
                st.error(f"An error occurred: {e}")
            finally:
                Path(video_path).unlink(missing_ok=True)
else:
    st.info("Upload a video file to get started!")
