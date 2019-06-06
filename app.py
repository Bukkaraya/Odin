from prometheus_client import start_http_server, Gauge
from sense_hat import SenseHat
import time

sense = SenseHat()

pressure_gauge = Gauge("room_pressure", "Pressure readings for my room")
temperature_gauge = Gauge("room_temperature", "Temperature readings for my room")
humidity_gauge = Gauge("room_humidity", "Humidity readings for my room")

if __name__ == "__main__":
    start_http_server(4000)
    while True:
        pressure_gauge.set(sense.get_pressure())
        temperature_gauge.set(sense.get_temperature())
        humidity_gauge.set(sense.get_humidity())
