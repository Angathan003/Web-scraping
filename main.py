import requests
from bs4 import BeautifulSoup

# Get user input
url = input("Enter the URL of the website: ")
heading = input("Enter the specific heading you want to extract information from: ")

# Send a GET request to the website
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find elements on the page using the specified heading
data = []
for element in soup.find_all(heading):
    data.append(element.text)

# Print the extracted data
if data:
    print(f"Information extracted from {heading}:")
    for item in data:
        print(item)
else:
    print(f"No information found with heading '{heading}'. Please try again.")
