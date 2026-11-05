# Day 4: Processing Sensor Data using Python Automation
import csv
import os

# 1. Dummy sensor data simulation and writing to a CSV file
file_name = "sensor_log.csv"
data = [
    ["Timestamp", "Sensor_ID", "Temperature_C", "Status"],
    ["2026-11-05 08:00:00", "SEN_01", 25.5, "Normal"],
    ["2026-11-05 08:05:00", "SEN_01", 28.2, "Warning"],
    ["2026-11-05 08:10:00", "SEN_01", 31.0, "Critical"],
    ["2026-11-05 08:15:00", "SEN_01", 26.1, "Normal"]
]

with open(file_name, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"-> Created and wrote dummy data to {file_name}")

# 2. Reading and processing the data using Python
print("\n-> Reading and filtering high-temperature logs:")
with open(file_name, mode='r') as file:
    reader = csv.reader(file)
    header = next(reader) # Skip header
    print(f"Header: {header}")
    
    for row in reader:
        temp = float(row[2])
        if temp > 28.0:
            print(f"ALERT! High temperature detected at {row[0]}: {temp}°C")