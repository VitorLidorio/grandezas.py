#Grandezas
opcao = 0
while (opcao != 5):
    print("***********") 
    print("Qual grandeza deseja calcular?")
    print("1 - Tensão em Volts")
    print("2 - Resistencia em Ohms")
    print("3 - Corrente em Ampéres")
    opcao = int(input("Escolha: "))
    if (opcao >= 1 and opcao <= 3):
        if (opcao == 1):
            r = float(input("Digite o valor da resistencia: "))
            i = float(input("Digite o valor da corrente: "))
            v = r*i
            print("A tensão é %.2f" %v, "Volts")
        elif (opcao == 2):
            v = float(input("Digite o valor da tensão: "))
            r = float(input("Digite o valor da resistencia: "))
            i = v/r
            print("A corrente é %2f" %i, "Ampéres")
        elif (opcao == 3):
            v = float(input("Digite o valor da tensão: "))
            i = float(input("Digite o valor da corrente: "))
            r = v/i
            print("A resistencia é %.2f" %r, "Ohms")
        elif (opcao >= 3):
            print("Opção invalida!")