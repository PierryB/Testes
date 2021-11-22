import socket


server = '127.0.0.1'  # localhost - loopback
port = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((server, port))
    sock.listen()  # escuta ...
    conn, addr = sock.accept() # informação do cliente que conectou
    with conn: # trabalhando com a conexão do cliente
        print('Cliente conectou com endereço:', addr)
        while True:  # while(1) {....}
            data = conn.recv(1024)  # leia 1024
            if not data:  # se não leu nada...
                break  # sai do while
            conn.sendall(data)  # se leu alguma coisa -> devolve para o cliente