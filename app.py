'''
Crie um app de compras de ingressos para o cinema. 
O programa irá receber (uma única vez) o nome e a idade do usuário, e em seguida, o programa exibe uma lista de filmes, 
suas salas e suas respectivas classificações indicativas (idade mínima para ver o fime). 
O usuário deverá escolher a sala do filme desejado e o programa deverá informar se o usuário tem idade para ver o filme ou não. 
Caso tenha a idade mínima para ver o filme, o programa irá imprimir o ingresso seguida da mensagem "Bom filme!". 
Caso o usuário não tenha a idade mínima para ver o filme, 
o programa irá impedir a entrada do usuário e iá re-exibir a lista de filmes para ele escolher outro.
'''

nome = input("Informe o nome: ")
idade = int(input("Infome a idade: "))

while True:
    print("Sala 1 - Roda quadrada - Livre")
    print("Sala 2 - A volta dos que não foram - 14 anos")
    print("Sala 3 - Um dois três quatro, o filme do sapato - 15")
    print("Sala 4 - Racombole - 16 anos")
    print("Sala 5 - Esqueceram de mim - 18 anos")

    sala = input("Informe a sala desejada: ")
 
    match sala:
        case "1":
            idade_minima = 0 
        case "2":
            idade_minima = 14 
        case "3":
            idade_minima = 15
        case "4":
            idade_minima = 16
        case "5":
            idade_minima = 18
        # default (valor inválido)
        case _:
            print("Sala inexistente")
            continue

    # verifica a idade do usuário e a idade do filme

    if idade >= idade_minima:
        print(f"Entrada de {nome} autorizada. Tenha uma bom filme.")
        break

    else:
        print("Favor, escolher outro filme.")
        continue