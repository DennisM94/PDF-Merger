from PyPDF2 import PdfFileReader, PdfFileMerger, PdfFileWriter
import os

def get_meta(path):
    with open(path, "rb") as f:
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
        nop = pdf.getNumPages()

    print(info)
    print(nop)

def extract_text(path):
    with open(path, "rb") as f:
        pdf = PdfFileReader(f)
        page_one = pdf.getPage(1)
        print(page_one)
        print(type(page_one))
        text = page_one.extractText()
        print(text)

def split_pdf(path):
    with open(path, "rb") as f:
        pdf = PdfFileReader(f)
        for page in range(pdf.getNumPages()):
            writer = PdfFileWriter()
            writer.addPage(pdf.getPage(page))
            with open(f"{page}.pdf", "wb") as f_out:
                writer.write(f_out)

def merge_pdf(input_path, output_path):
    writer = PdfFileWriter()
    for i in input_path:
        pdf_reader = PdfFileReader(i)
        for page in range(pdf_reader.getNumPages()):
            writer.addPage(pdf_reader.getPage(page))
    with open(output_path, "wb") as f_out:
        writer.write(f_out)

def lazy_merge(input_path, output_path):
    pdf_merger = PdfFileMerger()
    for i in input_path:
        pdf_merger.append(i)
    with open(output_path, "wb") as f_out:
        pdf_merger.write(f_out)

if __name__ == "__main__":
    path = r"C:\Users\you-p\Documents\____Coding\Python\PyCharm\PDF-Merger\PDF\VVorlesung_01(1).pdf"
    dir = "C:/Users/you-p/Documents/____Coding/Python/PyCharm/PDF-Merger/PDF"
    file_list = []
    for file in os.listdir(dir):
        file_list.append("PDF/" +file)

    merge_pdf(file_list, "out.pdf")

