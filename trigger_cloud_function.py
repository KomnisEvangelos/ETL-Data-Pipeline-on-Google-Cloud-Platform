
import requests

url = "URL"

# Optional: Add data to be sent in the POST request body (as a dictionary)
data = {"": ""}

response = requests.post(url, json=data)

if response.status_code == 200:
  print("POST request successful!")
  print(response.text)
  # Access the response content (optional)
  # print(response.text)
else:
  print(f"Error: {response.status_code}")
  print(response.text)