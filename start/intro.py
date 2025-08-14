
import pgzrun
from pygame import Rect

# --- CONFIGURAÇÕES GERAIS ---
WIDTH = 800
HEIGHT = 700
TILE_SIZE = 16
PLAYER_SPEED = 120 # pixels por segundo

# --- CALCULOS DO MAPA ---
MAP_WIDTH_IN_TILES = WIDTH // TILE_SIZE
MAP_HEIGHT_IN_TILES = HEIGHT // TILE_SIZE + 1

# --- MAPEAMENTO DOS TILES ---
TILE_MAPPING = {
    0: 'images/tiles/tile_0000',
    1: 'images/tiles/tile_0001',
    2: 'images/tiles/tile_0002',
    3: 'images/tiles/tile_0003',
    4: 'images/tiles/tile_0004',
    5: 'images/tiles/tile_0005',
    6: 'images/tiles/tile_0006',
    7: 'images/tiles/tile_0007',
    8: 'images/tiles/tile_0008',
    9: 'images/tiles/tile_0009',
    10:'images/tiles/tile_0010',
    11:'images/tiles/tile_0011',
    12:'images/tiles/tile_0012',
    13:'images/tiles/tile_0013',
    14:'images/tiles/tile_0014',
    15:'images/tiles/tile_0015',
    16:'images/tiles/tile_0016',
    17:'images/tiles/tile_0017',
    18:'images/tiles/tile_0018',
    19:'images/tiles/tile_0019',
    20:'images/tiles/tile_0020',
    21:'images/tiles/tile_0021',
    22:'images/tiles/tile_0022',
    23:'images/tiles/tile_0023',
    24:'images/tiles/tile_0024',
    25:'images/tiles/tile_0025',
    26:'images/tiles/tile_0026',
    27:'images/tiles/tile_0027',
    28:'images/tiles/tile_0028',
    29:'images/tiles/tile_0029',
    30:'images/tiles/tile_0030',
    31:'images/tiles/tile_0031',
    32:'images/tiles/tile_0032',
    33:'images/tiles/tile_0033',
    34:'images/tiles/tile_0034',
    35:'images/tiles/tile_0035',
    36:'images/tiles/tile_0036',
    37:'images/tiles/tile_0037',
    38:'images/tiles/tile_0038',
    39:'images/tiles/tile_0039',
    40:'images/tiles/tile_0040',
    41:'images/tiles/tile_0041',
    42:'images/tiles/tile_0042',
    43:'images/tiles/tile_0043',
    44:'images/tiles/tile_0044',
    45:'images/tiles/tile_0045',
    46:'images/tiles/tile_0046',
    47:'images/tiles/tile_0047',
    48:'images/tiles/tile_0048',
    49:'images/tiles/tile_0049',
    50:'images/tiles/tile_0050',
    51:'images/tiles/tile_0051',
    52:'images/tiles/tile_0052',
    53:'images/tiles/tile_0053',
    54:'images/tiles/tile_0054',
    55:'images/tiles/tile_0055',
    56:'images/tiles/tile_0056',
    57:'images/tiles/tile_0057',
    58:'images/tiles/tile_0058',
    59:'images/tiles/tile_0059',
    60:'images/tiles/tile_0060',
    61:'images/tiles/tile_0061',
    62:'images/tiles/tile_0062',
    63:'images/tiles/tile_0063',
    64:'images/tiles/tile_0064',
    65:'images/tiles/tile_0065',
    66:'images/tiles/tile_0066',
    67:'images/tiles/tile_0067',
    68:'images/tiles/tile_0068',
    69:'images/tiles/tile_0069',
    70:'images/tiles/tile_0070',
    71:'images/tiles/tile_0071',
    72:'images/tiles/tile_0072',
    73:'images/tiles/tile_0073',
    74:'images/tiles/tile_0074',
    75:'images/tiles/tile_0075',
    76:'images/tiles/tile_0076',
    77:'images/tiles/tile_0077',
    78:'images/tiles/tile_0078',
    79:'images/tiles/tile_0079',
    80:'images/tiles/tile_0080',
    81:'images/tiles/tile_0081',
    82:'images/tiles/tile_0082',
    83:'images/tiles/tile_0083',
    84:'images/tiles/tile_0084',
    85:'images/tiles/tile_0085',
    86:'images/tiles/tile_0086',
    87:'images/tiles/tile_0087',
    88:'images/tiles/tile_0088',
    89:'images/tiles/tile_0089',
    90:'images/tiles/tile_0090',
    91:'images/tiles/tile_0091',
    92:'images/tiles/tile_0092',
    93:'images/tiles/tile_0093',
    94:'images/tiles/tile_0094',
    95:'images/tiles/tile_0095',
    96:'images/tiles/tile_0096',
    97:'images/tiles/tile_0097',
    98:'images/tiles/tile_0098',
    99:'images/tiles/tile_0099',
    100: 'images/tiles/tile_0100',
    101: 'images/tiles/tile_0101',
    102: 'images/tiles/tile_0102',
    103: 'images/tiles/tile_0103',
    104: 'images/tiles/tile_0104',
    105: 'images/tiles/tile_0105',
    106: 'images/tiles/tile_0106',
    107: 'images/tiles/tile_0107',
    108: 'images/tiles/tile_0108',
    109: 'images/tiles/tile_0109',
    110: 'images/tiles/tile_0110',
    111: 'images/tiles/tile_0111',
    112: 'images/tiles/tile_0112',
    113: 'images/tiles/tile_0113',
    114: 'images/tiles/tile_0114',
    115: 'images/tiles/tile_0115',
    116: 'images/tiles/tile_0116',
    117: 'images/tiles/tile_0117',
    118: 'images/tiles/tile_0118',
    119: 'images/tiles/tile_0119',
    120: 'images/tiles/tile_0120',
    121: 'images/tiles/tile_0121',
    122: 'images/tiles/tile_0122',
    123: 'images/tiles/tile_0123',
    124: 'images/tiles/tile_0124',
    125: 'images/tiles/tile_0125',
    126: 'images/tiles/tile_0126',
    127: 'images/tiles/tile_0127',
    128: 'images/tiles/tile_0128',
    129: 'images/tiles/tile_0129',
    130: 'images/tiles/tile_0130',
    131: 'images/tiles/tile_0131',
}
# Este loop preenche o dicionário automaticamente.
# Ele espera que seus arquivos estejam em 'images/tiles/'.
for i in range(132):
    TILE_MAPPING[i] = f'tiles/tile_{i:04d}'

