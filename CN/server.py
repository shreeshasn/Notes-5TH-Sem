import socket
import threading

HOST = '127.0.0.1'  # Localhost
PORT = 12345        # Port to listen on

clients = []

def handle_client(client_socket, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    while True:
        try:
            msg = client_socket.recv(1024).decode('utf-8')
            if not msg:
                break
            print(f"[{addr}] {msg}")
            broadcast(msg, client_socket)
        except:
            break
    print(f"[DISCONNECTED] {addr} has left.")
    clients.remove(client_socket)
    client_socket.close()

def broadcast(msg, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(msg.encode('utf-8'))
            except:
                client.close()
                clients.remove(client)

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"[STARTING] Server is listening on {HOST}:{PORT}")
        while True:
            client_socket, addr = server_socket.accept()
            clients.append(client_socket)
            print(f"[ACTIVE CONNECTIONS] {len(clients)}")
            thread = threading.Thread(target=handle_client, args=(client_socket, addr))
            thread.start()
    except Exception as e:
        print(f"[ERROR] {e}")
    finally:
        server_socket.close()

if __name__ == "__main__":
    start_server()
