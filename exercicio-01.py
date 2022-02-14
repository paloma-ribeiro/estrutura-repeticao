def mostra_nota():
    nota = float(input("Insira uma nota de 0 a 10:"))
    while nota:
        if 0 <= nota <= 10:
            print('Nota:', nota)
            break
        else:
            print("Valor inválido!")
            nota = float(input("Insira uma nota de 0 a 10:"))
            continue


mostra_nota()
