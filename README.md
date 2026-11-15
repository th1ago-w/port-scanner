# Port Scanner

Port Scanner simples em Python usando sockets e threads.

## O que faz

Escaneia um intervalo de portas em um IP ou domínio e mostra quais estão abertas.

## Como usar

`python scanner.py`

## Exemplo de uso

Digite o IP ou domínio: `scanme.nmap.org`  
Porta inicial: `20`  
Porta final: `80`

Saída esperada:

[+] Porta 22 aberta
[+] Porta 80 aberta

## Tecnologias

- Python
- socket
- concurrent.futures

## Aviso

Use apenas em redes e sistemas que você tem autorização para testar.
