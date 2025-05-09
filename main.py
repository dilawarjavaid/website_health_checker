import requests
import csv
from datetime import datetime

input_file = "websites.txt"

with open(input_file, "r") as file:
    websites = [line.strip() for line in file if line.strip()]

print(f"Checking {len(websites)} websites...")
