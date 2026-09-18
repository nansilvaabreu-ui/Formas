lista = ["Pão", "Frango", "Leite"]

def mostrar():
    print({lista})
def cadastrar():
    produto = str(input("Cadastre o produto: "))
    lista.append(produto)
    print(f"{produto} adicionado a lista!")
    print(lista)
def Excluir():
    produto = str(input("Qual item deseja remover da lista? "))
    lista.remove(produto)
    print(f"{produto} removido da lista!")
    print(lista)
def modificar():
    produto = int(input("Qual produto deseja modificar? "))
    modif = str(input("Por qual item deseja trocar? "))
    lista[produto] = modif
    print(f"{produto} foi trocado por {modif}!")
    print(lista)

while True:

    print("Lista de Compras")
    print("1 - Mostrar lista")
    print("2 - Cadastrar item")
    print("3 - Excluir item")
    print("4 - Modificar item")
    print("0 - Sair")

    opcao = int(input("Escolha a opção."))

    if opcao == 1:
        mostrar()
    elif opcao == 2:
        cadastrar()
    elif opcao == 3:
        Excluir()
    elif opcao == 4:
        modificar()
    elif opcao == 0:
        print("Saindo do sistema...")
        break

 


