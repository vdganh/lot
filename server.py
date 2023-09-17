import socket

ip = "127.0.0.1"
port = 4444

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = (ip, port)
    sock.bind(address)
    sock.listen(1)
    print("Mengkoneksikan PORT : " + str(port))
    conn , ipvictim = sock.accept()
    msg = "PESAN DARI SERVER"
    conn.send(msg.encode())

main()