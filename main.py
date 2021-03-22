
# Simple python tool to retrieve weather station information and parse the JSON for data
# requires: requests, json
import requests
import json

# Retrieve the data as a JSON
data_json = requests.get("https://api.weather.com/v2/pws/observations/current?stationId=ITALHE7&format=json&units=m&apiKey=6532d6454b8aa370768e63d6ba5a832e").text

# Transform into a dict (actually a dict of list of dict of dict)
data_dict = json.loads(data_json)

# Play around with the data

# Pretty print
#print(json.dumps(data_dict, indent = 4, sort_keys=True))

# Print single values
print("Timestamp: ",data_dict["observations"][0]["obsTimeLocal"])
print("Temperature (°C): ",data_dict["observations"][0]["metric"]["temp"])
print("Wind Speed (km/h): ",data_dict["observations"][0]["metric"]["windSpeed"])