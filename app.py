# an app that will take a pdf and read it and convert the text to an mp3 file

import os
import pyttsx3
from PyPDF2 import PdfReader

# set input and output directories
input_dir = 'input'
output_dir = 'output'

# get list of pdf files in input directory
pdf_files = [f for f in os.listdir(input_dir) if f.endswith('.pdf')]

# initialize the speaker
speaker = pyttsx3.init()

# loop through each pdf file
for pdf_file in pdf_files:
    # open the pdf file
    book = open(os.path.join(input_dir, pdf_file), 'rb')
    pdfReader = PdfReader(book)
    print(f'Converting {pdf_file}...')

    # read the page
    text = ''
    for page in pdfReader.pages:
        text += page.extract_text()

    # create a separate output folder for each pdf file
    pdf_output_dir = os.path.join(output_dir, pdf_file[:-4])
    os.makedirs(pdf_output_dir, exist_ok=True)

    # save the audio
    speaker.save_to_file(text, os.path.join(pdf_output_dir, f'{pdf_file[:-4]}.mp3'))
    speaker.runAndWait()

    # save the transcript
    with open(os.path.join(pdf_output_dir, f'{pdf_file[:-4]}.txt'), 'w', encoding='utf-8') as transcript_file:
        transcript_file.write(text)

    # close the book
    book.close()

print('Conversion complete!')