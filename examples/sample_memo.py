"""
"""
# Libraries
import os
from decouple import config
from py_pdf_parser.loaders import load_file
from py_pdf_parser.visualise import visualise

# Globals
DIR_ROOT = config("DIR_ROOT")
DIR_DATA = config("DIR_DATA")
FILE_NAME_MEMO = "simple_memo.pdf"
FILE_NAME_TABLE = "order_summary.pdf"


# Load File
document = load_file(os.path.join(DIR_DATA, FILE_NAME_MEMO))


# Visualize Document
# visualise(document)

# Extract Elements
elements = document.elements

# Get Element - Text Search - Reference Element(s)
to_element = elements.filter_by_text_equal("TO:").extract_single_element()
print(to_element)
print(to_element.text())

# Get Element to the right of reference element
to_text = document.elements.to_the_right_of(to_element).extract_single_element().text()




# Create Sections
document = load_file(os.path.join(DIR_DATA, FILE_NAME_TABLE))

order_summary_sub_title_element = (
    document.elements.filter_by_font("sub_title")
    .filter_by_text_equal("Order Summary:")
    .extract_single_element()
)


"""
totals_sub_title_element = (
    document.elements.filter_by_font("sub_title")
    .filter_by_text_equal("Totals:")
    .extract_single_element()
)

final_element = document.elements[-1]

order_summary_section = document.sectioning.create_section(
    name="order_summary",
    start_element=order_summary_sub_title_element,
    end_element=totals_sub_title_element,
    include_last_element=False,
)
"""



