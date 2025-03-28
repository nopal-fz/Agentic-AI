# Agentic Video Summarizer 📽️🧠

Agentic Video Summarizer is a Streamlit-based application that allows users to upload videos and receive AI-generated summaries with the help of an intelligent agent.

## 🚀 Features
- 📂 **Upload Videos**: Supports `.mp4`, `.mov`, and `.avi` formats.
- 🤖 **AI Agent**: Uses **Mistral (Ollama)** to analyze and summarize video content.
- 🔎 **External Search**: Utilizes **DuckDuckGoTools** to enhance insights with additional web research.
- 📝 **Contextual Summarization**: Answers user queries based on the uploaded video content.

## 🛠️ Installation
Ensure you have **Python 3.8+** and **pip** installed on your system.

```sh
# Clone repository
git clone https://github.com/username/agentic-video-summarizer.git
cd agentic-video-summarizer

# Create a virtual environment
python -m venv env
source env/bin/activate  # For macOS/Linux
env\Scripts\activate    # For Windows

# Install dependencies
pip install -r requirements.txt
```

## 🎬 Usage
Run the application with the following command:

```sh
streamlit run agentic.py
```

Then, open your browser and access `http://localhost:8501/`.

## 📦 Dependencies
- `streamlit`
- `agno`
- `ollama`
- `duckduckgo_search`
- `pathlib`

Ensure all dependencies are installed using:
```sh
pip install -r requirements.txt
```

## 🛠️ AI Agent Configuration
This application uses `agno.Agent` with the **Mistral** model from Ollama:
```python
multimodal_agent = Agent(
    model=Ollama(id="mistral"),
    name="Video AI Summarizer",
    tools=[DuckDuckGoTools()],
    markdown=True
)
```
The agent analyzes videos and provides informative summaries, incorporating additional research if needed.

## 🛠️ Project Structure
```
agentic-video-summarizer/
│── agentic.py             # Main Streamlit app
│── requirements.txt   # Dependencies
│── README.md          # Documentation
```

## 📜 License
This project is licensed under the **MIT License**. You are free to use and modify this project as needed.

---
**Made with ❤️ by [Naufal Faiz N]**
