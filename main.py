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
    if usuario1 in usuarios and usuario2 in usuarios:
        interesses_1 = set(usuarios[usuario1])
        interesses_2 = set(usuarios[usuario2])  

        uniao_interesses = interesses_1 | interesses_2
        intersecao_interesses = interesses_1 & interesses_2
        porcentagem_similaridade = ((len(intersecao_interesses) / len(uniao_interesses)) * 100)
        return porcentagem_similaridade
    else:
        print('Selecione usuários válidos')

def melhor_recomendacao(usuario_alvo):
    maior_similaridade = -1
    melhor_usuario = None
    
    for outro_usuario in usuarios:
        if usuario_alvo != outro_usuario:
            valor = similaridade(usuario_alvo, outro_usuario)
            if valor > maior_similaridade:
                maior_similaridade = valor
                melhor_usuario = outro_usuario

    return melhor_usuario, maior_similaridade

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

def ver_interesses(usuario_alvo):
    print(usuarios[usuario_alvo])

def exibir_usuarios():
    print('Usuários Disponíveis: ')
    for nome in usuarios:
        print(f'- {nome}')

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
        exibir_usuarios()
        usuario = input('Digite o nome do usuário: ')
        ver_interesses(usuario)
        
    elif entrada_menu == '2':
        exibir_usuarios()
        usuario1 = input('Digite o nome do Usuário 1: ')
        usuario2 = input('Digite o nome do Usuário 2: ')
        print(similaridade(usuario1, usuario2))

    elif entrada_menu == '3':
        exibir_usuarios()
        usuario = input('Digite o nome do usuário: ')
        print(melhor_recomendacao(usuario))
        
    elif entrada_menu == '4':
        exibir_usuarios()
        usuario = input('Digite o nome do usuário: ')
        ranking(usuario)