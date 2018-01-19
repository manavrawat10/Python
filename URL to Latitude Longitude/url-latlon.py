# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 20:31:52 2018

@author: Manvenddra
"""

from geopy.geocoders import Nominatim
import socket
import requests
ip=socket.gethostbyname("rodriguez.com")
ip=str(ip)
url = 'http://freegeoip.net/json/'+ip
r = requests.get(url)
js = r.json()
c_name=js['country_name']
print(c_name)
geolocator = Nominatim()
location = geolocator.geocode(c_name)
print((location.latitude, location.longitude))
