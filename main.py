import xml.etree.ElementTree as ET # For XML Parsing
import csv # For reading CSV
import json
import requests # For getting content from the web
from bs4 import BeautifulSoup # For parsing content from the web
import logging

# Main Function
def main():
    """The main function contains examples on how to read each type of file
    Example 1: Regular Text File
    Example 2: CSV File
    Example 3: XML File
    Example 4: JSON File
    Example 5: PDF FIle
    Example 6: Getting Content via API
    Example 7: Web Content with other means"""
    print("Main Function Executing")

    print("-x-"*25)

    # Example 1
    print("\nReading a regular Text File.")
    example_1 = open_file('Data/example_1.txt')
    print(f"Output: {example_1}\n")

    print("---" * 25)

    # Example 2

    print("\nReading a CSV File.")
    example_2 = csv_open('Data/example_2.csv')
    print(f"Output: {example_2}\n")

    print("---" * 25)

    # Example 3
    print("\nParsing an XML Text File.")
    example_3 = xml_parsing('Data/example_3.xml')
    print(f"Output: {example_3}\n")

    print("---" * 25)

    # Getting Content from the Web
    print("\nParsing  Text from the Web.")
    example_4 = get_web_content('https://www.horizonte-magazin.ch/2020/12/03/parfuem-der-baeume-ist-kampfstoff/')
    print(f"Output: {example_4}\n")


# Generic Function to read a file
def open_file(file_path):
    with open(file_path, 'r') as f:
        text = [line.strip() for line in f]
    return text


# Reading CSV Files
def csv_open(file_path):
    with open(file_path, newline='\n') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        text = [token for token in reader]
    return text


# Parsing XML Files
def xml_parsing(file_path):
    root_node = ET.parse(file_path).getroot()
    text = [tag.text  for tag in root_node.findall('token')]
    return text


def save_json(outfile, content):
    """ Generic function to save dictionary data to a JSON file"""
    logging.info(f"Written JSON as {outfile}")
    with open(outfile, 'w') as f:
        json.dump(content, f, indent=4)


def get_json(file_name):
    """ Generic function to retrieve data from JSON file"""
    with open(file_name) as f:
        data = json.load(f)
        return data

# ---------------------------------------------------------------


# Getting Content from the Internet
# Documentation: https://docs.python.org/3/library/urllib.request.html#module-urllib.request
def get_web_content(url):
    response = requests.get(url)
    if response.status_code != 200:
        response = None
    return response.text


def web_content_parsing(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')
    print(soup)


# The caller for the main function, this is the entry point for our program
if __name__ == '__main__':
    main()