#Calculadora
opcao = 0
n1 = 0
n2 = 0
while opcao != '5':
    print('selecione o número da operação da calculadora: 1-soma 2-subtração 3-multiplicação 4-divisão 5-sair')
    opcao = input()
    
    #Condição de parada
    if opcao == '5':
        break
    
    n1 = input('entre com o primeiro numero:')
    n2 = input('entre com o segundo numero:')
    n1 = float(n1)
    n2 = float(n2)
    
    if opcao == '1':
        soma = 0
        soma = n1+n2
        print(soma)
    
    elif opcao == '2':
        sub = 0
        sub = n1-n2
        print(sub)
        
    elif opcao == '3':
        mult = 0
        mult = n1*n2
        print(mult)
        
    elif opcao == '4':
        div = 0
        div = n1/n2
        print(div)
