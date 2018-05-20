import sys
import smtplib


def imprimirLinha():
    print("========================================")

def sinalEntrada():
    sys.stdout.write("-> ")
    sys.stdout.flush()

def enviarEmail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, senha)
 
    server.sendmail(email, emailAlvo, mensagem)
    server.quit()

def menu():
    print("[1] Configurar email e senha")
    print("[2] Configurar mensagem")
    print("[3] Configurar emails alvos")
    sinalEntrada()
    menuResp = input()
    imprimirLinha()

    if menuResp == 1:
        print("Digite seu email:")
        sinalEntrada()
        global email
        email = sys.stdin.readline()
        
        print("Digite sua senha: ")
        sinalEntrada()
        global senha
        senha = sys.stdin.readline()
        
        imprimirLinha()
        menu()
    
    if menuResp == 2:
        print("Digite a mensagem que deseja enviar")
        sinalEntrada()
        global mensagem
        mensagem = sys.stdin.readline()
        
        imprimirLinha()
        menu()

    if menuResp == 3:
        print("Digite um email que deseja enviar a mensagem cadastrada: ")
        sinalEntrada()
        global emailAlvo
        emailAlvo = sys.stdin.readline()

        imprimirLinha()
        enviarEmail()

        print("Deseja continuar? [S/n]")
        sinalEntrada()
        continuar = sys.stdin.read()
        imprimirLinha()

        if continuar == "s" or continuar == "S":
            menu()

def main():
    menu()

main()