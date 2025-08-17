
# Kodland Teste Para Tutor
Este é um jogo de aventura 2D com visão de cima (top-down), desenvolvido em Python com a biblioteca Pygame Zero. O projeto foi construído passo a passo, implementando funcionalidades essenciais de um jogo, desde o menu inicial até a interação com inimigos.
![Screenshot do projeto](tela_inicial.jpg?width=50)
![Screenshot do projeto](jogo.jpg?width=50)
## Tecnologias Utilizadas
Python 3 A linguagem de programação base do projeto
Pygame Zero (pgzrun) Um framework amigável para iniciantes construído sobre o Pygame que simplifica o desenvolvimento de jogos
Pygame A biblioteca multimídia subjacente que o Pygame Zero utiliza Usamos especificamente o módulo pygame Rect para a criação de botões e colisões
Módulo random Módulo padrão do Python utilizado para a geração aleatória de inimigos no mapa
## Guia Passo a Passo para Instalar as Dependências do jogo
### Passo 1: Abra o Terminal
Primeiro, você precisa de uma interface de linha de comando.

No Windows: Procure por "Prompt de Comando" (CMD) ou "PowerShell" no menu Iniciar.

No macOS ou Linux: Procure por "Terminal".
### passo 2: Navegue até a Pasta do Seu Projeto
```
# Exemplo para Windows
cd Desktop\Kodland_Teste_Tutor

# Exemplo para macOS/Linux
cd Desktop/Kodland_Teste_Tutor

```
### Passo 3: Crie e Ative um Ambiente Virtual (Venv)
Não esqueça de ativar o ambiente virtual quando for rodar o jogo em seu computador
```
python -m venv venv

venv\Scripts\activate -> Windows

source venv/bin/activate -> macOS ou Linux
```
### Passo 4: Instale as Dependências
Agora que seu ambiente está ativo, execute o comando mágico. Ele vai ler o arquivo requirements.txt e instalar todas as bibliotecas listadas nele.
```
pip install -r requirements.txt
```

## Estrtura de Pasta
Estrutura do Projeto
Para que o jogo funcione corretamente, os arquivos devem seguir esta estrutura:
```bash
start/
├── intro.py            
├── README.md           
├── requirements.txt    
├── images/             
│   ├── personagem/
│   │   └── persona_0087.png
│   ├── moobs/
│   │   └── persona_0084.png ...
│   ├── itens/
│   │   └── axe_0118.png ...
│   └── tiles/
│       └── tile_0000.png ...
├── sounds/             
│   ├── ataque.ogg
│   └── move_run.ogg
└── music/              
    └── song.mp3
´´´

