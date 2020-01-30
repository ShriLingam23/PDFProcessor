import os
from PyPDF2 import PdfFileReader, PdfFileWriter

def pdf_splitter(path):
    fname = os.path.splitext(os.path.basename(path))[0]
    pdf = PdfFileReader(path)

    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))

        #output file name
        output_filename = 'D:/Practice/Python/PdfReader/sourcefiles/splittedfiles/{}_page_{}.pdf'.format(fname,page+1)

        #create and add page to new pdf
        with open(output_filename,'wb') as fh:
            pdf_writer.write(fh)

        print(f'Created: {output_filename}')

if __name__ == "__main__":
    path = 'D:/Practice/Python/PdfReader/sourcefiles/merged_file.pdf'
    pdf_splitter(path)
