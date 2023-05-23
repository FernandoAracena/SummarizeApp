# helpers.py
import docx2txt
from PyPDF2 import PdfReader
from googletrans import Translator

def extract_text(file_path):
    text = ''
    if file_path.endswith('.docx'):
        text = docx2txt.process(file_path)
    elif file_path.endswith('.pdf'):
        with open(file_path, 'rb') as f:
            pdf_reader = PdfReader(f)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()
    elif file_path.endswith('.txt'):
        with open(file_path, 'r') as f:
            text = f.read()
    return text

def translate_text(text):
    translator = Translator()
    translation = translator.translate(text, src='en', dest='no')
    if translation is not None and hasattr(translation, 'text'):
        translated_text = translation.text
        return translated_text
    else:
        raise AttributeError("Unable to translate the summary.")
