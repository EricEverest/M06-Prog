from datetime import datetime

with open("today.txt", "r") as file:
    today_string = file.read()

try:
    parsed_date = datetime.strptime(today_string, "%Y-%m-%d")
    print("Parsed date:", parsed_date)
except ValueError:
    print("Error: Unable to parse date from the file.")