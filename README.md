# PDF OCR Extractor

Extract text from scanned PDF files using OCR (Optical Character Recognition). This script is designed to handle multi-page PDFs efficiently and can be reused for any scanned PDF documents, including Arabic text.

---

## Features

- Extract text from **scanned PDFs** using OCR.
- Handles **multi-page PDFs** in chunks for better performance.
- Saves extracted text into `.txt` files.
- Easily adaptable for **any language** (requires EasyOCR language support).
- Batch processing of PDFs from a folder.

---

## Requirements

Python packages:
`easyocr>=1.6
numpy>=1.24
pdf2image>=1.16
Pillow>=10.0
`


**System dependency:**  
- **Poppler** (required by `pdf2image`)  
  - Windows: [Download binaries and add to PATH](http://blog.alivate.com.au/poppler-windows/)  
  - Mac: `brew install poppler`  
  - Linux (Debian/Ubuntu): `sudo apt install poppler-utils`

---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/pdf-ocr-extractor.git
cd pdf-ocr-extractor
```
2. Create a virtual environment and activate it:
```
python -m venv venv
source venv/bin/activate    # Mac/Linux
venv\Scripts\activate       # Windows
```
3. Install dependencies:
```
pip install -r requirements.txt
```

### Usage

1. Place your PDF files in the surahs/ directory (or any folder you configure in the script).
2. Run the script:
```
python main.py
```

3. Extracted text will be saved in the output/ directory with the same name as the PDF file.
Notes on Arabic PDFs:

  - The script was originally used to extract text from scanned Arabic Quranic PDFs (surahs).
  - EasyOCR is initialized with Arabic support (easyocr.Reader(['ar'])) for accurate recognition.
  - The script can easily be adapted for other languages by changing the EasyOCR language parameter.


### Configuration:

`CHUNK_SIZE`: Number of pages processed per chunk. Adjust for memory/performance.
`INPUT_DIR`: Folder containing PDFs.
`OUTPUT_DIR`: Folder where extracted text files are saved.

### License:

This project is open-source and free to use.


### Example Output

For a PDF example.pdf in surahs/, after running the script:
```
output/example.txt
```
contains the extracted text in the same order as the scanned pages.


###
Made with ❤️ by [Abdullah](https://github.com/sa-qib)  
