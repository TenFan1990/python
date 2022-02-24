# importing required modules
from pdfminer.high_level import extract_text
from pdfminer.high_level import extract_pages

def parseText(schedule):
    for line in schedule.splitlines():
        if not line:
            continue
        print("Line" + line)

pathToPdf = 'C:\\temp\\Meetings Schedule.pdf'

page_no = 0
for page_layout in extract_pages(pathToPdf):
    parseText(extract_text(pathToPdf, page_numbers=[page_no]))
    page_no += 1