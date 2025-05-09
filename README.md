# PDF-Summarizer-with-FastAPI-Streamlit-GPT-3.5-Dockerized-
An AI-powered full-stack web app that extracts text from PDF files and generates concise summaries using OpenAI's GPT-3.5 model. Built with FastAPI as the backend, Streamlit as the frontend, and Docker for seamless deployment.
________________________________________
# 🚀 Features
-	📄 Upload and extract text from PDF documents
-	✨ Automatically cleans and structures extracted text
-	🧠 Sends text to OpenAI’s GPT-3.5 for intelligent summarization
-	⚡ Responsive and clean Streamlit interface
-	🔁 Uses st.session_state for persistent UI interaction
-	🌐 Enables frontend-backend communication via CORS
-	🐳 Easily deployable with Docker

_______________________________________________

| Layer            | Technology       |
| ---------------- | ---------------- |
| Frontend         | Streamlit        |
| Backend          | FastAPI          |
| AI Model         | OpenAI GPT-3.5   |
| PDF Parser       | PyMuPDF (`fitz`) |
| HTTP Client      | `requests`       |
| CORS Support     | `CORSMiddleware` |
| Containerization | Docker           |

________________________________________
# 🔧 Local Setup (Without Docker)
1. Clone the repo
git clone https://github.com/your-username/pdf-summarizer-fastapi.git
cd pdf-summarizer-fastapi
3. Create a virtual environment

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
4. Install dependencies

pip install -r requirements.txt
5. Start the backend and frontend

## Terminal 1
uvicorn main:app --reload
______________________________________
# 🔐 OpenAI Key Required
-	This app uses the OpenAI GPT-3.5 API.
-	You’ll be prompted to paste your OpenAI API key in the UI.
-	Get your API key here: https://platform.openai.com/account/api-keys
________________________________________
# 📌 Flow Summary
1.	Upload a PDF
2.	FastAPI extracts and cleans the full text
3.	Text is sent to GPT with a summarization prompt
4.	Streamlit UI shows the returned summary



## Terminal 2
streamlit run app.py
•	FastAPI docs at: http://localhost:8000/docs
•	Streamlit app at: http://localhost:8501


