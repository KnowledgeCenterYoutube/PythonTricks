
import pyttsx3
import PyPDF2

book = open('test.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
speaker = pyttsx3.init()

for num in range(1, pages):
    page = pdfReader.getPage(num)
    txt = page.extractText()
    speaker.say(txt)
    speaker.runAndWait()
    
    
