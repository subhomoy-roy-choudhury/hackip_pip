This is a command line tool which is used to gather system info and ipaddress and location of any user .

# Contribution :- 
The main project is in this github  repository 
https://github.com/subhomoy-roy-choudhury/Hack_IP

# Installation :-
```
 > pip install Hack_IP 
 > hackip
```
# Usage :-
1. Inorder to find location of any public IP Address . 
```
from hackip import hack_ip
from requests import get

ip = get('https://api.ipify.org').text
print(ip)
a = hack_ip()
print(a.my_ip_location(ip))
```
# Scrrenshot :-
![scrrenshot](Hack_IP_mobile_screenshot.jpeg)

# LICENSE :- 

Copyright (c) 2018 The Python Packaging Authority

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
