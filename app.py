import os
import PyPDF2
from dotenv import load_dotenv
from openai import OpenAI
import datetime

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY, base_url="https://api.perplexity.ai")

def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def split_content(text):
    prompt = f"""Split the following text into questions and other content (including titles, bullet points, poetry, author names, formulas, and paragraphs if applicable). 
    Ignore any watermarks, footers, year or version information, or title or section number.
    Format the output as follows:
    
    QUESTIONS:
    1. [First question]
    2. [Second question]
    ...
    
    OTHER CONTENT:
    [All other content, including titles, bullet points, poetry, author names, formulas, and paragraphs]
    
    Text: {text}
    """
    
    try:
        response = client.chat.completions.create(
            model="llama-3.1-70b-instruct",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that splits textbook content into questions and other text."},
                {"role": "user", "content": prompt}
            ],
            temperature=0
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error in API call: {str(e)}")
        return None

def save_output(questions, other_content, original_filename):
    try:
        # Create Output folder if it doesn't exist
        os.makedirs('Output/Questions', exist_ok=True)
        os.makedirs('Output/Content', exist_ok=True)

        # Generate a timestamp
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Create unique filenames
        questions_filename = f'Output/Questions/{original_filename}_{timestamp}_questions.txt'
        content_filename = f'Output/Content/{original_filename}_{timestamp}_content.txt'

        with open(questions_filename, 'w', encoding='utf-8') as f:
            f.write(questions)
        with open(content_filename, 'w', encoding='utf-8') as f:
            f.write(other_content)
        return questions_filename, content_filename
    except Exception as e:
        print(f"Error saving files: {str(e)}")
        return None, None

def process_pdf(file):
    try:
        text = extract_text_from_pdf(file)
        content = split_content(text)
        
        if content is None:
            return None, None

        # Split the content into questions and other content
        parts = content.split("OTHER CONTENT:")
        questions = parts[0].replace("QUESTIONS:", "").strip()
        other_content = parts[1].strip() if len(parts) > 1 else ""
        
        # Get the original filename without extension
        original_filename = os.path.splitext(file.name)[0]
        
        return save_output(questions, other_content, original_filename)
    except Exception as e:
        print(f"Error processing PDF: {str(e)}")
        return None, None