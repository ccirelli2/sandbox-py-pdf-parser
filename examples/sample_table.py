"""
Purpose of this section is to demonstrate how to create a section and
visualize it.

We also practice assigning new names to font families, which can be used to
filter elements..
- Why is this important?  Because headers may have a different font than
other text in the body, which helps to differentiate elements from one another.
"""
# Libraries
import os
from decouple import config
from py_pdf_parser.loaders import load_file
from py_pdf_parser.visualise import visualise

# Globals
DIR_ROOT = config("DIR_ROOT")
DIR_DATA = config("DIR_DATA")
FILE_NAME = "order_summary.pdf"

# Change Fonts
font_mapping = {
    "BAAAAA+LiberationSerif-Bold,12.0":"Section_Headers",
    "DAAAAA+FreeMonoBold,12.0": "Column_Headers"
}

# Load File
document = load_file(
    os.path.join(DIR_DATA, FILE_NAME),
    font_mapping=font_mapping
)

# Create Sections
order_summary_sub_title_element = (
    document.elements.filter_by_font("Section_Headers")
    .filter_by_text_equal("Order Summary:")
)


# Isolate Table Headers
table_headers = (
    document
    .elements
    .filter_by_font("Column_Headers")
)


# Identify Elements to Exclude from headers search
total_key = (
    document
    .elements
    .filter_by_text_equal(
        text="Total:"
    )
    .extract_single_element()
)


total_value = (
    document
    .elements
    .to_the_right_of(total_key)
    .extract_single_element()
)

# Define Section
total_section = (
    document
    .sectioning
    .create_section(
        name="totals",
        start_element=total_key,
        end_element=total_value,
        include_last_element=True
    )
)

# Visualise Section
visualise(
    document=document,
    elements=total_section.elements,
    show_info=True
)
