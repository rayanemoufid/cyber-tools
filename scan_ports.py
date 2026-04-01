import socket

target = input("Entrez l'adresse IP cible : ")

print(f"Scan de {target} en cours...\n")

for port in range(1, 1025):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)
    
    result = sock.connect_ex((target, port))
    
    if result == 0:
        print(f"[+] Port {port} ouvert")
    
    sock.close()
