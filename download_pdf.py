import os
import requests
import json

# Load the JSON data
with open("pdf-links.json") as file:
    data = json.load(file)


# Create the /data directory if it doesn't exist
os.makedirs("data", exist_ok=True)

# Loop over the JSON data and download the PDFs
for name, url in data.items():
    response = requests.get(url)
    if response.status_code == 200:
        file_path = os.path.join("data", f"{name}.pdf")
        with open(file_path, "wb") as file:
            file.write(response.content)
        print(f"Downloaded {name}.pdf")
    else:
        print(f"Failed to download {name}.pdf")