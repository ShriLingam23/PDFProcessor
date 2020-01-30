import glob
from PyPDF2 import PdfFileWriter, PdfFileReader

def merger(output_path, input_path):

    pdf_writer = PdfFileWriter()
    
    # loop through each pdf in path
    for path in input_path :
        pdf_reader = PdfFileReader(path)

        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))

            with open(output_path , 'wb') as fh:
                pdf_writer.write(fh)


if __name__ == "__main__":
    paths = glob.glob('D:/Practice/Python/PdfReader/sourcefiles/*.pdf')
    paths.sort()

    merger('D:/Practice/Python/PdfReader/sourcefiles/merged_file.pdf',paths)