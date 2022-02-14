def valida_senha():
    nome = input('Insira seu nome: ')
    senha = input('Insira sua senha: ')

    x = True

    while x:
        if nome.lower() == senha.lower():
            print('A senha não pode ser igual o nome!')
            senha = input('Insira sua senha: ')
            continue
        else:
            print('Ok!')
            break


valida_senha()
