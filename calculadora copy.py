while True:
    numero1 = input('Digite um numero: ')
    numero2 = input('Digite outro numero: ')
    operador = input('Digite um operador(+-/*): ')
    numeros_validos = None

    try:
        numero1_f = float(numero1)
        numero2_f = float(numero2)
        numeros_validos = True
    except: 
        numeros_validos = None

    if numeros_validos is None:
        print('Por favor, digite numeros validos!')
        continue

    operadores_perm = '-+*/'

    if operador not in operadores_perm:
        print('Operador invalido!')
    
    if len(operador) >1:
        print('Digite apenas um operador')
        continue

    if (numero1_f and numero2_f):
        if (operador == '+'):
            soma = numero1_f + numero2
            print(soma)
        elif(operador == '-'):
            menos = numero1_f - numero2_f
            print(menos)
        elif(operador == '*'):
            vezes = numero1_f * numero2_f
            print(vezes)
        elif(operador == '/'):
            div = numero1_f/numero2_f
            print(div)
        else:
            print('Voce nao digitou um numero correto')

    sair  =  input("Digite [s]air").lower().startswith('s')
    if sair is True:
        break
    
    

