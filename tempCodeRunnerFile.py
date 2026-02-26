import os
import unicodedata

usuarios = {
    "otavio": {"python", "games", "academia", "tecnologia"},
    "luigi": {"games", "futebol", "academia", "filmes"},
    "maria": {"python", "livros", "filmes", "arte"},
    "joao": {"games", "filmes", "tecnologia"},
    "ana": {"livros", "arte", "viagem"},
    "carlos": {"python", "tecnologia", "games"},
    "beatriz": {"filmes", "arte", "viagem", "fotografia"},
}

def similaridade(usuario1, usuario2):
    interesses_1 = set(usuarios[usuario1])
    interesses_2 = set(usuarios[usuario2])  

    uniao_interesses = 0
    intersecao_interesses = interesses_1 & interesses_2

    if not uniao_interesses:
        return 0

    return (len(intersecao_interesses) / len(uniao_interesses)) * 100

def melhor_recomendacao(usuario_alvo):
    maior_similaridade = -1
    melhor_usuario = None
    
    for outro_usuario in usuarios:
        if usuario_alvo != outro_usuario:
            valor = similaridade(usuario_alvo, outro_usuario)
            if valor > maior_similaridade:
                maior_similaridade = valor
                melhor_usuario = outro_usuario

    return f'{melhor_usuario} - {maior_similaridade:.2f}%\n'

def ranking(usuario_alvo):
    ranking_lista = []
    for outro_usuario in usuarios:
        if usuario_alvo != outro_usuario:
            valor = similaridade(usuario_alvo, outro_usuario)
            ranking_lista.append((outro_usuario, valor))
    ranking_lista_ordenado = sorted(ranking_lista, key=lambda x: x[1], reverse=True)
    print(f'Top 3 pessoas mais parecidas com {usuario_alvo}:')
    for i in range(min(3, len(ranking_lista_ordenado))):
        nome, valor = ranking_lista_ordenado[i]
        print(f'{i+1}º {nome} - {valor:.2f}%')
    print()

def ver_interesses(usuario_alvo):
    print(f'Interesses de {usuario_alvo}: ')
    for interesse in usuarios[usuario_alvo]:
        print(f'- {interesse}')
    print()

def exibir_usuarios():
    print('Usuários Disponíveis: ')
    for nome in usuarios:
        print(f'- {nome}')

def obter_usuario_existente(mensagem):
    while True:
        exibir_usuarios()
        nome = formatar_texto(input(mensagem))

        if nome in usuarios:
            limpar_tela()
            return nome
        
        limpar_tela()
        print('Usuário não encontrado!\n')

def obter_novo_usuario(mensagem):
    nome = formatar_texto(input(mensagem))

    if nome in usuarios:
        limpar_tela()
        print('Usuário já existe!\n')
        return None
    
    if not nome:
        limpar_tela()
        print('Usuário Inválido!\n')
        return None
    
    return nome

def formatar_texto(texto):
    texto = texto.strip().lower()
    texto = unicodedata.normalize('NFD', texto)
    texto = ''.join(c for c in texto if unicodedata.category(c) != 'Mn')
    return texto

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    print('''1 - Ver interesses de um usuário
2 - Ver similaridade entre dois usuários
3 - Ver melhor recomendação
4 - Ver ranking
5 - Adicionar novo usuário
6 - Adicionar interesse a um usuário
7 - Sair''')
    
    entrada_menu = input('Seleciona uma opção: ')

    if entrada_menu == '1':
        limpar_tela()
        usuario = obter_usuario_existente('Digite o usuário: ')
        ver_interesses(usuario)
        
    elif entrada_menu == '2':
        limpar_tela()
        usuario1 = obter_usuario_existente('Digite o nome do Usuário 1: ')
        usuario2 = obter_usuario_existente('Digite o nome do Usuário 2: ')

        if usuario1 == usuario2:
            print('Escolha dois usuários diferentes!\n')
            continue

        print(f'A similaridade entre {usuario1} e {usuario2} é de {similaridade(usuario1, usuario2):.2f}%\n')

    elif entrada_menu == '3':
        limpar_tela()
        usuario = obter_usuario_existente('Digite o nome do usuário: ')
        print(melhor_recomendacao(usuario))
        
    elif entrada_menu == '4':
        limpar_tela()
        usuario = obter_usuario_existente('Digite o nome do usuário: ')
        ranking(usuario)

    elif entrada_menu == '5':
        limpar_tela()
        usuario = obter_novo_usuario('Digite o nome do usuário para adicionar: ')
        if not usuario:
            continue

        usuarios[usuario] = set()
        print(f'{usuario} foi adicionado(a)!\n')
    
    elif entrada_menu == '6':
        limpar_tela()
        usuario = obter_usuario_existente('Digite o nome do usuário: ')
        interesse = formatar_texto(input('Digite o interesse: '))

        if not interesse:
            limpar_tela()
            print('Interesse inválido!\n')
            continue

        if interesse in usuarios[usuario]:
            limpar_tela()
            print('Esse interesse já existe para esse usuário!\n')
            continue

        usuarios[usuario].add(interesse)
        print('Interesse adicionado!')
    
    elif entrada_menu == '7':
        break

    else:
        limpar_tela()
        print('Opção inválida! Tente novamente!\n')