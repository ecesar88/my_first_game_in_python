# -*- coding: utf-8 -*-
############################## ESSE PROGRAMA É LICENCIADO SOB A LICENÇA GNU GPL 3.0 ##############################
import random
import math
import os
import time

# Declaração das variáveis globais
title = ' Medieval Knight ' # Título do programa

# Dicionários com todas as informações/variáveis do player e inimigos
player_info = {
	'inventario':{
		'corpo':{
			'cabeca':{
				'nome':{'Sem item equipado'},
				'estado':{0},
				'defesa':{0},
				},
			'peitoral':{
				'nome':{'Camisa de pano desgastada'},
				'estado':{20},
				'defesa':{5},
				},
			'calcas':{
				'nome':{'Calças de pano desgastadas'},
				'estado':{20},
				'defesa':{5},
				},
			'pes':{
				'nome':{'Chinelo de palha simples'},
				'estado':{5},
				'defesa':{5},
			},
		'armas':{
			'principal':{
				'nome':{'Adaga de aço enferrujado'},
				'estado':{10},
				'dano':{1},
				},
			'secundaria':{
				'nome':{'Sem item equipado'},
				'estado':{0},
				'dano':{0},
				},
			},
		'itens':{
			'vida':{
				'hp-potion-grande':{
					'life-buff':{40},
					'quantidade':{0},
					},
				'hp-potion-media':{
					'life-buff':{20},
					'quantidade':{0},
					},
				'hp-potion-pequena':{
					'life-buff':{10},
					'quantidade':{1},
					},
				},
			'stamina':{
				'stamina-potion-grande':{
					'stamina-buff':{40},
					'quantidade':{0},
					},
				'stamina-potion-media':{
					'stamina-buff':{20},
					'quantidade':{0},
					},
				'stamina-potion-pequena':{
					'stamina-buff':{10},
					'quantidade':{0},
					},
			},
			'magicka':{
				'magicka-potion-grande':{
					'magicka-buff':{40},
					'quantidade':{0},
					},
				'magicka-potion-media':{
					'magicka-buff':{20},
					'quantidade':{0},
					},
				'magicka-potion-pequena':{
					'magicka-buff':{10},
					'quantidade':{0},
					},
			},
			'comida':{
				'Pão mofado':{
					'estado':{30},
					'life-buff':{5},
						},
					},
				},
			},
		},

	'player_stats':{
		'vida':{100},
		'stamina':{100},
		'magicka':{50},
	},

	'player_perks':{
		'forca':{50},
		'agilidade':{50},
		'mago':{20},
		'guerreiro':{20},
		'arqueiro':{20},
	},
}
inimigos = {
	'general_redaniano':{
		'nome':{'General Redaniano'},
		'vida':{160},
		'dano':{15},
		'dano_critico':{20},
		'chance_critico':{5}, # x em 20 (math.random(0,20))
	},

	'soldado_redaniano':{
		'nome':{'Soldado Redaniano'},
		'vida':{100},
		'dano':{5},
		'dano_critico':{10},
		'chance_critico':{2}, # x em 20 (math.random(0,20))
	},

	'bandido_chefe':{
		'nome':{'Bandido Chefe'},
		'vida':{120},
		'dano':{15},
		'dano_critico':{17},
		'chance_critico':{4}, # x em 20 (math.random(0,20))
	},

	'bandido':{
		'nome':{'Bandido'},
		'vida':{100},
		'dano':{5},
		'dano_critico':{8},
		'chance_critico':{2}, # x em 20 (math.random(0,20))
	},

	'afogador':{
		'nome':{'Afogador'},
		'vida':{150},
		'dano':{5},
		'dano_critico':{8},
		'chance_critico':{3}, # 2 em 20 (math.random(0,20))
	},
}

####################################################################################
# Verifica o nome do sistema operacional e limpa o terminal/cmd de acordo
def init():
	""" Verifica o nome do sistema operacional e limpa o terminal/cmd de acordo """
	if os.name in('nt', 'me', 'ce'):
		os.system('cls')
		print(f'\nSO: Windows\n')
		print(f'{title.upper():#^50}')

	elif os.name == 'posix':
		os.system('clear')
		print(f'\nSO: Posix\n')
		print(f'{title.upper():#^50}')


# Inicializa o menu inicial e redireciona o fluxo do programa de acordo com a entrada do usuário
def menu_inicial():
	""" Inicializa o menu inicial e redireciona o fluxo do programa de acordo com a entrada do usuário """
	print('\n\t1 - NOVO JOGO\n\t2 - CARREGAR\n\t3 - CONFIGURAÇÕES\n\t4 - SAIR\n\t')
	tmp = str(input('\t >>> '))
	if tmp == '1':
		novo_jogo()
	elif tmp == '2':
		carregar_jogo()
	elif tmp == '3':
		configuracoes()
	elif tmp == '4':
		sair()
	else:
		init()
		print('\nOpção inválida, por favor, escolha uma opção válida.')
		time.sleep(1)
		menu_inicial()

# Define o sistema de combate para uso quando necessário
def sistema_combate(inimigos['']):
	""" Usa o dicionário player_stats para executar o sistema de combate """
	print(f'Você agora está em combate!')
	while True:
		print('O seu inimigo é um ' + )
	    print('\nAtacar?')
	    print('\t1 - SIM\n\t2 - NÃO')
	    attack = str(input('>>> '))
	    if attack == '1':
	        print('Atacando')
	        print(f'Você deu {player_info['inventario']['armas']['principal']['dano']} de dano no inimigo!')
	       # enemy['hp'] -= arma['dano']
	       # if enemy['hp']<= -1:
	       #     print()
	       # else:
	       #     print(enemy['hp'])
	       # if enemy['hp'] <= 0:
	       #     print('Parabéns! Você venceu!')
	       #     break
	    elif attack == '2':
	        print('Round do inimigo!')
	        print('O inimigo te deu 8 de dano!')
	        player['hp'] -= 8
	        print(f'O seu HP atual é: {player_info['player_stats']['vida']}')
	        if player_info['player_stats']['vida'] <= 0:
	            print('Oh não! Você morreu! :/')
	            print(f'GAME OVER')
	            break
	            init()
	    else:
	        print('Por favor, digite uma opção válida!')
	        continue


	




# Inicializa um novo jogo
def novo_jogo():
	""" Inicializa um novo jogo """
	print('Digite o seu nome: ')
	nome_player= str(input('>>> '))

	


# Carrega um arquivvo de savegame
def carregar_jogo():
	""" Carrega um arquivo de savegame """
	print('carregar jogo')


# Configura os parametros a serem usados no jogo (variaveis globais)
def configuracoes():
	""" Configura os parametros a serem usados no jogo (variaveis globais) """
	print('configuracoes')


# Encerra o jogo e volta para o terminal/cmd
def sair():	
	""" Encerra o jogo e volta para o terminal/cmd """
	print('Saindo...')
	time.sleep(2)
	init()
	exit(0)


if __name__ == '__main__':
	init()
	menu_inicial()

