import streamlit as st
from PIL import Image
import pytesseract
import json
import os

# Function to perform OCR
def extract_text(image):
    """Extract text from image using Tesseract."""
    text = pytesseract.image_to_string(image, lang='eng+hin')
    return text

# Function to search for keywords
def search_keywords(text, keyword):
    """Search for keywords in the extracted text."""
    lines = text.split('\n')
    matches = [line for line in lines if keyword.lower() in line.lower()]
    return matches

# Streamlit application
st.title("OCR Text Extraction and Keyword Search")

# Upload image
uploaded_file = st.file_uploader("Upload an image (JPEG, PNG)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Perform OCR
    extracted_text = extract_text(image)
    st.subheader("Extracted Text:")
    st.write(extracted_text)

    # Keyword search
    keyword = st.text_input("Enter keyword to search:")
    
    if keyword:
        results = search_keywords(extracted_text, keyword)
        st.subheader("Search Results:")
        if results:
            for result in results:
                st.write(f"• {result}")
        else:
            st.write("No matches found.")
