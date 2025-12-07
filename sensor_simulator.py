import os
import json
import time
import random
from datetime import datetime
from azure.iot.device import IoTHubDeviceClient, Message
from dotenv import load_dotenv

load_dotenv()

# -------------------------------------------------------------------
# IoT Hub Connection Strings (one per device)
# -------------------------------------------------------------------
DEVICES = {
    "Dows_Lake": os.getenv("DEVICE_DOWS_LAKE"),
    "Fifth_Avenue": os.getenv("DEVICE_FIFTH_AVENUE"),
    "NAC": os.getenv("DEVICE_NAC")
}

# Validate that connection strings exist
for location, conn in DEVICES.items():
    if not conn:
        raise ValueError(f"Missing connection string for device: {location}")

# -------------------------------------------------------------------
# Sensor Value Generators (Realistic Ranges)
# -------------------------------------------------------------------
def generate_sensor_data(location):
    return {
        "location": location,
        "timestamp": datetime.utcnow().isoformat(),
        "ice_thickness_cm": round(random.uniform(20, 45), 1),
        "surface_temp_c": round(random.uniform(-15, 2), 1),
        "snow_accumulation_cm": round(random.uniform(0, 10), 1),
        "external_temp_c": round(random.uniform(-25, 5), 1)
    }

# -------------------------------------------------------------------
# Main Loop
# -------------------------------------------------------------------
def send_data():
    clients = {}

    # Create IoT Hub clients for each device
    for location, conn_str in DEVICES.items():
        clients[location] = IoTHubDeviceClient.create_from_connection_string(conn_str)

    print("Starting IoT sensor simulation...")
    print("Sending data every 10 seconds.\n")

    while True:
        for location, client in clients.items():
            data = generate_sensor_data(location)
            msg = Message(json.dumps(data))
            msg.content_type = "application/json"
            msg.content_encoding = "utf-8"

            client.send_message(msg)
            print(f"Sent from {location}: {data}")

        print("----- Cycle Complete -----\n")
        time.sleep(10)


if __name__ == "__main__":
    try:
        send_data()
    except KeyboardInterrupt:
        print("\nSimulation stopped.")
