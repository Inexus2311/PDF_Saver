"""protect pdf files
Created by Insomnia404
"""
# imports
import os
import sys
import argparse

# import json
from PyPDF2 import PdfWriter, PdfReader


def quite_program():
    """quit Programm"""
    sys.exit()


# Read from launch json file

# def load_launch_json_args():
#     """Load arguments from launch.json"""
#     try:
#         with open("./launch.json") as json_file:
#             launch_config = json.load(json_file)
#             return launch_config.get("configurations", [])[0].get("args", [])
#     except (FileNotFoundError, json.JSONDecodeError, IndexError):
#         return []


def protect_pdf(filename, password):
    """protect pdf function"""
    while not os.path.exists(filename):
        message = (
            f"[-] File: {filename} does not exist! "
            "Enter again oder quit the program with q"
        )
        print(message)
        answer = input()
        filename = answer
        if answer.lower() == "q":
            print("Programm will closing now!")
            quite_program()
    # Read PDF
    pdf_reader = PdfReader(filename)
    pdf_writer = PdfWriter()
    for page in pdf_reader.pages:
        # Einzelene Seiten auf pdf writer hinzufügen
        pdf_writer.add_page(page)

    pdf_writer.encrypt(user_password=password, use_128bit=True)
    output_filename = filename + "_protected.pdf"
    with open(output_filename, "wb") as out:
        pdf_writer.write(out)
    print(f"{filename} has been protected!")


def main():
    """main"""
    # Argparser definition
    parser = argparse.ArgumentParser(description="Protect a PDF file.")
    parser.add_argument("-n", "--name", required=True)
    parser.add_argument("-p", "--password", required=True)

    # Übernehmen der Argumente aus launch.json
    # launch_args = load_launch_json_args()
    # if launch_args:
    #     sys.argv.extend(launch_args)

    # Manuell Argumente zu sys.argv hinzufügen
    # sys.argv.extend(["--name", "Erste Schritte.pdf", "--password", "test"])
    args = parser.parse_args()
    print(args)
    protect_pdf(args.name, args.password)


# Hier rufst du die main-Funktion auf
if __name__ == "__main__":
    main()
