import tkinter as tk

extrato = 0
depositos_feitos = 0
saques_feitos = 0

def depositar():
    global extrato, depositos_feitos

    user_1 = float(entry_valor.get())
    extrato += user_1
    depositos_feitos += 1
    label_resultado["text"] = f"Foram depositados R${user_1} na sua conta. Seu extrato agora é de R${extrato}"
    if depositos_feitos >= 3:
        label_resultado["text"] = "Limite de depósitos atingido, volte amanhã"

def sacar():
    global extrato, saques_feitos

    user_1 = float(entry_valor.get())
    if user_1 > extrato:
        label_resultado["text"] = f"Saldo indisponível, você possui R${extrato}"
    else:
        extrato -= user_1
        label_resultado["text"] = f"Você sacou R${user_1}, seu saldo atual é de R${extrato}"
        saques_feitos += 1
        if saques_feitos >= 3:
            label_resultado["text"] = "Limite de saques atingido"

def exibir_extrato():
    global extrato, depositos_feitos
    label_resultado["text"] = f"Seu saldo é de R${extrato} e foram realizados hoje {depositos_feitos} depósitos e {saques_feitos} saques feitos."

# Cria a janela principal
janela = tk.Tk()
janela.title("Sistema Bancário")

# Cria os widgets da interface
label_instrucao = tk.Label(janela, text="Bem-vindo ao banco. O que deseja fazer?")
label_valor = tk.Label(janela, text="Valor:")
entry_valor = tk.Entry(janela)
button_depositar = tk.Button(janela, text="Depositar", command=depositar)
button_sacar = tk.Button(janela, text="Sacar", command=sacar)
button_extrato = tk.Button(janela, text="Ver Extrato", command=exibir_extrato)
label_resultado = tk.Label(janela, text="")

# Posiciona os widgets na janela
label_instrucao.pack()
label_valor.pack()
entry_valor.pack()
button_depositar.pack()
button_sacar.pack()
button_extrato.pack()
label_resultado.pack()

# Inicia o loop de eventos da interface
janela.mainloop()
