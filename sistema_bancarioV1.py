# Desafio de código: Sistema bancário simples

menu = '''
================================================

    Bem-vindo ao sistema bancário V:1.0.0
             Selecione uma opção:
[1] Depositar  [2] Sacar  [3] Extrato  [4] Sair

================================================
 '''
dinheiro_total = 0.0
numero_de_saques = 0
limite= 500.0
LIMITE_SAQUES = 3


while True:
    opcao = input(menu)
    if opcao == '1':
        valor = float(input('Digite o valor a ser depositado:'))
        if valor > 0:
            dinheiro_total += valor
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso!')
        else:
            print('Valor inválido! O depósito deve ser maior que zero.')
    elif opcao == '2':
        valor = float(input('Digite o valor a ser sacado:'))
        
        excedeu_saldo = valor  > dinheiro_total
        excedeu_limite = valor > limite
        excedeu_saques = numero_de_saques >= LIMITE_SAQUES
        if excedeu_saldo:
            print('Saldo insuficiente para saque!')
        elif excedeu_limite:
            print(f'O valor do saque não pode ser maior que R$ {limite:.2f}!')
        elif excedeu_saques:
            print('Número máximo de saques atingido!')
        elif valor > 0:
            dinheiro_total -= valor
            numero_de_saques += 1
            print(f'Saque de R$ {valor:.2f} realizado com sucesso!')
        else:
            print('Valor inválido! O saque deve ser maior que zero.')
    elif opcao =='3':
        print(f'Saldo atual: R$ {dinheiro_total:.2f}')
        print(f'Número de saques realizados: {numero_de_saques}')
        if numero_de_saques == 0:
            print ('Nenhum saque realizado até o momento.')   
        
    elif opcao == '4':
        print('Saindo...')
        break
    else:
        print('Opção inválida! Por favor, selecione uma opção válida.')
