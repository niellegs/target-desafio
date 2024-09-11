init = 0
pastValue1 = 1
pastValue2 = 0

while True:

    isFibonacci = int(input("Escolha um número: "))


    while (init < isFibonacci):

        pastValue2 = pastValue1
        pastValue1 = init
        init = pastValue1 + pastValue2

        if init != isFibonacci:
            print(f"\033[0;31m{init}\033[0m ", end="")
        else:
            print(f"\033[0;32m{init}\033[0m ", end="")

    if init == isFibonacci:
        print(f"\nO número {isFibonacci} pertence a sequência de Fibonacci.")
    else:
        print(f"\nO número {isFibonacci} não pertence a sequência de Fibonacci.")

    while True:
        toContinue = input("Quer continuar? [S/N] ").upper()
        if toContinue in 'SN':
            break
        else:
            print("Não consegui entender. Digite uma opção novamente.")
    if toContinue == 'S':
        init = 0
        pastValue1 = 1
        pastValue2 = 0
    else:
         break