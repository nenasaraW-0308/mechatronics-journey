// Day 3: Reading Analog Sensor / Potentiometer Data in Embedded C
const int sensorPin = 34; // Analog input pin on ESP32

void setup() {
  Serial.begin(115200);
  Serial.println("Day 3: Sensor Data Reading Initialized");
}

void loop() {
  int sensorValue = analogRead(sensorPin); // Read analog value from sensor
  float voltage = sensorValue * (3.3 / 4095.0); // Convert to voltage
  
  Serial.print("Raw Sensor Value: ");
  Serial.print(sensorValue);
  Serial.print(" | Calculated Voltage: ");
  Serial.print(voltage);
  Serial.println("V");
  
  delay(2000); // Wait for 2 seconds
}
