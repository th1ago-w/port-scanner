import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((host, port))
            if result == 0:
                print(f"[+] Porta {port} aberta")
    except:
        pass

def scan(host, start_port, end_port, threads=100):
    print(f"Escaneando {host} de {start_port} até {end_port}...\n")
    with ThreadPoolExecutor(max_workers=threads) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(scan_port, host, port)

if __name__ == "__main__":
    alvo = input("Digite o IP ou domínio: ")
    inicio = int(input("Porta inicial: "))
    fim = int(input("Porta final: "))
    
    scan(alvo, inicio, fim)
