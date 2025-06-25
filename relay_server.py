import socket
import threading

clients = []

def handle(client, other):
    while True:
        try:
            data = client.recv(1024)
            if not data:
                break
            other.sendall(data)
        except:
            break
    client.close()
    other.close()

s = socket.socket()
s.bind(('0.0.0.0', 9000))
s.listen(2)
print("Relay server listening on port 9000...")

while len(clients) < 2:
    conn, addr = s.accept()
    print("Connected:", addr)
    clients.append(conn)

threading.Thread(target=handle, args=(clients[0], clients[1])).start()
threading.Thread(target=handle, args=(clients[1], clients[0])).start()