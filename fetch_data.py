import requests

# ThingSpeak MQTT Credentials
MQTT_BROKER = "mqtt3.thingspeak.com"
MQTT_PORT = 1883
MQTT_CLIENT_ID = "OQQpOjEOCxoNFzkCITsKDD0"
MQTT_USERNAME = "OQQpOjEOCxoNFzkCITsKDD0"
MQTT_PASSWORD = "OH0MVqIeaY9me31twr+aAIRH"
CHANNEL_ID = "2890602"
READ_API_KEY = "EUXOJ4MTM77PXEG9"

# Fetching data from the last 5 hours (300 minutes)
url = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds.json?api_key={READ_API_KEY}&minutes=300"

response = requests.get(url)
data = response.json()

# Displaying fetched data
for entry in data["feeds"]:
    print(f"Timestamp: {entry['created_at']}, Temperature: {entry['field1']} Celsius, Humidity: {entry['field2']} %, CO2: {entry['field3']} ppm")