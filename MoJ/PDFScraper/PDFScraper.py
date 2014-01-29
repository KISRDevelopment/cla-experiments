"""NONE OF THIS CRAP WORKS YET!!!"""

import sys
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice, TagExtractor
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.converter import PDFPageAggregator
from pdfminer.cmapdb import CMapDB
from pdfminer.layout import LAParams, LTTextBoxHorizontal
from pdfminer.image import ImageWriter

"""from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LAParams
import sys"""

# Open a PDF file.
fp = open(sys.argv[1], 'rb')
# Create a PDF parser object associated with the file object.
parser = PDFParser(fp)
# Create a PDF document object that stores the document structure.
document = PDFDocument(parser)
# Supply the password for initialization.
# (If no password is set, give an empty string.)
document.initialize('')
# Check if the document allows text extraction. If not, abort.
if not document.is_extractable:
    raise PDFTextExtractionNotAllowed
# Create a PDF resource manager object that stores shared resources.
rsrcmgr = PDFResourceManager()
# Set parameters for analysis.
laparams = LAParams()
# Create a PDF device object.
######device = PDFDevice(rsrcmgr)
device = PDFPageAggregator(rsrcmgr, laparams=laparams)
# Create a PDF interpreter object.
interpreter = PDFPageInterpreter(rsrcmgr, device)
# Process each page contained in the document.
for page in PDFPage.create_pages(document):
    interpreter.process_page(page)
    # recieve the LTPage object for the page.
    layout = device.get_result()
    ### PRINT FOR TESTING ###
    for obj in layout:
        if isinstance( obj, LTTextBoxHorizontal ):
            print obj.get_text().encode('utf-8')
