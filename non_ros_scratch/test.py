import serial
import time

# Open a serial connection to GPS
# Adjust '/dev/ttyS0' to your serial port (might be ttyAMA0, ttyS0, etc.)
gps_serial = serial.Serial('/dev/ttyS0', 9600, timeout=1)

try:
    print("Reading GPS data. Press CTRL+C to exit.")
    while True:
        data = gps_serial.readline().decode('utf-8')
        if data:
            print(data, end='')  # Print raw NMEA sentences
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Exiting program")

# Close the serial connection
gps_serial.close()
