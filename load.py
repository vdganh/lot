import socket

ip = "127.0.0.1"
port = 4444

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addres = (ip, port)
    sock.connect(addres)

    msg = sock.recv(1024)

    print(msg.decode())

    sock.close()

main()