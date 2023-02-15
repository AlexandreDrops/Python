# Projeto 1 - Desenvolvimento de um jogo da forca

# import
import random
from os import system, name

# Função para limpar a tela a cada execução
def limpa_tela():
    # Windows
    if name == 'nt':
        _ = system('cls')

    # Mac ou Linux
    else:
        _ = system('clear')

# Função
def game():
    limpa_tela()


    # Lista de palavras para o jogo
    palavras = ['BANANA', 'UVA', 'ABACATE', 'MORANGO', 'LARANJA', 'MARACUJA', 'PERA']

    # EScolhe aleatoriamente uma palavra
    palavra = random.choice(palavras)

    # List comprehension
    letras_descobertas = ['_' for letra in palavra]

    # Número de chances
    chances = 6

    # Lista de letras erradas
    letras_erradas = []

    # Estrutura de repetição (Enquanto o numero de chances for maior que zero)
    while chances > 0:
        # Print
        limpa_tela()
        print("\nBem vindo ao jogo da forca!")
        print("Adivinhe a palavra abaixo: \n")

        print(" ".join(letras_descobertas))
        print("\nChances restantes:", chances)
        print("Letras erradas:", " ".join(letras_erradas))

        # Tesntativa
        tentativa = input("\nDigite uma letra:").upper()

        # Condicional
        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)

        # Condicional
        if "_" not in letras_descobertas:
            print("\nVocê venceu!! A palavra era: ", palavra)
            break            

    # Condicional
    if "_" in letras_descobertas:
        print("\nVocê perdeu. A palavra era:", palavra)
        


   

# Bloco main
if __name__ == "__main__":
    game()
    execucao = True
    again = input("\nDeseja jogar novamente? (S/N): ").upper()
    while execucao:
        if again == "N":
            execucao = False
            exit("\nObrigado e até a próxima.")
        elif again == "S":
            game()
            again = input("\nDeseja jogar novamente? (S/N): ").upper()
        else:
            again = input("\nOpção inválida! \nDeseja jogar novamente? (S/N): ").upper()





    









