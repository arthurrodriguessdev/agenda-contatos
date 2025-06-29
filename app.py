contatos = {}
menu = True

#Definição de funções
def adicionarContatos():
    nome_contato = input("\nInforme o nome do novo contato: ")
    telefone_contato = input("Digite o número de telefone do contato: ")   

    contatos[nome_contato] = telefone_contato

    print("\nContato adicionado com sucesso!\n")
    
def listarContatos():
    c = 1
    print()
    for nome, telefone in contatos.items():
        print(c, '-', nome, ":", telefone)
        c += 1

    contato_selecionado = input("\nInforme o nome do contato que deseja exibir o número: ")
    
    if contato_selecionado in contatos:
        print("\nTelefone: ", contatos[contato_selecionado], "\n")
    else:
        print("\nContato não identificado!\n")

def atualizarContato():
    print("\n1 - Atualizar nome")
    print("2 - Atualizar número de telefone")

    try:
        opcao = input("\nInforme o que deseja editar: ")
        opcao = int(opcao)
    
    except ValueError:
        print("\nSomente número!\n")
        return
    
    if opcao == 1:
        j = 1

        for nome in contatos:
            print(j, '-', nome)
            j += 1

        contato_selecionado = input("\nDigite o nome do contato que será editado: ")

        if contato_selecionado in contatos:
            novo_nome_contato = input("\nDigite o novo nome do contato: ")
            contatos[novo_nome_contato] = contatos[contato_selecionado]
            del contatos[contato_selecionado]

            print("\nNome atualizado com sucesso!\n")

        else:
            print("\nContato não encontrado na lista!\n")

    elif opcao == 2:
        i = 1
        for nome, telefone in contatos.items():
            print(i, "-", nome, ":", telefone)
            i += 1

        contato_selecionado = input("Informe o nome correspondente ao número que será editado: ")
        
        if contato_selecionado in contatos:
            novo_telefone = input("Digite o novo número de telefone: ")
            contatos[contato_selecionado] = novo_telefone

            print("\nNúmero atualizado com sucesso!")

        else:
            print("\nContato não encontrado na lista!\n")

    else:
        print("\nOpção inválida!")

def removerContato():
    i = 1
    for nome, telefone in contatos.items():
        print(i, "-", nome, ":", telefone)
        i += 1
    
    selecionar_contato = input("\nInforme o nome do contato que deseja remover: ")

    if selecionar_contato in contatos:

        contatos.pop(selecionar_contato)

        print("\nContato removido com sucesso!\n")

    else:
        print("\nContato não encontrado na lista!\n")

def sairMenu():
    print("\nSESSÃO FINALIZADA!")

#Definição do menu e controle de fluxo
while menu:
    print("=== AGENDA DE CONTATOS ===")
    print()

    print("1 - Adicionar contatos")
    print("2 - Listar contatos")
    print("3 - Atualizar contato")
    print("4 - Remover contato")
    print("5 - Sair\n")

    try:
        opcao = input("Informe a opção desejada: ")
        opcao = int(opcao)
    except:
        print("\nDigite apenas números!\n")
        continue

    if opcao > 0 and opcao <= 5:
        if opcao == 1:
            adicionarContatos()
        elif opcao == 2:
            listarContatos()
        elif opcao == 3:
            atualizarContato()
        elif opcao == 4:
            removerContato()
        elif opcao == 5:
            sairMenu()
            break
    else:
        print("\nA opção digtada é inválida!\n")
        