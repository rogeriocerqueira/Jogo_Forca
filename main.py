import random

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def escolhe_palavra():
   linhas = arquivo.readlines()
   linhas = linhas[random.randrange(1, len(linhas))]
   return linhas[:-1]

def esconde_palavra():
    palavra = escolhe_palavra()
    tracos = []

    for _ in palavra:
        tracos.append('_')
    return palavra, tracos

def verifica_jogo(acertos, erros, palavra):
    if acertos >= len(palavra) and erros != len(HANGMANPICS)-1:
        print('Parabens! Você ganhou o jogo')
    else:
        print('Game Over!')
        print('A palavra era: %s ' %(palavra))


def analisa_letra(escolha, lista): # Guarda as letras escolhidas pelo usuario em uma lista de valores

    for _ in lista:
        if escolha == _:
            return True, lista

    lista.append(escolha)
    return False, lista


def inicia_jogo():
    palavra, tracos = esconde_palavra()
    acertos, erros = 0, 0
    print(HANGMANPICS[0]) #imprime logo de inicio
    print(''.join(tracos))
    while (erros != len(HANGMANPICS)-1) and acertos < len(palavra):
        
        i = 0
        escolha = input('Digite uma letra: ').upper()
        
        if escolha in palavra:
            for _ in palavra: #Para não guardar a variável na memória

                if escolha in palavra[i]:
                    tracos[i] = _
                    acertos += 1
                i+=1

        else:
            erros +=1
            
       print(HANGMANPICS[erros])
       print(''.join(tracos))
        
    verifica_jogo(acertos, erros, palavra)

if __name__ == '__main__':
  resp = 'S'
  while resp == 'S':
    inicia_jogo()
    resp = input('Deseja continuar?').upper()
