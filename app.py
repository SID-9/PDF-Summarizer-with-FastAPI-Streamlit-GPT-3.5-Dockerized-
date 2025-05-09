import streamlit as st 
import requests 

backend_url= "http://localhost:8000"

st.title("PDF summarizer")

uploaded_file = st.file_uploader("Upload a pdf file : ",type=["pdf"])

if uploaded_file:
    api_key = st.text_input("Enter your open ai api key : ",type="password")
    
    if api_key:
        st.session_state.api_key = api_key

    if st.button("read pdf"):
        files = {"file":(uploaded_file.name,uploaded_file,"application/pdf")}
        
        response = requests.post(f"{backend_url}/pdf-file",files = files)
        
        if response.status_code == 200:
        
            result = response.json()
        
            content = result['contents']
            if content:
                st.session_state.content = content
                
                st.success(f"file uploaded is : {result['filename']}")
                
                response2 = requests.post(
                    f"{backend_url}/ask-gpt",
                    json={
                        'content':st.session_state.content,
                        'api_key': st.session_state.api_key
                    }
                )
                
                if response2.status_code == 200:
                    result2 = response2.json()
                    
                    st.subheader("summarized content")
                    st.write(result2['answer'])
                else:
                    st.error("error from gpt api")
            else:
                st.error("No content found in pdf")
        else:
            st.error("cant connect to backend")
       
        
        
