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


# import requests
# import json

# # === ThingSpeak Channel Config ===
# THINGSPEAK_API_KEY = "EUXOJ4MTM77PXEG9"
# CHANNEL_ID = "2890602"
# THINGSPEAK_FEED_URL = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds.json"

# def fetch_latest_data():
#     try:
#         response = requests.get(THINGSPEAK_FEED_URL, params={"api_key": THINGSPEAK_API_KEY, "results": 1})
#         if response.status_code == 200:
#             data = response.json()
#             latest_entry = data["feeds"][-1]  # Get last data point
#             print(f"📊 Latest Data: {json.dumps(latest_entry, indent=4)}")
#         else:
#             print(f"❌ Failed to fetch data: {response.status_code}")
#     except Exception as e:
#         print(f"❌ Error fetching data: {e}")

# if __name__ == "__main__":
#     fetch_latest_data()