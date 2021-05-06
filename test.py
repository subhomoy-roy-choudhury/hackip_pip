from hackip import hack_ip
import hackip
from requests import get

ip = get('https://api.ipify.org').text
print(ip)
a = hack_ip()
print(a.my_ip_location(ip))