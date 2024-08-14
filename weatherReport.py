import requests
import sys

import json

##################################################
# Takes input from user (day, estimated time of incident, and location (lat/long))
##################################################
date = input("Input date (yyyy-mm-dd): ")
print("Date: " + date)          # Print user entry to output
dateTime = date + "T00:00:00"   # For use in solar calculator

time = input("Time (xx:xx:xx): ")
print("Time: " + time)

offset = input("UTC Offset (MST:-6, MDT:-7): ")
print("UTC Offset: " + offset)

lat = input("Latitude (decimal): ")
print("Latitude: " + lat)
long = input("Longitude (decimal): ")
print("Longitude: " + long)

timeHour = int(time[0:2])       # Integer hour for weather report


##################################################
# Weather Report API
##################################################

#*************************************************************
# IMPORTANT: API key
key = "AGTT45RB2PRRLJ8GNA43WAW74"
#*************************************************************

url1 = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/" + str(lat) + "%2C" + str(long) + "/" + date + "/" + date + "?unitGroup=us&elements=datetime%2Cname%2Cprecip%2Cprecipprob%2Cprecipcover%2Cpreciptype%2Csnow%2Csnowdepth%2Cwindspeed%2Ccloudcover%2Cvisibility%2Cconditions%2Cdescription%2Cmoonphase&include=hours&key=" + key + "&contentType=json"
                
# Retrieve data from API
response = requests.request("GET", url1)
# Check if data was able to be accessed
if response.status_code!=200:
  print('Unexpected Status code: ', response.status_code)
  sys.exit()  


# Parse the results as JSON
jsonData = response.json()

# Get weather report from specified hour
jsonDays = jsonData['days']
jsonTime = jsonDays[0]['hours'][timeHour]

strTime = "TIME (hour): " + date + " " + jsonTime['datetime']

strConditions = "\n\nConditions: " + jsonTime['conditions']
strCloudCover = "\nCloud Cover (%): " + str(jsonTime['cloudcover'])
strVisibility = "\nVisbility: " + str(jsonTime['visibility'])

strPrecip = "\nPrecipitation: " + str(jsonTime['preciptype'])
if jsonTime['precipprob'] != 0.0:
  strPrecip = strPrecip + "\n\tAmount (in): " + str(jsonTime['precip']) + "\n\tSnow (in): " + str(jsonTime['snow'])

strSnow = "\n\tSnow Depth (in): " + str(jsonTime['snowdepth'])

strWind = "\nWindspeed (mph): " + str(jsonTime['windspeed'])

strMoon = "\nMoonphase: " + str(jsonDays[0]['moonphase'])


L = [strTime, strConditions, strCloudCover, strVisibility, strPrecip, strSnow, strWind, strMoon]

##################################################
# Solar Calculator API
##################################################

url2 = 'https://qed.epa.gov/hms/rest/api/meteorology/solar'
myobj = {"model": "day",
    "localTime": "",
    "source": "",
    "dateTimeSpan": {
        "startDate": dateTime,
        "endDate": dateTime,
        "dateTimeFormat": ""
    },
    "geometry": {
        "description": "",
        "comID": 0,
        "hucID": "",
        "stationID": "",
        "point": {
            "latitude": lat,
            "longitude": long
        },
        "geometryMetadata": "",
        "timezone": {
            "name": "",
            "offset": offset,
            "dls": False
        }
    },
    "dataValueFormat": "",
    "temporalResolution": "",
    "timeLocalized": False,
    "units": "",
    "outputFormat": "",
    "baseURL": "",
    "inputTimeSeries": ""}

x = requests.post(url2, json = myobj)

jsonString = json.loads(x.text)

results = list(jsonString["data"].values())[timeHour-1]

with open('weatherReport.txt', 'w') as file:
  file.writelines(L)
  file.write("\nSolar Elevation (deg above horizon): " + results[26])
  file.write("\nSolar Azimuth (deg CW from N): " + results[27])
