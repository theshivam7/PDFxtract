<div align="center">

# PDFxtract

[![Try PDFxtract](https://img.shields.io/badge/Try-PDFxtract-brightgreen?style=for-the-badge&logo=streamlit)](https://pdfxtractor.streamlit.app/)

**Textbook Content Extractor**
</div>

## Overview
PDFxtract is a powerful tool designed to extract and categorize content from PDF textbooks. It separates questions from other content, making it easier for students and educators to study and analyze textbook material.

Try PDFxtract here: [PDFxtract Tool](https://pdfxtractor.streamlit.app/)

## Features

- Extract text content from PDF files
- Automatically separate questions from other content
- User-friendly web interface built with Streamlit
- Download extracted content as text files

### Prerequisites

Make sure you have the following installed:

- Python 3.7 or higher
- `pip` (Python package installer)

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/theshivam7/PDFxtract.git

2. **Navigate to the project directory**:
    ```bash
    cd PDFxtract

    ```
3. Create a virtual environment and activate it:

```bash
python3 -m venv venv
```

4. Activate the virtual environment:
- On Windows:
  ```bash
  venv\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```
5: Install the Required Dependencies

Install the dependencies listed in the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

6. **Create a `.env` file** in the root of your project and add your API key for the translation service.

    ```env
    OPENAI_API_KEY=your_openai_api_key
    ```

## Usage

1. Run the Streamlit app:
   ```
   streamlit run ui.py
   ```

2. Open your web browser and go to the URL provided by Streamlit (usually `http://localhost:8501`).

3. Upload a PDF file using the file uploader.

4. Click on "Extract Content" to process the PDF.

5. Once processing is complete, use the download buttons to get your extracted content.



## Acknowledgments

- [Streamlit](https://streamlit.io/) for the excellent web app framework
- [PyPDF2](https://pypdf2.readthedocs.io/) for PDF processing
- [OpenAI](https://openai.com/) for the powerful language model

## About the Developer
I'm [**Shivam Sharma**](https://www.linkedin.com/in/theshivam7/), an undergrad at IIT Madras. I develop websites and apps for Android and iOS, and I'm passionate about AI and ML.

## Contact Me

If you have any questions, feel free to reach out on LinkedIn or check out my GitHub for interesting projects:

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/theshivam7/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=flat-square&logo=github&logoColor=white)](https://www.github.com/theshivam7/)
---

## 🤝 Contributors

We welcome contributions! Feel free to submit pull requests or open issues.

---

<div align="center">
  
[![Made with ❤️ by Shivam](https://img.shields.io/badge/Made%20with%20%E2%9D%A4%EF%B8%8F%20by-Shivam-red?style=for-the-badge)](https://github.com/theshivam7)

</div>