# --- CONFIGURACOES DE ATAQUE ---
is_attacking = False        # O jogador esta atacando agora? Comeca como Falso.
attack_timer = 0.0          # Cronometro para a duracao da animacao de ataque.
ATTACK_DURATION = 0.3      # Duracao do ataque em segundos (ajuste para ficar mais rapido ou lento).
attack_cooldown = 0.0       # Cronometro para o intervalo entre ataques.
ATTACK_COOLDOWN_TIME = 0.5  # Intervalo minimo entre um ataque e outro.
ATTACK_THRUST = 25          # Quantos pixels a arma avanca durante o ataque.
SWING_START_ANGLE = -50  # Angulo inicial do ataque
SWING_END_ANGLE = 90     # Angulo final do ataque


# --- CRIAÇÃO DAS CAMADAS DO MAPA ---
# 1. Criamos os mapas GRANDES, do tamanho da tela.
CHAO_LAYOUT = [[0 for _ in range(MAP_WIDTH_IN_TILES)] for _ in range(MAP_HEIGHT_IN_TILES)]
ESTRUTURAS_LAYOUT = [[-1 for _ in range(MAP_WIDTH_IN_TILES)] for _ in range(MAP_HEIGHT_IN_TILES)]

# 2. Agora, modificamos o mapa GRANDE para adicionar a casa.

