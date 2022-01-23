def run():
    # for contador in range(1000):
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)

    # for i in range(10000):
    #     print(i)
    #     if i == 5678:
    #         break

    # texto = input('Escribe un texto: ')
    # for letra in texto:
    #     if letra == 'o':
    #         break
    #     print(letra)

    numero = int(input('Escribe un numero entre el 21 y el 100: '))
    while numero > 10:
        numero -= 1
        if numero % 2 != 0:
            continue
        print(numero)
        if numero == 20:
            break


if __name__ == '__main__':
    run()
