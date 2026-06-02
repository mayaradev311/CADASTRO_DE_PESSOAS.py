import os

opcao = 0

while opcao != 5:
    print("=======MENU===========")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Sair do programa")

    opcao = int(input("Escolha uma opção: "))
    print("======================")

    if opcao == 1:
        nome = input("Digite o seu nome de usuário porfavor: ")
        telefone = input("Digite o seu número de telefone porfavor: ")
        email = input("Digite o seu email porfavor: ")

        arquivo = open("cad_pessoas.txt", "a")
        arquivo.write(f"{nome},{telefone},{email}\n")
        arquivo.close()


        print("Usuário cadastrado com sucesso!!")
        input()
        os.system("cls")

    elif opcao == 2:
        print("Listar pessoas")

        arquivo = open("pessoas.txt", "r")

        for linha in arquivo:
            nome, telefone, email = linha.strip().split(",")
            print(f"nome da pessoa: {nome}")
            print(f"telefone da pessoa: {telefone}")
            print(f"email da pessoa: {email}")
        arquivo.close()    
        input()
        os.system("cls")
