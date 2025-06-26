print("=== AGENDA DE CONTATOS ===")
print()

print("1 - Adicionar contatos")
print("2 - Listar contatos")
print("3 - Buscar contato")
print("4 - Atualizar telefone")
print("5 - Remover contato")
print("6 - Sair\n")

opcao = input("Informe a opção desejada: ")
opcao = int(opcao)

listaNome = []
listaContato = []

#Definição de funções
def adicionarContatos():
    nome_contato = input("\nInforme o nome do novo contato: ")
    telefone_contato = input("Digite o número de telefone do contato: ")   

    listaNome.append(nome_contato)
    listaContato.append(telefone_contato)

    print("\nContato adicionado com sucesso!")
    
def removerContato():
    i = 1
    for nome in listaNome:
        print(i,'-', nome)
        i += 1
    
    selecionar_contato = input("\nInforme o número do contato que deseja remover: ")
    selecionar_contato = int(selecionar_contato)

    listaContato.pop(selecionar_contato - 1)
    listaNome.pop(selecionar_contato - 1)

    print("Contato removido com sucesso!")

def listarContatos():
    






if opcao > 0 and opcao <= 6:
    if opcao == 1:
        adicionarContatos()
    elif opcao == 2:
        ...
    elif opcao == 3:
        ...
    elif opcao == 4:
        ...
    elif opcao == 5:
        removerContato()
else:
    print("\nA opção digtada é inválida!")