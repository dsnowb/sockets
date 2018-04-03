import socket
from datetime import datetime as dt

PORT = 1337
print('--- Starting server on port {} at {} ---'.format(PORT, dt.now()))

# set up TCP socket
sock = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
        socket.IPPROTO_TCP
)
sock.bind(('127.0.0.1', 1337))
sock.listen()
recv_buffer = 8

while True:
    try:
        conn,addr = sock.accept()

        msg = ''
        while True:
            part = conn.recv(recv_buffer)
            msg += part.decode('utf8')
            if len(part) < recv_buffer:
                break;
        msg = '[{}] Echoed: '.format(dt.now()) + msg
        
        print(msg)
        conn.sendall(msg.encode('utf8'))
        conn.close()
    
    except KeyboardInterrupt:
        print('\b\b--- Stopping server on port {} at {} ---'.format(PORT, dt.now()))
        sock.close()
        exit()
