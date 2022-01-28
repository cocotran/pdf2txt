import argparse
from ast import arg
import sys
from traceback import print_tb

from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer

def extract(pdf_file_path: str, output_path: str):
    f = open(output_path, "a")
    for page_layout in extract_pages(pdf_file_path):
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                f.write(element.get_text())
    f.close()

def main():
    parser = argparse.ArgumentParser(description='Extract text from pdf files')
    parser.add_argument('-m', '--multiple', dest='multiple_file', help='Extract text to multiple file. (Default to one file)', default=False)
    parser.add_argument('-i', '--infile', nargs='*', required=True, dest='infile')
    parser.add_argument('-o', '--outfile', dest='outfile', nargs='?')
    args = parser.parse_args()

    if args.multiple_file:
        pass
    else:
        outfile = args.outfile
        if args.outfile is None:
            outfile = args.infile[0].replace("pdf", "txt")
        if outfile[-4:] != ".txt":
            outfile = outfile + ".txt"
        for file in args.infile:
            extract(file, outfile)

main()