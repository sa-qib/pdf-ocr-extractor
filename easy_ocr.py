import easyocr
import numpy as np
from pathlib import Path
from pdf2image import convert_from_path
import warnings

warnings.filterwarnings("ignore", message=".*pin_memory.*")

# --- CONFIG ---
CHUNK_SIZE = 20   # number of pages per chunk
INPUT_DIR = Path("./surahs")
OUTPUT_DIR = Path("./output")


def init_reader():
    """Initialize EasyOCR with Arabic language"""
    return easyocr.Reader(['ar'])


def convert_pdf_to_images(file):
    """Convert a PDF file into a list of page images"""
    return convert_from_path(file, dpi=300)


def process_chunk(reader, pages, start, end):
    """OCR a chunk of PDF pages and return extracted text"""
    text_output = []
    for page in pages[start:end]:
        page_np = np.array(page)  # PIL.Image -> numpy array
        result = reader.readtext(page_np, detail=0, paragraph=True)
        text_output.extend(result)
    return text_output


def save_text(output_file, text_output):
    """Append extracted text to the output file"""
    with open(output_file, "a", encoding="utf-8") as f:
        f.write("\n".join(text_output) + "\n")


def process_pdf(reader, file):
    """Process a single PDF file"""
    output_file = OUTPUT_DIR / f"{file.stem}.txt"

    # Skip if already processed
    if output_file.exists():
        print(f"⏩ Skipping {file.name}, already processed.")
        return

    print(f"Processing {file.name} ...")

    # Convert PDF -> images
    pages = convert_pdf_to_images(file)
    total_pages = len(pages)
    print(f"Total pages: {total_pages}")

    # Process in chunks
    for start in range(0, total_pages, CHUNK_SIZE):
        end = min(start + CHUNK_SIZE, total_pages)
        print(f"  -> Processing pages {start+1} to {end} ...")

        text_output = process_chunk(reader, pages, start, end)
        save_text(output_file, text_output)

    print(f"✅ Finished {file.name}, saved to {output_file}")


def main():
    """Main function to process all PDFs in the input folder"""
    reader = init_reader()
    OUTPUT_DIR.mkdir(exist_ok=True)

    for file in INPUT_DIR.glob("*.pdf"):
        process_pdf(reader, file)


if __name__ == "__main__":
    main()
