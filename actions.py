# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
import requests , json
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

    def name(self):
        return 'action_weather'

    def run(self,dispatcher,tracker,domain,):
        loc = tracker.get_slot('location')
        r = requests.get('http://api.openweathermap.org/data/2.5/weather?q={}&appid=7a35b812533ac1adb0482b7cd81f7b26'.format(loc))
        loc_weather = json.loads(r.content)
        name = loc_weather['name'] #provides the name of the country whose weather you are forecasting
        w=loc_weather['weather']
        description = w[0]['description']#gives the weather details of that particular country
        current_temp = loc_weather['main']['temp'] #gives the current temperature of that particular country
        max = loc_weather['main']['temp_max']#gives the maximum temperature
        min = loc_weather['main']['temp_min'] #gives the minimum temerature
        pressure = loc_weather['main']['pressure']
        humidity = loc_weather['main']['humidity']
        wind_speed = loc_weather['wind']['speed']
        response = """It is currently {} kelvin in {} at the moment.
              The maximum tempertaure  is {} kelvin and the MINIMUM tempertaure is {} kelvin.
              The humidity is {} and the pressure  is {} .
              The wind speed is {} mph. """.format(current_temp , name , max , min , humidity , pressure , wind_speed)
        dispatcher.utter_message(response)
        return[]
