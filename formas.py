def circulo():
        raio = int(input("Qual o tamanho do raio? "))
        area = (raio * raio) * 3,14
        print(f"O valor da área do circulo é: {area}")
def triangulo():
        base = int(input("Qual o valor da base? "))
        altura = int(input("Qual o valor da altura? "))
        area = base * altura / 2
        print(f"O valor da área do Triângulo é: {area}")
def quadrado():
        base = int(input("Qual o valor da base? "))
        altura = int(input("Qual o valor da altura? "))
        area = base * altura
        print(f"O valor da área do Quadrado é: {area}")
def retangulo():
        base = int(input("Qual o valor da base? "))
        altura = int(input("Qual o valor da altura? "))
        area = base * altura
        print(f"O valor da área do Retângulo é: {area}")
def paralelogramo():
        base = int(input("Qual o valor da base? "))
        altura = int(input("Qual o valor da altura? "))
        area = base * altura
        print(f"O valor da área do Paralelogramo é: {area}")
def lozango():
        diagonal1 = int(input("Qual o valor da diagonal1? "))
        diagonal2 = int(input("Qual o valor da diagonal2? "))
        area = diagonal1 * diagonal2 / 2
        print(f"O valor da área do Lozango é: {area}")
def trapezio():
        basemaior = int(input("Qual o valor da base maior? "))
        basemenor = int(input("Qual o valor da base menor? "))
        altura = int(input("Qual o valor da altura? "))
        area = (basemaior + basemenor) * altura / 2
        print(f"O valor da área do Trapézio é: {area}")


while True:
    print("1 - Circulo")
    print("2 - Triângulo")
    print("3 - Quadrado")
    print("4 - Retângulo")
    print("5 - Paralelogramo")
    print("6 - Losango")
    print("7 - Trapézio")
    print("0 - Sair")
    menu = input("Qual forma geometrica você deseja caucular a aréa? ")
   
    if menu == "1":
        circulo()
    elif menu == "2":
        triangulo()
    elif menu == "3":
        quadrado()
    elif menu == "4":
        retangulo()
    elif menu == "5":
        paralelogramo()
    elif menu == "6":
        lozango()
    elif menu == "7":
        trapezio()
    elif menu == "0":
        print("Saindo do sistema!")
        break