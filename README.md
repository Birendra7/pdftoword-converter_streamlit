
# PDF to Word Converter

This is a Streamlit-based web application that allows users to upload a PDF file and convert it into a Word document. The converted file can then be downloaded for further use.

## Features

- **PDF Upload**: Upload your PDF file directly through the web interface.
- **Text Extraction**: Extracts text from each page of the uploaded PDF.
- **Word Document Creation**: Converts the extracted text into a Word document.
- **Download Option**: Provides an option to download the converted Word document.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Set Up a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv env
   source env/bin/activate  # On macOS/Linux
   .\env\Scripts\activate   # On Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   If `requirements.txt` is not available, manually install the required libraries:
   ```bash
   pip install streamlit PyPDF2 python-docx
   ```

## Usage

1. Run the application:
   ```bash
   streamlit run app.py
   ```

2. Open your browser and navigate to:
   ```
   http://localhost:8501
   ```

3. Upload a PDF file using the provided uploader.

4. View the number of pages in the PDF.

5. Click the **Download the Converted File** button to download the Word document.

## File Structure

```
project-directory/
├── app.py                # Main Streamlit application script
├── requirements.txt      # List of dependencies
├── README.md             # Project documentation
└── env/                  # Virtual environment folder (optional)
```

## Requirements

- Python 3.7 or higher
- Libraries:
  - Streamlit
  - PyPDF2
  - python-docx

## Notes

- The app extracts text from PDFs and might not fully preserve formatting or images.
- Ensure the uploaded PDF has selectable text for best results.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! Feel free to fork this repository and submit pull requests.

## Contact

For any issues or suggestions, please reach out via [email@example.com].
```

Replace `<repository-url>`, `<repository-folder>`, and `[email@example.com]` with appropriate values for your project. Let me know if you'd like to refine it further!
