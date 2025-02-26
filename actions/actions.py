from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
from typing import Any, Text, Dict, List
import pandas as pd
import csv

class GetAnswer(Action):
     def __init__(self):
         self.faq_d = pd.read_csv('./data/example.csv')
         qs = list(self.faq_d['question'])
         with open("./data/example.yml", "wt", encoding="utf-8") as f:
             f.write('version: "2.0"\n')
             f.write("nlu: \n- intent: question\n  examples: | \n")
             for q in qs:
                 f.write(f"    - {q}\n") 

     def name(self) -> Text:
        return "action_get_answer"

        return []

class ActionRouteBot(Action):
    def name(self) -> str:
        return "action_route_bot"

    def run(self, dispatcher, tracker, domain):
        user_message = tracker.latest_message.get("text")
        # Add logic to route to Bot 1 or Bot 2
        if "bot1" in user_message.lower():
            dispatcher.utter_message(response="utter_greet")
        elif "bot2" in user_message.lower():
            dispatcher.utter_message(response="utter_greet_bot_smenu")
        else:
            dispatcher.utter_message(text="I am not sure which bot to use.")
        return []

class ActionCallAPI(Action):

    def name(self) -> str:
        return "action_call_api"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain) -> list:
        # Gọi API
        url = "https://identity-api.tesop.asia/en/api/v1.0/User/smenu-phone"
        params = {

        }

        # Thực hiện yêu cầu GET
        response = requests.get(url)
        print(response.json())
        message = f"Data received: {response.json()}"
        # Kiểm tra kết quả
        # if response.status_code == 200:
        #     # Lấy thông tin từ data
        #     message = f"Data received: {response.data}"
        # else:
        #     message = "Failed to fetch data from API."

        # Gửi lại phản hồi đến người dùng
        dispatcher.utter_message(text=message)

        return []