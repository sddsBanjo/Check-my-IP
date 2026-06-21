AMARELO = "\033[93m"
AZUL = "\033[96m"
ROSA = "\033[38;2;255;192;203m"
VERDE = "\033[92m"
RESET = "\033[0m"

def validar_ip(ip_string: str) -> bool:
    msg = f"{AMARELO}{ip_string} {ROSA}não é um endereço IPv4 válido!{RESET}\n"
    ip = ip_string.split(".")
    if len(ip) != 4:
        print(msg)
        return False
    for octeto in ip:
        try:
            octeto_int = int(octeto)
            if not(0 <= octeto_int <= 255) or (str(octeto_int) != octeto):
                raise ValueError
        except ValueError:
            print(msg)
            return False
    if ip[0] == "0":
        print("Um endereço IPv4 normal não pode ter 0 como seu primeiro octeto.")
        return False
    return True

def classificar(octeto: int) -> tuple[str, str, str, str, str]:
    if 1 <= octeto <= 126:
        return "A", "255.0.0.0", "11111111.00000000.00000000.00000000", "REDE.HOST.HOST.HOST", "16.777.214"
    elif octeto == 127:
        return "A (Loopback)", "255.0.0.0", "11111111.00000000.00000000.00000000", "REDE.HOST.HOST.HOST", "N/A (Reservado)"
    elif 128 <= octeto <= 191:
        return "B", "255.255.0.0", "11111111.11111111.00000000.00000000", "REDE.REDE.HOST.HOST", "65.534"
    elif 192 <= octeto <= 223:
        return "C", "255.255.255.0", "11111111.11111111.11111111.00000000", "REDE.REDE.REDE.HOST", "254"
    elif 224 <= octeto <= 239:
        return "D (Multicast)", "N/A", "N/A", "N/A", "0"
    elif 240 <= octeto <= 255:
        return "E (Experimental)", "N/A", "N/A", "N/A", "0"

def calcular(ip: list, ip_class: str) -> tuple[str, str, str, str]:
    o1, o2, o3, o4 = ip[0], ip[1], ip[2], ip[3]
    if ip_class == "A":
        return f"{o1}.0.0.1", f"{o1}.255.255.254", f"{o1}.0.0.0", f"{o1}.255.255.255"
    elif ip_class == "A (Loopback)":
        return f"{o1}.0.0.1 (localhost)", f"{o1}.255.255.254", f"{o1}.0.0.0", f"{o1}.255.255.255"
    elif ip_class == "B":
        return f"{o1}.{o2}.0.1", f"{o1}.{o2}.255.254", f"{o1}.{o2}.0.0", f"{o1}.{o2}.255.255"
    elif ip_class == "C":
        return f"{o1}.{o2}.{o3}.1", f"{o1}.{o2}.{o3}.254", f"{o1}.{o2}.{o3}.0", f"{o1}.{o2}.{o3}.255"
    else:
        return "N/A", "N/A", "N/A", "N/A"

def exibir_relatorio(relatorio: dict) -> None:
    print(f"{AZUL}[========= RELATÓRIO DE DETALHES IPv4 =========]{RESET}")
    print(f" Endereço:            {VERDE}{relatorio['ipv4_address']}{RESET}")
    print(f" Classe do IP:        {relatorio['ip_class']}")
    print(f" Máscara:             {relatorio['mask']}")
    print(f" Máscara (binário):   {relatorio['mask_bin']}")
    print(f" Função da Máscara:   {relatorio['mask_func']}")
    print(f" Qtd. Hosts Válidos:  {relatorio['num_hosts']}")
    print(f" Endereço Rede:       {relatorio['network_address']}")
    print(f" Endereço Broadcast:  {relatorio['broadcast_address']}")
    print(f" Primeiro Host Útil:  {relatorio['first_host']}")
    print(f" Último Host Útil:    {relatorio['last_host']}")
    if relatorio['ip_class'] == "A (Loopback)":
        print(f"\n{AMARELO}[NOTA DE REDE]: Este bloco é virtual e opera apenas dentro")
        print(f"da máquina local. Os endereços seguem os limites da Classe A.{RESET}")
    print(f"{AZUL}[==============================================]{RESET}\n")

def analisar_ip(ip_string: str) -> None:
    relatorio = {
        "ipv4_address": ip_string,
        "ip_class": "",
        "mask": "",
        "mask_bin": "",
        "mask_func": "",
        "num_hosts": "",
        "first_host": "",
        "last_host": "",
        "network_address": "",
        "broadcast_address": ""
    }
    ip = ip_string.split(".")
    primeiro_octeto = int(ip[0])
    relatorio['ip_class'], relatorio['mask'], relatorio['mask_bin'], relatorio['mask_func'], relatorio['num_hosts'] = classificar(primeiro_octeto)
    relatorio['first_host'], relatorio['last_host'], relatorio['network_address'], relatorio['broadcast_address'] = calcular(ip, relatorio['ip_class'])
    exibir_relatorio(relatorio)