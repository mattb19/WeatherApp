import datetime as dt
import requests

BASE_URL = "http://api.openweathermap.org?"
API_Key = open('api_key', 'r'). read()
CITY = "Greenville"

url = BASE_URL + "appid=" = API_KEY + "&q=" = CITY

response = requests.get(url).json()

print(response)
