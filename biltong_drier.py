#!/usr/bin/python3 

# you need to import DHT with "pip3 install adafruit-circuitpython-dht"
# then install "sudo apt-get install libgpiod2"

import Adafruit_DHT
import RPi.GPIO as GPIO
import time
 
# Set sensor type : Options are DHT11,DHT22 or AM2302
sensor=Adafruit_DHT.DHT11
 
# Tell GPIO to which pin the sensor is connected to:
dht=17
relayFan = 21
relayHeat = 20
relays = (20,21)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(relayFan, GPIO.OUT)
GPIO.setup(relayHeat, GPIO.OUT)

#oorsprinklike code, ek gebruik dit nie
#humidity, temperature = Adafruit_DHT.read_retry(sensor, dht)
#if humidity is not None and temperature is not None:
 # print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
#else:
 # print('Failed to get reading. Try again!')

# my eerste toets code:
#if temperature < 20:
#    print ("Temperature is", (temperature) )
#    print ("Humidity is", (humidity) )
#    print ("Switching on relays")
#    GPIO.output(relays, True)
#    time.sleep(5)
#    print ("Switching off relays")
#    GPIO.output(relays, False)
#elif humidity > 60:
#    print ("Humidity is", (humidity) )
#    print ("Temperature is", (temperature) )
#    print ("Switching on relays")
#    GPIO.output(relays, True)
#    time.sleep(5)
#    print ("Switching off relays")
#    GPIO.output(relays, False)
#else:
#    print ('Nothing to do')
#
#GPIO.cleanup()

# volgende stap is om altwee readings in a while loop kondisie te sit.
# (i.e. terwyl temp of humiditeit kondisie waar is, sit altwee relays aan.
# moet verander word om fan langer aan te hou as heat element. 

print ('Take initial reading\n')
humidity, temperature = Adafruit_DHT.read_retry(sensor, dht)

while humidity > 60 or temperature < 25:
    print ('Temperature is', (temperature) )
    print ('Humidity is', (humidity) )
    print ('Switching on relays for 2 minutes \n')
    GPIO.output(relays, True)
    time.sleep(120)
    print ('Switching off relays\n')
    GPIO.output(relays, False)
    time.sleep(5)
    print ('taking new reading\n') 
    humidity, temperature = Adafruit_DHT.read_retry(sensor, dht)
    print ('Temperature is', (temperature) )
    print ('Humidity is', (humidity) )
else:
    print('Temp or Humidity now below threshold, switching to standby.\n')

GPIO.cleanup()

#end

