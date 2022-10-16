#!/bin/python3
import socket 
import sys 
from datetime import datetime

# define our target
if len(sys.argv) == 3:
	target = socket.gethostbyname(sys.argv[1])
else: 
	print("Invalid amount of arguments")
	print("Syntax: python3 scanner.py <ip>")
#add pretty banner
print("-" * 50)
print("scanning target " + target)
print ("Time started: " + str (datetime.now() ))
print("-" * 50)

try: 
	for port in range(50,1000):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		Socket.setdefaulttimeout (1)
		result = s.connect_ex((target,port))
		if result ==0:
			print("Port {} is open " .format(port))
		s.close()
except KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit()
except socket.gainerror:
	print("Hostname could not be resolved.")
	sys.exit()
except	socket.error:
	print ("Couldn't connect to server.")
	sys.exit()
