from fastapi import FastAPI,status,UploadFile,File
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import fitz
from openai import OpenAI

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#reponse model
class FileReturn(BaseModel):
    filename:str
    contents:str
    
    
class AskGpt(BaseModel):
    content: str
    api_key:str
    
    
@app.post("/pdf-file",response_model=FileReturn,status_code=status.HTTP_200_OK)
async def pdf_file(file: UploadFile=File(...)):
    content = await file.read()
    
    doc = fitz.open(stream=content,filetype="pdf")
    
    all_text=""
    
    for page in doc:
        all_text += page.get_text()
    
    doc.close()
    
    return FileReturn(
        filename= file.filename,
        contents=all_text.strip()
    )

# gpt model config
@app.post("/ask-gpt")
def ask_gpt(data:AskGpt):
    
    prompt= f""" 
    You are a helpful assistant. 
    Summarize the content provided below in the shortest way possible.
    
    content:
    {data.content}
    
    Answer:
    """
    
    client = OpenAI(api_key=data.api_key)
    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages=[
            {"role":"user","content":prompt}
            
        ]
    )
    summary = response.choices[0].message.content
    return {"answer":summary}