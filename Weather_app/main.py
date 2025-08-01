import requests
import json
import os

city = input("Enter your city name :\n")
url = f"http://api.weatherapi.com/v1/current.json?key=cf2763011c6b4890bfe153928252607&q={city}"
response = requests.get(url)
Weather_report_dict = json.loads(response.text)
Weather = Weather_report_dict["current"]["temp_c"]
condition = Weather_report_dict["current"]["condition"]["text"]
wind_speed = Weather_report_dict["current"]["wind_kph"]
humidity = Weather_report_dict["current"]["humidity"]
print(Weather)
print(condition)
print(wind_speed)
print(humidity)
os.system(f"say 'The current temperature in {city} is {Weather} degrees celsius' ")
os.system(f"say 'And it is {condition}' ")
os.system(f"say 'Also the wind speed is {wind_speed} kilometer per hour and humidity is {humidity}%' ")

