import socket
import threading

HOST = '0.0.0.0'

PORT = 8080

clients = []

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST , PORT ))
    server_socket.listen(5)
    print(f"Сервер запущено на хост {HOST}:{PORT}")
    while True:
        client_socket , add = (server_socket.accept())
        print(f"Клієнт підключився  ")
        clients.append(client_socket)
        t = threading.Thread()
        t.start()
if __name__ == "main":
    main()