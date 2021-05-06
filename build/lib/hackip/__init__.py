import socket 
import os
import sys
import re
from colorama import Fore, Back, Style , init
from termcolor import colored
import platform
import psutil
from pyfiglet import Figlet
from requests import get
from geolite2 import geolite2


class hack_ip:
    def __init__(self):
        print("Hack_IP")

    def func(self, number):
        print("This is a function")
        return number

    # Location Tracker
    def my_ip_location(self,my_ip):
        reader = geolite2.reader()
        location = reader.get(my_ip)

        #geolite database dict values and fine tunning
        a=(location['city']['names']['en'])
        b=(location['continent']['names']['en'])
        c=(location['country']['names']['en'])
        d=(location['location'])
        e=(location['postal'])
        f=(location['registered_country']['names']['en'])
        g=(location['subdivisions'][0]['names']['en'])

        print('''city: %s\ncontinent: %s\ncountry: %s\nlocation: %s\npostal: %s\nregistered_country: %s\nsubdivisions: %s\n'''
        % (a,b,c,d,e,f,g))
