
# IoT Assignment 3 - MQTT System

This repository contains the code and scripts for the IoT assignment where we use MQTT to publish and subscribe to sensor data, which is then sent to ThingSpeak for visualization and storage.

## Project Overview

This project involves creating a simple IoT system that simulates the publishing of sensor data (Temperature, Humidity, CO2 Levels) from an MQTT publisher to an MQTT broker. The subscriber receives this data and sends it to a ThingSpeak channel for further analysis and visualization.

### Components
1. **Publisher**: Generates random sensor data and publishes it to an MQTT topic.
2. **Subscriber**: Listens to the MQTT broker for incoming messages, processes the data, and sends it to ThingSpeak.
3. **ThingSpeak**: Cloud-based platform to store and visualize the sensor data.

## Steps Involved

1. **Publisher**: 
   - Publishes random sensor data(Temperature, Humidity, CO2 Levels) to an MQTT broker.
   - The data is in JSON format and is published at regular intervals to a dynamic topic.

2. **Subscriber**:
   - Subscribes to the MQTT topic to receive sensor data.
   - On receiving the data, it sends it to ThingSpeak via an HTTP API.

3. **ThingSpeak**:
   - Stores the data in respective fields (Temperature, Humidity, CO2).
   - The ThingSpeak API key is required for writing data to the channel.

## Technologies Used
- **MQTT**: Used for communication between the publisher and subscriber.
- **ThingSpeak**: Used for storing and visualizing the sensor data.
- **Python**: Used to implement the publisher, subscriber, and communication with ThingSpeak.
- **Paho MQTT**: Python library for MQTT.
- **Requests**: Python library to send HTTP requests to ThingSpeak.

## ThingSpeak Channel Link

[ThingSpeak Channel](https://thingspeak.mathworks.com/channels/2890602)
