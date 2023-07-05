extrato = 0
depositos_feitos = 0
saques_feitos = 0

def depositar(): # Aqui o usuario deposita dinheiro
    global extrato, depositos_feitos, saques_feitos

    user_1 = float(input("Digite quanto deseja depositar.\n: ")) # O usuario fala o valor, logo após ele é adicionado ao extrato e começa a contação dos depositos.
    extrato += user_1
    depositos_feitos += 1
    print(f"Foram depositados R${user_1} na sua conta, seu extrato agora é de R${extrato}")
    user_2 = input("Deseja depositar novamente?\n(1) Sim\n(2) Não\n: ") # Aqui pergunta se o usuario quer fazer o deposito novamente.
   
    if depositos_feitos >= 3: # Caso o limite de depositos seja feito ele é impedido e o dinheiro não é depositado.
        print("Limite de depósitos atingido, volte amanhã") 
        return menu()
    if user_2 == '1': # Aqui é caso ele vá executar dois depositos seguidos
        depositar()
        depositos_feitos += 1
    elif user_2 == '2': # Aqui é caso o usuario não queria mais depositar 
        print("Ok, o que deseja fazer agora?")
        menu()

def sacar(): # Aqui o usuario saca o dinheiro
    global extrato, saques_feitos

    user_1 = float(input("Quanto deseja sacar?\n: ")) # Aqui o usuario digita quanto quer sacar
    if saques_feitos == 3: 
        print("Limite de saques atingido")
        return menu()
    if user_1 > extrato:
        print(f"Saldo indisponível, você possui {extrato}")
        user_2 = float(input("Deseja sacar novamente?\n(1) Sim\n(2) Não\n: "))
        if user_2 == 2:
            return menu() 
        else:
            return sacar()

    if user_1 < extrato:
        saques_feitos+=1
        print(saques_feitos)
        extrato -= user_1
        print(f"Você sacou {user_1}, seu saldo atual é {extrato}")
        user_2 = float(input("Deseja sacar novamente?\n(1) Sim\n(2) Não\n: "))
        if user_2 == 1:
            return sacar()
        else:
            return menu()



def menu():
    while True:
        user = input("Bem vindo ao banco, o que deseja fazer?\n(1) Sacar\n(2) Depositar\n(3) Ver Extrato\n: ")
        if user == '2':
            depositar()
        if user == '3':
            print(f"Seu saldo é de R${extrato} e foram realizados hoje\n{depositos_feitos} depósitos.\n{saques_feitos} saques")
        if user == '1':
            sacar()



menu()
