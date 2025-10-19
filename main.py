# -*- coding: utf-8 -*-
import time

# ======= CONTROLE DE RITMO =======
BPM = 96  # ajuste aqui pra casar com o vídeo
BEAT = 60 / BPM

def wait(beats=1.0):
    time.sleep(beats * BEAT)

def texto(line, beats=4):
    print(line)
    wait(beats)

def mantra(frase, vezes=4, espaçamento_beats=2):
    for _ in range(vezes):
        print(frase)
        wait(espaçamento_beats)

# ======= BLOCOS =======
def intro_resenha():
    texto("Primeiramente vou lançar um pronunciamento aqui antes, né?", 4)
    texto("Que na Bahia o que bate é maluquice", 4)
    texto("Então eu vou lançar de maluquice aqui", 3)
    texto("Se for pra me escutar e levar a sério, nem escute", 3)
    texto("É, a parada é essa", 2)
    texto("Eskine, o gangster do arrocha", 2)
    texto("Bota a peça pra cima, tô brincando, calma", 3)
    texto("É arrocha, vamo' simbora", 2)
    texto("Alô Levi, alô DDL, assim ó, ó, pega", 3)

def refrao_solta_a_carta(loops=2):
    for _ in range(loops):
        texto("Solta a carta, car*lho", 2.5)
        texto("Tigrinho, filha da p*ta", 2.5)
        texto("Pra eu pegar o meu dinheiro", 2.5)
        texto("E comer umas quatro p*ta'", 2.5)

def bloco_vuk_onda():
    texto("É vuk, vuk, vuk, vuk, na onda maluca", 3)
    texto("É vuk, vuk, vuk, vuk, ah", 2.5)
    texto("É vuk, vuk, vuk, vuk, na onda maluca", 3)
    texto("É vuk, vuk, solta a carta, tigrinho, vai", 3)
    texto("É vuk, vuk, vuk, eh, vuk, na onda maluca", 3)
    texto("É vuk, vuk, vuk, vuk, ah", 2.5)
    texto("Ó o naipe, vuk, vuk, vuk na onda, eh", 3)
    texto("Vuk, vuk, vuk", 2)

def bloco_papo_de_cria():
    texto("Assim ó, papo de cria, ela roça no pau", 2.5)
    mantra("Roça no pau", 2, 1.2)
    texto("Roça no pau, não me leve a mal", 2.5)
    texto("Não me leve a mal, toma sequência, ei, tum", 2.5)
    mantra("Toma sequência de pau", 5, 1.2)
    texto("Sequência, tome", 1.8)
    mantra("Sequência de pau, arrocha, sequência de pau", 2, 1.3)
    mantra("O naipe com arrocha, vai, oh, sequência de pau", 1, 2)
    mantra("Sequência de pau", 2, 1.2)
    texto("Toma sequência", 1.5)

def bloco_passinho_romano():
    texto("Hm, faz o passinho do romano mais aquela sarrada no ar", 3)
    mantra("Faz o passinho do romano mais aquela sarrada no ar", 1, 3)
    texto("Faz o passinho do romano, faz, aquela sarrada no ar", 3)
    texto("Faz o passinho do romano mais aquela, vai", 2.5)
    mantra("Tchu, ei, tchu, tchu, tchu", 1, 1.2)
    texto("Tchururu, vai no passinho do romano, mais aquela sarrada no, tchu", 3)
    mantra("Tchuru, tchu, tchu", 1, 1.1)
    texto("Tchuru, faz o passinho do romano, mais aquela sarrada no", 2.5)
    mantra("Tchu, ei, tchuru, tchu, tchu", 1, 1.1)
    texto("Tchuru, vai no passinho do romano, mais aquela sarrada no tchu, ei", 3)
    mantra("Tchuru, tchu, tchu", 1, 1.1)

