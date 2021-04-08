import requests
import json

questions = {

}

r = requests.get("https://api.stackexchange.com/2.2/questions")

try:
    questions = r.json()
except json.decoder.JSONDecodeError:
    print("Error")
else:
    print(questions)