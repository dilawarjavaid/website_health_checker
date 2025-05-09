# Website Health Monitor

A simple command-line tool to monitor the health of websites listed in a `websites.txt` file. It checks each site's status, response time, and logs the results into a CSV file (`log.csv`).

## Features

- Checks if websites are online or offline
- Logs response time and HTTP status code
- Appends results to a timestamped log
- Simple to use and extend

## Requirements

- Python 3.x
- `requests` module

Install dependencies using:

```bash
pip install requests
````

## Usage

1. **Add websites to monitor:**

   Create a `websites.txt` file and list one URL per line:

   ```
   https://example.com
   https://google.com
   ```

2. **Run the script:**

   ```bash
   python monitor.py
   ```

3. **Check the output:**

   * The script will print the health status of each website.
   * Results will be saved to `log.csv` in the following format:

     ```
     Timestamp, URL, Response Time (ms), Status Code, Status
     ```

## Example Output

```bash
Checking 2 websites...
https://example.com - Online - 200
https://google.com - Online - 200
```
![Screenshot (16)](https://github.com/user-attachments/assets/4cbae9a0-ee13-43ec-9149-5d26711cb089)


