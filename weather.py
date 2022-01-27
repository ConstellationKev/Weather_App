import requests
import os

divider = "-------------------------"
city_name = input("City name: ").strip()
state_code = input("State (optional) : ").strip()
print(divider)
api_key = os.environ.get("weather_api_key")
url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name},{state_code}&appid={api_key}"

response = requests.get(url)
# print(response.text)
status = response.status_code
if status == 404:
    print("City and/or state is not found, please check your inputs (note: state name can't be abbreviated sorry)")
    exit()
else:
    #finds the specifics we need in our weather output
    weather_in_area = (response.json()["weather"])

    for weather in weather_in_area:
        result = weather["main"]
        description = weather["description"]

    weather_in_area = (response.json()["main"])
    temperature = weather_in_area["temp"]
    feels_like = weather_in_area["feels_like"]
    humidity = weather_in_area["humidity"]

# printed output of the weather
given_weather = (f"""
{city_name}, {state_code}'s weather: {result}
Description: {description}
Temperature: {temperature}    Feels like: {feels_like}
Humidity: {humidity}

API from openweathermap.org
""")

print(given_weather)
