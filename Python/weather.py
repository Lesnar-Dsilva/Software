import requests;#web requests
from pprint import pprint;#parse JSON

key = "";#API Key
city = input("Enter a city: ");
api = f"https://api.openweathermap.org/data/2.5/weather?appid={key}&q={city}";
weather_data = requests.get(api).json();
pprint(weather_data["main"]);
#28mins 27/05/2022
