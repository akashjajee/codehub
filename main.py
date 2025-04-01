import gspread
from oauth2client.service_account import ServiceAccountCredentials
from collections import defaultdict

from Autoemail import *


scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name('Auth_key.json', scope)

client = gspread.authorize(creds)

spreadsheet = client.open('Customer Issues')

worksheet = spreadsheet.get_worksheet(0)

data = worksheet.get_all_records()

customer_counts = defaultdict(lambda: {'Total': 0, 'Pending': 0, 'Resolved': 0})
for entry in data:
    customer = entry['Email ID']
    customer_counts[customer]['Total'] += 1
    if entry['Resolved'] == '':
        customer_counts[customer]['Pending'] += 1
    else:
        customer_counts[customer]['Resolved'] += 1


for customer, counts in customer_counts.items():
    SendMail(customer, counts['Total'], counts['Pending'], counts['Resolved'])

    print(f"Customer: {customer}")
    print(f"  Total Issues: {counts['Total']}")
    print(f"  Pending Issues: {counts['Pending']}")
    print(f"  Resolved Issues: {counts['Resolved']}")




