import os
from socket import *
from sys import *


def tester(host, port):
	try:
		app=create_connection((host, port))
		if app:
			own_addr=app.getsockname()
			print('... connection de %s:%s vers %s:%s'%(own_addr[0], own_addr[1],host,port))
			print("[*]Le port %s est ouvert sur %s"%(port, host))
			print ' '
			
	except Exception, e:
		print("[-]Aucune connection n'a pu etre etablie sur le port %s"%port)
		print ' '

def many_scan(host, ports):
	for port in ports:
		tester(host, port)


def most_scan(host, nb):
	ports=[21,23,80,25,8000,43,800,3721,4306,27,33,22,4001,2017,1,45]
	many_scan(host, ports[:nb])

if __name__ == '__main__':
	option=str(argv[1])
	host=str(argv[2])
	if option == '--tester' or option == '-t':
		port=int(argv[3])
		tester(host, port)
	elif option == '--tester_bcp' or option == '-ts':
		ports=argv[3:-1]
		many_scan(host, ports)
	elif option == '--plage_port' or option == '-pp':
		nb=int(argv[3])
		most_scan(host,nb)
	else:
		print('cette option n\'est pas disponible')
