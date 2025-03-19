import requests

# URL of the website you want to scrape
url = "https://example.com"

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print("Request successful!")
    html_content = response.text  # Get the HTML content
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
