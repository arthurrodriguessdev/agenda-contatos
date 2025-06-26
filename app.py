listaNome = []
listaContato = []
menu = True

#Definição de funções
def adicionarContatos():
    nome_contato = input("\nInforme o nome do novo contato: ")
    telefone_contato = input("Digite o número de telefone do contato: ")   

    listaNome.append(nome_contato)
    listaContato.append(telefone_contato)

    print("\nContato adicionado com sucesso!\n")
    
def listarContatos():
    c = 1
    for nome in listaNome:
        print(c, '-', nome)
        c += 1

    try:
        opcao = input("\nInforme o número equivalente ao contato que deseja exibir o número de contato: ")
        opcao = int(opcao)

    except ValueError:
        print("\nSomente número!\n")
        return
    
    if opcao >= 1 and opcao <= len(listaNome):
        print(f"\n{listaContato[opcao - 1]}\n")
    else:
        print("\nOpção inválida!\n")

def atualizarContato():
    print("1 - Atualizar nome")
    print("2 - Atualizar número de telefone")

    try:
        opcao = input("\nInforme o que deseja editar: ")
        opcao = int(opcao)
    
    except ValueError:
        print("\nSomente número!\n")
        return
    
    if opcao == 1:
        j = 1

        for nome in listaNome:
            print(j, '-', nome)
            j += 1

        try:
            opcao = input("\nInforme o número correspondente ao nome que será editado: ")
            opcao = int(opcao)

        except ValueError:
            print("\nSomente número!\n")
            return

        nome_contato = input("\nDigite o novo nome do contato: ")
        listaNome[opcao - 1] = nome_contato

        print("\nNome atualizado com sucesso!\n")

    elif opcao == 2:
        i = 1

        for contato in listaContato:
            print(i, '-', contato)
            i += 1

        try:
            opcao = int(opcao)
            opcao = input("Informe o número correspondente ao número que será editado: ")

        except ValueError:
            print("\nSomente número!\n")
            return
        
        telefone_contato = input("Digite o novo número de telefone: ")
        listaContato[opcao - 1] = telefone_contato

        print("\nNúmero atualizado com sucesso!")

    else:
        print("\nOpção inválida!")

def removerContato():
    i = 1
    for nome in listaNome:
        print(i,'-', nome)
        i += 1
    
    try:
        selecionar_contato = input("\nInforme o número do contato que deseja remover: ")
        selecionar_contato = int(selecionar_contato)

    except ValueError:
        print("\nSomente número!\n")
        return

    if selecionar_contato >= 1 and selecionar_contato <= len(listaContato):

        selecionar_contato = int(selecionar_contato)

        listaContato.pop(selecionar_contato - 1)
        listaNome.pop(selecionar_contato - 1)

        print("\nContato removido com sucesso!\n")

    else:
        print("\nOpção inválida!\n")

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
        