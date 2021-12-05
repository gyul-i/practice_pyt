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
    mes = combo(mes,key)
    return mes

HOST = '127.0.0.1'
PORT = 8080

sock = socket.socket()
sock.bind((HOST, PORT))
sock.listen(1)
conn, addr = sock.accept()

mes = conn.recv(1024)

p, g, A = pickle.loads(mes)
b = randint(0, 10000)
B = g ** b % p
conn.send(pickle.dumps(B))
key = A ** b % p


while True:
    try:
        mes = receive(conn, key)
        print(mes)
        send_mes(conn, 'Сообщение успешно получено и расшифровано', key)
    except EOFError:
        break

conn.close()