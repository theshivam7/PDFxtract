import streamlit as st
from app import process_pdf
import os

def main():
    st.set_page_config(page_title="PDFxtract", page_icon="📚", layout="wide")
    
    # Custom CSS for improved appearance and text visibility
    st.markdown("""
    <style>
    .main {
        padding: 2rem;
        border-radius: 0.5rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #4CAF50 !important;
        color: white !important;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border: none;
        border-radius: 4px;
        transition: background-color 0.3s;
    }
    .stButton>button:hover {
        background-color: #45a049 !important;
    }
    /* Ensure text color adapts to both light and dark modes */
    body {
        color: var(--text-color);
    }
    .stTextInput>div>div>input {
        color: var(--text-color);
    }
    .stMarkdown {
        color: var(--text-color);
    }
    /* Custom colors for success and info messages */
    .stSuccess {
        background-color: #4CAF50 !important;
        color: white !important;
    }
    .stInfo {
        background-color: #2196F3 !important;
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.title("📚 PDFxtract: Textbook Content Extractor")
    st.markdown("---")

    # Main content area
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("Upload your PDF")
        uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

        if uploaded_file is not None:
            st.success(f"File uploaded: {uploaded_file.name}")
            
            if st.button("Extract Content", key="extract_button"):
                with st.spinner("Processing PDF... This may take a few moments."):
                    questions_file, content_file = process_pdf(uploaded_file)
                
                if questions_file and content_file:
                    st.session_state.processed = True
                    st.session_state.questions_file = questions_file
                    st.session_state.content_file = content_file
                    st.success("Extraction complete!")
                else:
                    st.error("An error occurred during processing. Please try again.")

    with col2:
        st.subheader("Download Extracted Content")
        if 'processed' in st.session_state and st.session_state.processed:
            with open(st.session_state.questions_file, "rb") as file:
                st.download_button(
                    label="Download Questions",
                    data=file,
                    file_name=os.path.basename(st.session_state.questions_file),
                    mime="text/plain",
                    key="download_questions"
                )
            
            with open(st.session_state.content_file, "rb") as file:
                st.download_button(
                    label="Download Other Content",
                    data=file,
                    file_name=os.path.basename(st.session_state.content_file),
                    mime="text/plain",
                    key="download_content"
                )
        else:
            st.info("Upload and process a PDF to see download options.")

    # Instructions
    st.markdown("---")
    st.subheader("How to use PDFxtract")
    st.markdown("""
    1. Upload your PDF textbook using the file uploader.
    2. Click on "Extract Content" to process the PDF.
    3. Once processing is complete, use the download buttons to get your extracted content.
    4. To process another file, simply upload a new PDF and click "Extract Content" again.
    """)

if __name__ == "__main__":
    main()