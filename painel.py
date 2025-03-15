import os
import requests

# Definição de cores ANSI para personalização
verde = "\033[1;32m"
vermelho = "\033[1;31m"
azul = "\033[1;34m"
roxo = "\033[1;35m"
reset = "\033[0m"

# Arte ASCII Personalizada
ascii_art = f"""
{verde}
████████╗██╗  ██╗███████╗██████╗  █████╗ ██████╗  ██████╗ ██████╗ 
╚══██╔══╝██║  ██║██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝ ██╔══██╗
   ██║   ███████║█████╗  ██████╔╝███████║██║  ██║██║  ███╗██████╔╝
   ██║   ██╔══██║██╔══╝  ██╔═══╝ ██╔══██║██║  ██║██║   ██║██╔═══╝ 
   ██║   ██║  ██║███████╗██║     ██║  ██║██████╔╝╚██████╔╝██║     
   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝     
   
           {vermelho}By: IMPERADOR{reset}
"""

# Função para puxar informações de qualquer IP
def puxar_info_ip():
    ip = input(f"\n{azul}Digite o IP para consulta: {reset}")
    url = f"http://ip-api.com/json/{ip}?fields=status,message,country,regionName,city,zip,lat,lon,isp,org,as,query"

    try:
        response = requests.get(url)
        dados = response.json()

        if dados["status"] == "fail":
            print(f"\n{vermelho}[✖] Erro: {dados['message']}{reset}\n")
        else:
            print(f"""
{verde}🔍 IP Encontrado: {dados['query']}
🌎 País: {dados['country']}
🏙️  Região: {dados['regionName']}
🏢 Cidade: {dados['city']}
📍 CEP: {dados['zip']}
🛰️ Latitude: {dados['lat']}
🛰️ Longitude: {dados['lon']}
🔗 Provedor (ISP): {dados['isp']}
🏛️ Organização: {dados['org']}
📡 ASN: {dados['as']}
{reset}""")

    except:
        print(f"\n{vermelho}[✖] Erro ao puxar informações do IP.{reset}\n")

# Função para atualizar o Termux
def atualizar_termux():
    print(f"\n{roxo}[✔] Atualizando Termux...{reset}")
    os.system("apt update && apt upgrade -y")

# Função do menu principal
def menu():
    while True:
        os.system("clear")
        print(ascii_art)
        print(f"{verde}[ 1 ] Puxar informações de qualquer IP")
        print(f"{azul}[ 2 ] Atualizar Termux")
        print(f"{vermelho}[ 3 ] Sair")
        opcao = input(f"\n{reset}Escolha uma opção: ")

        if opcao == "1":
            puxar_info_ip()
        elif opcao == "2":
            atualizar_termux()
        elif opcao == "3":
            print(f"\n{vermelho}Saindo...{reset}")
            break
        else:
            print(f"\n{vermelho}[✖] Opção inválida!{reset}\n")

        input("\nPressione ENTER para continuar...")

# Executa o menu
menu()
