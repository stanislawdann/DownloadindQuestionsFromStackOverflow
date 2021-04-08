import requests
import json
import pprint
import webbrowser
import datetime

searchDate = datetime.date.today() - datetime.timedelta(days=7)

params = {
    "site" : "stackoverflow",
    "sort" : "votes",
    "order" : "desc",
    "fromdate" : searchDate,
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
        webbrowser.open_new_tab(question["link"])