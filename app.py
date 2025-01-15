import streamlit as st
from PyPDF2 import PdfReader
from docx import Document
import io

st.title("PDF To WORD Converter")
st.write("Upload Your PDF File Here:")

# File uploader for PDF files
uploaded_file = st.file_uploader(" ", type="pdf")

if uploaded_file is not None:
    pdf = PdfReader(uploaded_file)  # Initialize PdfReader with the uploaded file
    st.write("PDF Uploaded Successfully")
    st.write(f"Number of Pages: {len(pdf.pages)}")

    # Create a Word document
    doc = Document()

    # Extract text from each page and add it to the Word document
    for page_num in range(len(pdf.pages)):
        page = pdf.pages[page_num]
        text = page.extract_text()
        doc.add_paragraph(text)

    # Save the Word document to an in-memory buffer
    word_io = io.BytesIO()
    doc.save(word_io)
    word_io.seek(0)

    # Provide a download button for the Word file
    st.download_button(
        label="Download the Converted File:",
        data=word_io,
        file_name="converted-file.docx",
    )
else:
    st.write("Please upload a PDF file to convert.")
