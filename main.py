
# Simple python tool to retrieve weather station information and parse the JSON for data and send to telegram
# requires: requests, json, telegram_send
import requests
import json
import telegram_send

# send info via telegram
def send_data(text):
    telegram_send.send(messages=[text])

# retrieve and transform the weather data as a dict
def get_data(link):
    # Retrieve the data as a JSON
    data_json = requests.get(link).text

    # Transform into a dict (actually a dict of list of dict of dict)
    data_dict = json.loads(data_json)

    return data_dict

# retrieve
data = get_data("https://api.weather.com/v2/pws/observations/current?stationId=ITALHE7&format=json&units=m&apiKey=6532d6454b8aa370768e63d6ba5a832e")

message = "Current weather in Talheim, DE: \n"
message += "Timestamp: " + data["observations"][0]["obsTimeLocal"] + "\n"
message += "Temperature (°C): " + str(data["observations"][0]["metric"]["temp"]) + "\n"
message += "Wind Speed (km/h): " + str(data["observations"][0]["metric"]["windSpeed"]) + "\n"
send_data(message)
# Play around with the data

# Pretty print
#print(json.dumps(data, indent = 4, sort_keys=True))

# Print single values
#print("Timestamp: ",data["observations"][0]["obsTimeLocal"])
#print("Temperature (°C): ",data["observations"][0]["metric"]["temp"])
#print("Wind Speed (km/h): ",data["observations"][0]["metric"]["windSpeed"])
