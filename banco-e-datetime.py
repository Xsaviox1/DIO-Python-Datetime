from datetime import *

opcao = ""
saque = 0
saldo = 0
deposito = 0
saques = []
depositos = []
LIMITE_TRANSACOES = 10
LIMITE_SAQUES = 3
VALOR_MAXIMO_SAQUE = 500
TAMANHO_MENU = 50
AGENCIA = "0001"
transacoes = 0
proximo_dia = ""
data_hoje = ""
usuario = {}

def perguntar_menu():
    opcao = input("Digite a opção desejada...\n")
    return opcao

def criar_conta_corrente():
    global usuario
    print("Vamos criar a sua conta corrente")
    cpf = input("Informe o seu CPF: ")
    if cpf not in usuario:
        print("CPF digitado incorretamente ou usuário não existe!")
        return
    numero = len(usuario[cpf]["contas"]) + 1
    nova_conta = {
        "numero":numero,
        "nome":usuario[cpf]["nome"]
    }
    usuario[cpf]['contas'].append(nova_conta)
    print(f"Conta {numero} criada para usuário {usuario[cpf]['nome']}")

def criar_usuario():
    global usuario
    print("Vamos criar seu usuário")
    cpf = input("Digite o seu CPF: ")
    if cpf.isdigit() == False:
        print("O CPF informado está em formado inválido, digite somente numeros")
        return
    if cpf in usuario:
        print("O CPF informado já esta sendo utilizado")
        return
    nome = input("Digite o seu nome completo: ")
    data_nasc = input("Digite a sua data de nascimento: ")
    endereco = input("Digite o seu endereço: ")
    usuario[cpf] = {
                    "nome": nome,
                    "data_nasc": data_nasc,
                    "endereco":endereco,
                    "contas": []
    }
    print("Usuário criado com sucesso!")

def listar_contas():
    cpf = input("Informe o seu CPF: ")
    if cpf not in usuario:
        print("CPF digitado incorretamente ou usuário não existe!")
        return
    for conta in usuario[cpf]['contas']:
        print(f"Agência: {AGENCIA} | Conta: {conta['numero']} | Nome: {conta['nome']}")
        print(f""" Agencia: {AGENCIA} """.center(TAMANHO_MENU,"_"))
        print(f""" Conta: {conta['numero']} """.center(TAMANHO_MENU,"_"))
        print(f""" Nome: {conta['nome']} """.center(TAMANHO_MENU,"_"))


def processar_menu():
    if(opcao.upper() == "SAIR"):
        print("Obrigado por usar o nosso banco :D")
    elif(opcao.upper() == "SACAR"):
        sacar()
    elif(opcao.upper() == "EXTRATO"):
        verificar_extrato()
    elif(opcao.upper() == "DEPOSITAR"):
        depositar() 
    elif(opcao.upper() == "CRIAR USUARIO"):
        criar_usuario()
    elif(opcao.upper() == "CRIAR CONTA CORRENTE"):
        criar_conta_corrente()
    elif(opcao.upper() == "LISTAR CONTAS"):
        listar_contas()
    else: 
        print("*opcao digitada incorretamente, tente novamente*\n")  
        return

def armazenar_saque():
    saques.append((saque,datetime.now(),))
    
def armazenar_deposito():
    depositos.append((deposito,datetime.now(),))

def sacar():
    global saque
    global saldo
    global transacoes

    if (transacoes >= LIMITE_TRANSACOES):
        print("O seu limite de transações chegou ao fim, volte amanhã")
        return

    if(len(saques) >= LIMITE_SAQUES):
        print("Os saques diarios disponiveis acabaram\n")
        return
    
    if saldo <= 0:
        print("Não há saldo disponivel em conta")
        return

    saque = input("Digite quanto você deseja sacar(limite de 3 saques de 500,00 R$):...\n")
    try:
        saque = float(saque)
    except:
        print(f"O valor '{saque}' não é um número!")
        return
    
    if(saque > saldo):
        print("Você não tem saldo suficiente para esta transação")
        return
    
    if(saque > 0 and saque <= VALOR_MAXIMO_SAQUE):
        saldo = saldo - saque
        armazenar_saque()
        transacoes += 1
        print(f"Saque de {saque:.2f} R$ realizado com sucesso\n")
        print(f"Transações restantes: {LIMITE_TRANSACOES - transacoes}")
        return saldo
    else:
        print("O limite para saque é de 500 R$, coloque um valor valido\n")
    
def fazer_extrato_saques():
    if (len(saques) > 0):
        print(f"Saques realizados:")
        for v, d in saques:
            print(f"Saque de {v:.2f} R$ realizado ás {d.strftime('%H:%M:%S')} do dia {d.strftime('%d/%m/%Y')} ")

def fazer_extrato_depositos():
    if (len(depositos) > 0):
        print(f"Depositos realizados:")
        for v, d in depositos:
            print(f"Deposito de {v:.2f} R$ realizado ás {d.strftime('%H:%M:%S')} do dia {d.strftime('%d/%m/%Y')} ")

def verificar_extrato():
    print(f"O seu saldo atual é de {saldo:.2f} R$\n")
    fazer_extrato_saques()
    fazer_extrato_depositos()
    print("\n")

def depositar():
    global saldo
    global deposito
    global transacoes
    if (transacoes >= LIMITE_TRANSACOES):
        print(f"O seu limite de transações chegou ao fim, aguarde 24 horas para novas transações")
        return
    
    deposito = input("Digite quanto você deseja depositar:\n")
    try:
        deposito = float(deposito)
    except:
        print(f"O valor '{deposito}' não é um número!")
        return
    if(deposito >= 0):
        saldo = saldo + deposito
        armazenar_deposito()
        transacoes += 1
        print(f"Deposito de {deposito:.2f} R$ realizado com sucesso\n")
        print(f"Transações restantes: {LIMITE_TRANSACOES - transacoes}")
        return saldo
    else:
        print("O valor fornecido é invalido\n")

def mostrar_menu():
    print(""" Bem vindo ao banco """.center(TAMANHO_MENU,"_"))
    print(""" Selecione a operacao desejada """.center(TAMANHO_MENU,"_"))
    print(""" Sacar """.center(TAMANHO_MENU,"-"))
    print(""" Depositar """.center(TAMANHO_MENU,"-"))
    print(""" Extrato """.center(TAMANHO_MENU,"-"))
    print(""" Criar usuario """.center(TAMANHO_MENU,"-"))
    print(""" Criar conta corrente """.center(TAMANHO_MENU,"-"))
    print(""" Listar contas """.center(TAMANHO_MENU,"-"))
    print(""" Sair """.center(TAMANHO_MENU,"-"))

def comparar_datas():
    global depositos
    global saques
    global transacoes
    global proximo_dia

    if not depositos and not saques:
        return

    data_hoje = datetime.now().date()

    data_primeiro_deposito = depositos[0][1].date()
    data_primeiro_saque = saques[0][1].date()

    data_mais_antiga = min(data_primeiro_deposito, data_primeiro_saque)
    proximo_dia = data_mais_antiga + timedelta(days=1)

    if data_hoje >= proximo_dia:
        depositos.clear()
        saques.clear()
        transacoes = 0
    


while(opcao.upper() != "SAIR"):
    comparar_datas()
    mostrar_menu()
    opcao = perguntar_menu()
    processar_menu()

