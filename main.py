import requests
import csv
from datetime import datetime

input_file = "websites.txt"


def check_website(url):
    """Check the health of a website."""
    try:
        response = requests.get(url, timeout=5)
        status = "Online" if response.status_code == 200 else "Offline"
        return response.status_code, response.elapsed.total_seconds() * 1000, status
    except requests.exceptions.RequestException:
        return None, None, "Offline"


with open(input_file, "r") as file:
    websites = [line.strip() for line in file if line.strip()]

print(f"Checking {len(websites)} websites...")
