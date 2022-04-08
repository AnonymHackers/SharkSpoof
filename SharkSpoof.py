import time
import socket
import subprocess, os
import sys
os.system("color a")
def PortScanning(Target, Port):
	global connection
	try:
		connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		connection.connect((Target, Port))
	except:
		print("[WARNING] The Scan has a Error")
		time.sleep(5)
		sys.exit()
	while True:
		data = connection.recv(512)
		if data.lower() == 'q':
			connection.close()
			break
	print("[INFO] Received>: %s" % data)
def SystemScanning(Target):
	global s
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	index = 1
	while True:
		try:
			s.connect((Target, index))
			collect_data = s.recv(512)
			print("[INFO] System received>: %s" % collect_data)
			if data.lower() == 'q':
				s.close()
				break
		except:
			Error = 1
def getPortInfo(Target, Port):
	try:
		sd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sd.connect((Target, Port))
		print(f"[INFO] Port: {Port} Open")
	except:
		print(f"[INFO] Port: {Port} Closed")
while True:
	Command = input(">")
	if Command == 'help':
		print("PortScanning.info = Scanning informations from Port")
		print("SystemScanning.info = Scanning System from Target")
		print("PortInformation.get = Scan port to see if he open")
	elif Command == 'PortScanning.info':
		Target = input("Target> ")
		Door = int(input("Port> "))
		PortScanning(Target, Door, Local)
	elif Command == 'SystemScanning.info':
		Target = input("Target> ")
		SystemScanning(Target, LocalMain)
	elif Command == 'PortInformation.get':
		Target = input("Target> ")
		Port = int(input("Port> "))
		getPortInfo(Target, Port)