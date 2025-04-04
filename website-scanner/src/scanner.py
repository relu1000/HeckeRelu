# scanner.py

import requests
from utils.helpers import parse_response, format_output
from config.settings import API_KEY, TIMEOUT

def scan_website(url):
    try:
        response = requests.get(url, timeout=TIMEOUT)
        if response.status_code == 200:
            parsed_data = parse_response(response.text)
            output = format_output(parsed_data)
            print(output)
        else:
            print(f"Failed to retrieve {url}: Status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    target_url = input("Enter the website URL to scan: ")
    scan_website(target_url)