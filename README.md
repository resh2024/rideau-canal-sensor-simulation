## Overview

This repository contains the IoT Sensor Simulator used to generate real-time environmental telemetry for the Rideau Canal Skateway Monitoring System.

The simulator creates three virtual IoT devices, each representing a different canal location:

- Dow's Lake

- Fifth Avenue

- NAC

Every 10 seconds, each device sends randomized, realistic sensor readings to Azure IoT Hub.

Technologies Used

- Python 3.x

- Azure IoT Device SDK

- python-dotenv

- JSON for telemetry formatting

## Prerequisites

You must have:

- Python 3.8+

- An Azure IoT Hub instance

- Three IoT devices registered in IoT Hub

- Valid device connection strings

- Internet access

## Installation

Clone the repository:

git clone https://github.com/resh2024/rideau-canal-sensor-simulation
cd rideau-canal-sensor-simulation

- Install dependencies:

- pip install -r requirements.txt

## Configuration

Create a .env file in the project root:

DOWS_LAKE_CONNECTION_STRING="your-connection-string"
FIFTH_AVENUE_CONNECTION_STRING="your-connection-string"
NAC_CONNECTION_STRING="your-connection-string"

A reference file .env is included.

## Usage

Run the simulator:

python sensor_simulator.py

This starts continuous telemetry streaming to Azure IoT Hub.

To stop:

CTRL + C

## Code Structure

rideau-canal-sensor-simulation/
├── sensor_simulator.py # Main simulation script
├── requirements.txt # Python dependencies
├── .env.example # Example environment variable file
├── README.md # Documentation
└── config/
└── sensor_config.json # Optional: custom ranges for sensor data

🧠 Code Explanation
Main Script: sensor_simulator.py

Handles:

Loading environment variables

Initializing IoT Hub clients

## Generating sensor data

Sending JSON messages to Azure IoT Hub every 10 seconds

Key Functions
Function Description
generate_sensor_data(location) Creates randomized sensor values
send_message(client, payload) Sends a JSON message to IoT Hub
run_simulator() Main loop running all devices
📡 Sensor Data Format
JSON Schema
{
"location": "string",
"timestamp": "ISO-8601 datetime",
"ice_thickness_cm": "float",
"surface_temp_c": "float",
"snow_accumulation_cm": "float",
"external_temp_c": "float"
}

Sample Output
{
"location": "Dows_Lake",
"timestamp": "2025-12-07T07:29:05.373733",
"ice_thickness_cm": 27.7,
"surface_temp_c": -9.4,
"snow_accumulation_cm": 4.2,
"external_temp_c": 4.7
}

## Troubleshooting

ModuleNotFoundError: No module named 'azure'

- Install missing packages:

- pip install azure-iot-device python-dotenv

Error: Missing connection string

- Check .env spelling:

DOWS_LAKE_CONNECTION_STRING=
FIFTH_AVENUE_CONNECTION_STRING=
NAC_CONNECTION_STRING=

IoT Hub is not receiving messages

Check:

- Device exists in IoT Hub

- Correct connection strings

- No firewall blocking MQTT or AMQP

- Internet connection

Null values showing in Stream Analytics

- Ensure your ASA input matches your JSON field names:

- ice_thickness_cm

- surface_temp_c

- snow_accumulation_cm

- external_temp_c

Script closes immediately

- Run in debug mode:

- python sensor_simulator.py --debug
