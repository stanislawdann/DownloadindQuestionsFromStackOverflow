import requests
import json
import pprint
import webbrowser

params = {
    "site" : "stackoverflow",
    "sort" : "votes",
    "order" : "desc",
    "fromdate" : "2021-04-01",
    "tagged" : "python",
    "min" : 6
}

r = requests.get("https://api.stackexchange.com/2.2/questions", params)

try:
    questions = r.json()
except json.decoder.JSONDecodeError:
    print("Error")
else:
    for question in questions["items"]:
        pprint.pprint(question["link"])