# ESTRUTURAS_LAYOUT[5][5] = 80
# ESTRUTURAS_LAYOUT[5][6] = 81
# ESTRUTURAS_LAYOUT[5][7] = 82
# ESTRUTURAS_LAYOUT[6][5] = 100
# ESTRUTURAS_LAYOUT[6][6] = 101
player = Actor('moobs/persona_0087', anchor=('center', 'bottom'))

# 3. Definimos a posicao inicial do personagem na tela (x, y).
player.pos = (100, 200)
arma = Actor('itens/axe_0118', anchor=('center', 'top'))
player_direction = 'frente'
ARMA_OFFSETS = {
    'frente': (15, 5),   # (dx, dy) a partir do centro do personagem
    'costas': (15, -10),
    'direita': (10, -5),
    'esquerda': (-10, -5)
}
# --- ESTADO DO JOGO E MENU ---
game_state = "menu"
sound_on = False

button_width = 250
button_height = 60
button_spacing = 30
total_height = 3 * button_height + 2 * button_spacing
start_y = (HEIGHT // 2) - (total_height // 2)


buttons = [
    {
        # NOS embrulhamos a tupla (x, y, w, h) com a função Rect()
        "rect": Rect(
            (WIDTH // 2 - button_width // 2, start_y + i * (button_height + button_spacing)),
            (button_width, button_height)
        ),
        "text": txt
    }
    for i, txt in enumerate(["Iniciar Jogo", "Som: Ligado", "Sair"])
]
def draw_layer(layout):
    for row_index, row in enumerate(layout):
        for col_index, tile_id in enumerate(row):
            if tile_id != -1:
                x_pos = col_index * TILE_SIZE
                y_pos = row_index * TILE_SIZE
                image_name = TILE_MAPPING.get(tile_id)
                if image_name:
                    screen.blit(image_name, (x_pos, y_pos))

def draw_game():
    draw_layer(CHAO_LAYOUT)
    draw_layer(ESTRUTURAS_LAYOUT)
    player.draw()
    arma.draw()

def draw_menu():
    screen.fill((255, 255, 255))
    screen.draw.text(
        "Kodlandia",
        center=(WIDTH // 2, start_y - 80),
        fontsize=60, color="black"
    )
    for i, btn in enumerate(buttons):
        rect = btn["rect"]
        text = f"Som: {'Ligado' if sound_on else 'Desligado'}" if i == 1 else btn["text"]
        screen.draw.filled_rect(rect, (200, 200, 200))
        screen.draw.rect(rect, (100, 100, 100))
        screen.draw.text(text, center=rect.center, fontsize=24, color="black")

def draw():
    if game_state == "menu":
        draw_menu()
    elif game_state == "jogo":
        draw_game()
def update(dt):
    """
    Esta funcao e chamada a cada frame pelo Pygame Zero.
    'dt' e o tempo (em segundos) que passou desde o ultimo frame.
    Usamos 'dt' para garantir que o movimento seja suave e consistente
    em computadores de diferentes velocidades.
    """
    # Declaramos todas as variaveis globais que a funcao vai modificar
    global player_direction, is_attacking, attack_timer, attack_cooldown

    if game_state == "jogo":
        # 1. ATUALIZA OS CRONOMETROS (SEMPRE)
        if attack_cooldown > 0:
            attack_cooldown -= dt

        if is_attacking:
            attack_timer -= dt
            # Se o tempo do ataque acabou, desativa o modo de ataque
            if attack_timer <= 0:
                is_attacking = False

        # 2. LOGICA DE ACAO: ATACAR OU MOVER/DESCANSAR?
        
        # <<< SE ESTIVER ATACANDO, TODA A LOGICA DE ATAQUE FICA AQUI DENTRO >>>
        if is_attacking:
            # --- LOGICA DE ANIMACAO DE ATAQUE (ROTACAO) ---
            
            # Posiciona a arma na mao do personagem (ponto de pivo)
            offset_x, offset_y = ARMA_OFFSETS[player_direction]
            arma.x = player.x + offset_x
            arma.y = player.y - (player.height / 2) + offset_y
            
            # Calcula o progresso da animacao (de 0.0 a 1.0)
            progress = (ATTACK_DURATION - attack_timer) / ATTACK_DURATION
            
            # Interpola o angulo atual baseado no progresso
            current_angle = SWING_START_ANGLE + (SWING_END_ANGLE - SWING_START_ANGLE) * progress
            arma.angle = current_angle
            
            # Garante que a imagem certa esta sendo usada durante o ataque
            if player_direction in ['frente', 'costas']:
                arma.image = 'itens/axe_0118' # Substitua pelo seu nome de arquivo
            else:
                arma.image = 'itens/axe_0118' # Substitua pelo seu nome de arquivo
        
        # <<< SENAO (SE NAO ESTIVER ATACANDO), A LOGICA DE MOVIMENTO/DESCANSO FICA AQUI >>>
        else:
            # --- LOGICA DE MOVIMENTO DO PERSONAGEM ---
            if keyboard.left:
                player.x -= PLAYER_SPEED * dt
                player.image = 'moobs/persona_0087' # Seu sprite de personagem
                player_direction = 'esquerda'
            elif keyboard.right:
                player.x += PLAYER_SPEED * dt
                player.image = 'moobs/persona_0087'
                player_direction = 'direita'

            if keyboard.up:
                player.y -= PLAYER_SPEED * dt
                player.image = 'moobs/persona_0087'
                player_direction = 'costas'
            elif keyboard.down:
                player.y += PLAYER_SPEED * dt
                player.image = 'moobs/persona_0087'
                player_direction = 'frente'

            # --- ATUALIZACAO DA ARMA (EM POSICAO DE DESCANSO) ---
            offset_x, offset_y = ARMA_OFFSETS[player_direction]
            arma.x = player.x + offset_x
            arma.y = player.y - (player.height / 2) + offset_y
            
            # Reseta o angulo da arma e atualiza sua imagem/orientacao
            arma.angle = 0
            if player_direction == 'frente':
                arma.image = 'itens/axe_0118'
            elif player_direction == 'costas':
                arma.image = 'itens/axe_0118'
            elif player_direction == 'direita':
                arma.image = 'itens/axe_0118'
                arma.flip_x = False
            elif player_direction == 'esquerda':
                arma.image = 'itens/axe_0118'
                arma.flip_x = True

# --- FUNÇÕES DE INPUT (EVENTOS) ---
def on_mouse_down(pos):
    global sound_on, game_state
    if game_state == "menu":
        for i, btn in enumerate(buttons):
            if btn["rect"].collidepoint(pos):
                if i == 0: game_state = "jogo"
                elif i == 1:  # Botao de Som
                    # 1. Inverte o estado da variavel 'sound_on'
                    sound_on = not sound_on

                    # 2. SE o som estiver ligado, toque a musica.
                    if sound_on:
                        # O '-1' faz a musica tocar em loop infinito.
                        # Remova se quiser que toque so uma vez.
                        music.play("song")
                    # 3. SENAO (se o som estiver desligado), pare a musica.
                    else:
                        music.stop()
                elif i == 2: quit()

def on_key_down(key):
    global game_state, is_attacking, attack_timer, attack_cooldown
    if key == keys.ESCAPE and game_state == "jogo":
        game_state = "menu"
    # Inicia o ataque ao pressionar a barra de espaco
    if key == keys.SPACE:
        # So pode atacar se:
        # 1. Estiver na tela do jogo
        # 2. Nao estiver atacando no momento
        # 3. O tempo de cooldown ja tiver acabado
        if game_state == "jogo" and not is_attacking and attack_cooldown <= 0:
            print("Ataque iniciado!") # Mensagem de teste
            is_attacking = True
            attack_timer = ATTACK_DURATION
            attack_cooldown = ATTACK_COOLDOWN_TIME

# Inicia o jogo
pgzrun.go()