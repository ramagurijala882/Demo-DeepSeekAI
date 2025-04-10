import requests
import json

url = "http://localhost:11434/api/generate"
headers = {"Content-Type": "application/json"}
data = {
    "model": "llama3",
    "prompt": "What is water?"
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print("Response:")
print(response.text)
