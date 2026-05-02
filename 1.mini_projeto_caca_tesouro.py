import numpy as np

# Criando o mapa
mapa = np.random.randint(1,10,size=(5,5))

# Escondendo teosuro no mapa

while True:
    tesouro_linha, tesouro_coluna = np.random.randint(0,5, size=2)
    if (tesouro_linha, tesouro_coluna) != (0,0):
        break

# Definindo posição inicial e pontuação

posicao_jogador = (0,0)
pontuacao = 0

while True:
    mapa_com_jogador = np.copy(mapa)
    mapa_com_jogador[posicao_jogador] = 0
    print(mapa_com_jogador)

    #Escolhendo a movimentação através do input
    direcao = input('Digite a direcao que deseja se mover (cima, baixo, esquerda e direita)')
    if direcao == 'cima' or direcao == 'c':
        nova_posicao = (posicao_jogador[0]-1, posicao_jogador[1])
    elif direcao == 'baixo' or direcao == 'b':
        nova_posicao = (posicao_jogador[0]+1, posicao_jogador[1])
    elif direcao == 'esquerda' or direcao == 'e':
        nova_posicao = (posicao_jogador[0], posicao_jogador[1]-1)
    elif direcao == 'direita' or direcao == 'd':
        nova_posicao = (posicao_jogador[0], posicao_jogador[1]+1)

    # Checando se o movimento é válido

    if nova_posicao [0] < 0 or nova_posicao [0] >= mapa.shape[0] or nova_posicao[1] < 0 or nova_posicao [1] >= mapa.shape[0]:
        print('posição invalidada')
        continue

    posicao_jogador = nova_posicao
    pontuacao += 1

    if posicao_jogador == (tesouro_linha, tesouro_coluna):
        mapa_com_jogador = np.copy(mapa)
        mapa_com_jogador[posicao_jogador] = 0
        print(mapa_com_jogador)
        break

print('\n\n==== PARABÉNS====')
print(f'Sua pontuação final foi: {pontuacao}')
print(f'O tesouro estava em: {( tesouro_linha, tesouro_coluna,)}')


