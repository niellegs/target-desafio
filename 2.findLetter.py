from traceback import print_tb

while True:
    sentence = str(input("Digite uma frase: ")).upper()
    count = sentence.count('A')

    if count > 0:
        print(f"Há {count} letras A na frase fornecida.")
    else:
        print("Não há nenhuma letra A na frase fornecida.")

    while True:
        toContinue = input("Quer continuar? [S/N] ").upper()
        if toContinue in 'SN':
            break
        else:
            print("Não consegui entender. Digite uma opção novamente.")
    if toContinue == 'N':
        break

