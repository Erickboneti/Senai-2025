pessoas = []

# Funções de Cadastro
def nome_de_cadastro():
    while True:
        nome = input("\n★ Digite o nome: ").strip()

        if not nome:
            print("❗ Campo obrigatório! Digite um nome válido.")
        elif any(char.isdigit() for char in nome):
            print("❗ O nome não pode conter números.")
        else:
            return nome

def cpf_de_cadastro():
    while True:
        try:
            cpf = input("★ Digite o CPF (somente números): ").strip()
            cpf = cpf.replace('.', '').replace('-', '')

            if not cpf.isdigit():
                raise ValueError

            if len(cpf) != 11:
                print("❗ O CPF deve ter exatamente 11 dígitos.")
                continue

            if cpf == cpf[0] * 11:
                print("❗ O CPF não pode ter todos os números iguais.")
                continue

            return cpf
        except ValueError:
            print("❗ CPF inválido. Use apenas números.")

def email_de_cadastro():
    while True:
        email = input("★ Digite o email: ").strip()

        if not email:
            print("❗ O campo de e-mail não pode estar vazio.")
        elif '@' not in email or '.' not in email:
            print("❗ Email inválido. Certifique-se de que contém '@' e '.'")
        else:
            parte1 = email.split('@')
            if len(parte1) != 2 or not parte1[0]:
                print("❗ Email inválido: falta algo antes do '@'.")
            else:
                usuario, dominio = parte1
                dominio_partes = dominio.split('.')
                if len(dominio_partes) < 2 or not dominio_partes[0] or len(dominio_partes[-1]) < 2:
                    print("❗ Email inválido: formato incorreto.")
                else:
                    return email

def idade_de_cadastro():
    while True:
        try:
            idade = int(input("★ Digite a idade: "))
            if idade < 18:
                print("❗ Você não tem a idade mínima.")
            else:
                return idade
        except ValueError:
            print("❗ Digite sua idade em números.")

def peso_usuario():
    while True:
        try:
            peso = int(input("★ Digite o peso (kg): "))
            if peso < 46:
                print("❗ Você está abaixo do peso mínimo.")
            elif peso > 102:
                print("❗ Você está acima do peso máximo.")
            else:
                return peso
        except ValueError:
            print("❗ Digite seu peso apenas em números.")

def problema_fisico():
    while True:
        deficiencia = input("★ Possui problema físico (sim/não): ").strip().lower()
        if deficiencia not in ["sim", "não", "nao"]:
            print("❗ Responda apenas com 'sim' ou 'não'.")
        else:
            return deficiencia

def escolaridade():
    while True:
        print("\n📒 --- Nível de Escolaridade --- 📒")
        print("1 - Ensino Fundamental")
        print("2 - Ensino Médio")
        print("3 - Ensino Superior")
        try:
            opcao = int(input("★ Escolha uma opção: "))
            if opcao not in [1, 2, 3]:
                print("❗ Opção inválida.")
            else:
                return opcao
        except ValueError:
            print("❗ Digite apenas números.")

def interesse():
    while True:
        servir = input("★ Quer servir (sim/não): ").strip().lower()
        if servir not in ["sim", "não", "nao"]:
            print("❗ Responda apenas com 'sim' ou 'não'.")
        else:
            return servir

def historico():
    while True:
        passagem = input("★ Tem histórico policial (sim/não): ").strip().lower()
        if passagem not in ["sim", "não", "nao"]:
            print("❗ Responda apenas com 'sim' ou 'não'.")
        else:
            return passagem

# Função para cadastrar pessoa
def cadastro_pessoa():
    print("\n📋 --- Cadastro de Pessoa --- 📋")
    nome = nome_de_cadastro()
    cpf = cpf_de_cadastro()
    email = email_de_cadastro()
    idade = idade_de_cadastro()
    peso = peso_usuario()
    fisico = problema_fisico()
    estudo = escolaridade()
    vontade = interesse()
    passagem = historico()

    pessoa = {
        "nome": nome,
        "cpf": cpf,
        "email": email,
        "idade": idade,
        "peso": peso,
        "fisico": fisico,
        "estudo": estudo,
        "vontade": vontade,
        "passagem": passagem
    }
    pessoas.append(pessoa)
    print(f"\n✅ Pessoa cadastrada com sucesso: {nome}")

# Funções auxiliares
def nome_lista():
    print("\n📅 --- Lista de Pessoas --- 📅")
    if not pessoas:
        print("❗ Não há pessoas cadastradas.")
        return
    for i, pessoa in enumerate(pessoas):
        print(f"{i} - {pessoa['nome']}")

def formata_escolaridade(nivel):
    return ["Ensino Fundamental", "Ensino Médio", "Ensino Superior"][nivel - 1]

def vizualizar_dados():
    nome_lista()
    try:
        indice = int(input("\nDigite o número da pessoa para visualizar os dados: "))
        if not 0 <= indice < len(pessoas):
            print("❗ Código inválido.")
            return
        pessoa = pessoas[indice]
        print("\n📋 --- Dados da Pessoa --- 📋")
        for chave, valor in pessoa.items():
            print(f"★ {chave.capitalize()}: {valor}")
    except ValueError:
        print("❗ Digite apenas números.")

# Menu principal
def menu():
    print("\n==================================================")
    print("★ ★ ★ Bem-vindo ao Sistema de Recrutamento ★ ★ ★")
    print("==================================================")
    while True:
        print("\n1 - Cadastrar Pessoa")
        print("2 - Listar Pessoas")
        print("3 - Visualizar Dados")
        print("4 - Finalizar")
        try:
            opcao = int(input("\nEscolha uma opção: "))
            if opcao == 1:
                cadastro_pessoa()
            elif opcao == 2:
                nome_lista()
            elif opcao == 3:
                vizualizar_dados()
            elif opcao == 4:
                print("\n✅ Programa finalizado. Até logo!")
                break
            else:
                print("❗ Opção inválida.")
        except ValueError:
            print("❗ Digite apenas números.")

# Executa o programa
if __name__ == "__main__":
    menu()