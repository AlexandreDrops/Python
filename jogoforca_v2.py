# Projeto 1 - Desenvolvimento de um jogo da forca

# import
import random
from os import system, name
from time import sleep

# Função para limpar a tela a cada execução
def limpa_tela():
    # Windows
    if name == 'nt':
        _ = system('cls')

    # Mac ou Linux
    else:
        _ = system('clear')

# Função que desenha a forca na tela
def display_hangman(chances):
    # Lista de estágios da forca
    stages = [  # estágio 6 (final)
                """
                --------
                |      |
                |      O
                |     \\|/ 
                |      |
                |     / \\
                -
                """,
                # estágio 5
                """
                --------
                |      |
                |      O
                |     \\|/ 
                |      |
                |     / 
                -
                """,
                # estágio 4
                """
                --------
                |      |
                |      O
                |     \\|/ 
                |      |
                |      
                -
                """,
                # estágio 3
                """
                --------
                |      |
                |      O
                |     \\| 
                |      |
                |      
                -
                """,
                # estágio 2
                """
                --------
                |      |
                |      O
                |      |
                |      |
                |      
                -
                """,
                # estágio 1
                """
                --------
                |      |
                |      O
                |      
                |      
                |      
                -
                """,
                # estágio 0
                """
                --------
                |      |
                |      
                |      
                |      
                |      
                -
                """,

    ]
    return stages[chances]


# Função do jogo
def game():
    limpa_tela()


    # Lista de palavras para o jogo
    palavras = ['BANANA', 'UVA', 'ABACATE', 'MORANGO', 'LARANJA', 'MARACUJA', 'PERA']

    # EScolhe aleatoriamente uma palavra
    palavra = random.choice(palavras)

    # Lista de letras da palavra
    lista_letras_palavras = [letra for letra in palavra]

    # Cria o tabuleiro com o caracter "_" multiplicado pelo comprimento da palavra
    tabuleiro = ["_"] * len(palavra)

    # Número de chances
    chances = 6

    # Lista de letras digitadas
    letras_tentativas = []

    # Estrutura de repetição (Enquanto o numero de chances for maior que zero)
    while chances > 0:
        # Print
        limpa_tela()
        print("\nBem vindo ao jogo da forca!")
        print("Adivinhe a palavra abaixo: \n")

        print(display_hangman(chances))
        print("Palavra: ", tabuleiro)
        print("\nChances restantes:", chances)
        print("\nLetras já digitadas:", " ".join(letras_tentativas))
        print("\n")

        # Tentativa
        tentativa = input("\nDigite uma letra:").upper()

        # Condicional
        if tentativa in letras_tentativas:
            print("\nVocê ja tentou essa letra. Escolha outra!")
            sleep(1.1)
            continue

        letras_tentativas.append(tentativa)

        # Condicional
        if tentativa in lista_letras_palavras:

            print("\nVocê acertou a letra!")
            sleep(1.1)

            # Loop
            for indice in range(len(lista_letras_palavras)):
                
                # Condicional
                if lista_letras_palavras[indice] == tentativa:
                    tabuleiro[indice] = tentativa
                
            # Se todos os espaços forma preenchidos, o jogo acabou
            if "_" not in tabuleiro:
                print("\nVocê venceu!! A palavra era: {}.".format(palavra))
                break

        else:
            print("\nOps.. Essa letra não está na palavra!")
            sleep(1.1)
            chances -= 1
                
    # Condicional
    if "_" in tabuleiro:
        print("\nVocê perdeu. A palavra era: {}.".format(palavra))
  

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





    


