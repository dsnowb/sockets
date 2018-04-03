import socket
import sys

# Set up client TCP socket and connect to server
avail = socket.getaddrinfo('127.0.0.1', 1337)
stream_info = [i for i in avail if i[1] == socket.SOCK_STREAM][0]
client = socket.socket(*stream_info[:3])
client.connect(stream_info[-1])

client.sendall(str(sys.argv[1]).encode('utf8'))

# Receive and assemble message from client
recv_buffer = 8
msg = '' 
while True:
    part = client.recv(recv_buffer)
    msg += part.decode('utf8')
    if len(part) < recv_buffer:
        break

print(msg)

client.close()
