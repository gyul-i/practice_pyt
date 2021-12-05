import socket
import pickle
from random import randint

def combo(P1, key):
    P2 = []
    for i in range(len(P1)):
        P2 += chr(ord(P1[i]) ^ key)
    return ''.join(P2)

def send_mes(sock, mes, key):
    mes = combo(mes, key)
    sock.send(pickle.dumps(mes))

def receive(sock, key):
    mes = pickle.loads(sock.recv(1024))
    mes = combo(mes, key)
    return mes

HOST = '127.0.0.1'
PORT = 8080

sock = socket.socket()
sock.connect((HOST, PORT))

p = randint(0,10000)
g = randint(0,10000)
a = randint(0,10000)

A = g ** a % p
sock.send(pickle.dumps((p, g, A)))

B = pickle.loads(sock.recv(1024))
key = B ** a % p
mes= input("Сообщение: ")
while mes != 'exit':
    send_mes(sock, mes, key)
    print(receive(sock, key))
    mes = input()

sock.close()
