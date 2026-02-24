# 👥 Sistema de Recomendação por Afinidade

Um sistema interativo em Python que calcula a similaridade entre usuários com base em seus interesses, utilizando lógica de conjuntos (Teoria dos Conjuntos).

## 🚀 Funcionalidades

- **Cálculo de Similaridade:** Compara dois usuários e retorna a porcentagem de afinidade.
- **Ranking de Afinidade:** Exibe o Top 3 pessoas mais parecidas com o usuário alvo.
- **Sugestão Inteligente:** Identifica automaticamente o usuário com maior compatibilidade.
- **Gestão Dinâmica:** Permite adicionar novos usuários e novos interesses em tempo real.
- **Normalização de Dados:** Tratamento de strings para ignorar acentos e letras maiúsculas/minúsculas.

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Biblioteca `unicodedata`**: Para normalização de caracteres Unicode.
- **Biblioteca `os`**: Para manipulação da interface do terminal.

## 🧠 Lógica Técnica

O coração do projeto é a função de similaridade, que utiliza a lógica de **Interseção sobre União**:

$$\text{Similaridade} = \left( \frac{\text{Interseção dos Interesses}}{\text{União dos Interesses}} \right) \times 100$$

Isso garante que o cálculo seja preciso, independentemente da quantidade de interesses que cada usuário possui.

## 📦 Como Executar

1. Certifique-se de ter o Python instalado.
2. Clone o repositório:
   ```bash
   git clone [https://github.com/otaviosrb/friends-recommendations.git](https://github.com/otaviosrb/friends-recommendations.git)