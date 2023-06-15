from machine import Pin
import dht
d = dht.DHT22(Pin15))
for i in range(100):
  d.measure()
  time.sleep(1)
  print(d.temerature())
  print(d.humidity)
  time.sleep(3)
  
  