def bloco_gerente_dancinhas():
    texto("Vou lançar a gerente aqui, ó, assim, ó, ó", 2)
    texto("Dancinha do Manoel, batedeira invertida, foi pro lado, parou", 3)
    mantra("E naipe, tchugudu, tchugudu", 3, 1.1)
    texto("Olhou pra cara da amiga, deu risada sem graça", 2.5)
    texto("Não quero, cala a boca agora", 2)
    texto("E teile e puxe, e pegue e naipe", 2.2)
    mantra("E naipe, naipe", 2, 0.9)
    mantra("E naipe, e naipe, naipe, e naipe, naipe", 2, 1.1)

def bloco_banana_call():
    texto("Canta assim Albergue", 1.8)
    mantra("Boto na cama, te soco a banana, o que é que tu faz?", 1, 3)
    mantra("Se eu te boto na cama, te soco a banana, o que é que tu faz?", 1, 3)
    texto("Se eu te boto na cama, te soco a banana, o que é que tu, E ela faz, ó", 3)
    texto("Se eu te boto na cama, te soco a banana, o que é que tu faz?", 3)
    texto("Vem e bota, ui, lá ele", 2.2)
    mantra("Te boto, vai", 7, 0.9)
    mantra("Ui, vai ser só pau nas canjanga", 1, 2.8)
    mantra("Só pau nas canjanga", 4, 1.2)

def bloco_xereca_coroa():
    texto("Rala a xerec* no Playba", 2.5)
    mantra("Calma, vida, tá de boa", 1, 1.4)
    texto("Rala a xerec* no Laizzao", 2.5)
    mantra("Calma, vida, tá de boa", 1, 1.4)
    texto("Rala a xerec* no Donk", 2.5)
    mantra("Calma, vida, tá de boa", 1, 1.4)
    texto("Rala a xerec* no Alê", 2.5)
    mantra("Calma, vida, tá de boa", 1, 1.4)
    texto("Vai lá mama, mas tá de boa", 2.5)
    texto("Rala a xerequinha no coroa, p*rra", 2.5)
    mantra("No coroa, joga no coroa, p*rra", 6, 1.0)

def bloco_zoada():
    texto("Quando eu trans* com ela é uma zoada do carai", 2.8)
    texto("A noite toda é uma zoada do carai", 2.5)
    texto("Quando eu pego de jeito é uma zoada do car*lho", 2.8)
    texto("A noite toda é uma zoada do", 2.0)
    mantra("Ai, ai, ai, oi", 1, 1.3)
    mantra("Ai, ai, ai", 1, 1.1)
    texto("Ai, ai, ai, a noite toda é uma zoada do carai", 2.5)
    mantra("Ai, ai, ai, ai", 1, 1.1)
    mantra("Ai, ai, ai", 1, 1.1)
    texto("Ai, ai, ai, a noite toda é uma zoada do carai", 2.5)

def bloco_espada():
    mantra("Ela quer pegar na minha espada, ela quer pegar na minha", 4, 1.6)

def bloco_sextou_barba():
    texto("Chegou sexta-feira, é dia de se alinhar", 2.5)
    texto("Pega o barbeador e começa a raspar", 2.5)
    # alterna verificação de 'lisinha' / 'raspada'
    for _ in range(2):
        texto("Deixa eu ver, deixa eu ver se tá lisinha", 2.5)
        texto("Deixa eu ver, deixa eu ver, tá raspa'", 2.2)
    texto("Deixa eu ver se tá lisinha", 2.2)
    texto("Deixa eu ver, e tá raspada", 2.2)
    texto("Deixa eu ver se tá li'", 1.6)
    texto("Deixa eu ver, tá raspadinha", 2.2)
    texto("Deixa eu ver se tá lisinha", 2.2)

# ======= ROTEIRO =======
def show():
    intro_resenha()
    refrao_solta_a_carta(loops=2)
    bloco_vuk_onda()

    bloco_papo_de_cria()
    bloco_passinho_romano()
    bloco_gerente_dancinhas()

    bloco_banana_call()
    bloco_xereca_coroa()
    bloco_zoada()
    bloco_espada()
    bloco_sextou_barba()

    # Encorezinho maroto:
    refrao_solta_a_carta(loops=1)
    bloco_vuk_onda()
    print("🔥 Fim da resenha — DJ Python assinou. 🔥")

if __name__ == "__main__":
    show()
