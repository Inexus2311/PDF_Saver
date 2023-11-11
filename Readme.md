# Protect PDF Files

This Python script provides a simple way to protect PDF files by adding password encryption to them. It utilizes the PyPDF2 library for handling PDF operations.
Installation

Before running the script, make sure you have Python installed on your system. You can download it from Python's official website.

# Clone Repository

Clone the repository or download the script file.

    git clone https://github.com/your-username/protect-pdf-script.git

# Installations

cd protect-pdf-script

Install the required Python packages using the following command:

    pip install PyPDF2

or install the requirements in repository

    pipenv install Pipfile

# Usage

Run the script from the command line with the required parameters:

    python protect_pdf.py -n <PDF_FILENAME> -p <PASSWORD>

Replace <PDF_FILENAME> with the name of the PDF file you want to protect and <PASSWORD> with the desired password.
Example

    python protect_pdf.py -n "example.pdf" -p "securepassword"

Notes

    The script will prompt you to enter the PDF filename and password.
    If the specified PDF file does not exist, the script will keep prompting until a valid filename or "q" to quit is entered.
    The protected PDF will be saved as <PDF_FILENAME>_protected.pdf in the same directory.

Feel free to contribute and improve the script!
