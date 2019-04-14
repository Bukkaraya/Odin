from influxdb import InfluxDBClient
from sense_hat import SenseHat
import time

client = InfluxDBClient(host='localhost', port=8086)
client.switch_database('sense')

sense = SenseHat()

if __name__ == '__main__':
    while True:
        readings = [{
            'measurement': 'roomReadings',
            'fields': {
                    'temperature': sense.get_temperature(),
                    'humidity': sense.get_humidity(),
                    'pressure': sense.get_pressure()
                }
            }]
        result = client.write_points(readings)
        if not result:
            print('There seems to have been an issue...')
        time.sleep(5)

