from funcoes import validar_ip, analisar_ip, classificar, calcular, exibir_relatorio, AMARELO, AZUL, RESET
import os
import sys
import time

if sys.platform == "win32":
    os.system("")

# se retornar TRUE, programa fecha
# se retornar FALSE, programa continua
def checar_ip() -> bool:
    print("Digite um endereço IPv4 (ou 'sair' para encerrar):")
    ip: str = input().strip().lower()
    print()
    if ip == "sair":
        print(f"{AMARELO}Encerrando o Check my IP. Até logo!{RESET}")
        time.sleep(2)
        return True
    if validar_ip(ip) == False:
        return False
    analisar_ip(ip)
    return False

print(f"\nBem-vindo ao < {AZUL}Check my IP{RESET} >")
print("Nesta simples ferramenta de CLI, você pode digitar qualquer endereço IPv4 e receber um relatório completo.")
print("Teste e veja a mágica acontecer!\n")
while True:
    if checar_ip():
        break