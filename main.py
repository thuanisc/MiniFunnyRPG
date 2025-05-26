import pygame
import sys

# from battle import introducao
#
# if __name__ == "__main__":
#     introducao()

def menu_visual():
    pygame.init()
    pygame.mixer.init()
    largura, altura = 800, 600
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Mini-RPG")

    pygame.mixer.music.load("musicas/musica.mp3")
    pygame.mixer.music.play(-1)

    fundo = pygame.image.load("imagens/fundo_menu.jpg").convert()
    fundo = pygame.transform.scale(fundo, (largura, altura))

    letreiro = pygame.image.load("imagens/letreiro.png").convert_alpha()
    letreiro = pygame.transform.scale(letreiro, (480, 120))
    letreiro_rect = letreiro.get_rect(center=(largura // 2, 110))
    fundo_letreiro = pygame.Surface((500, 130), pygame.SRCALPHA)
    fundo_letreiro.fill((0, 0, 0, 120))

    fonte = pygame.font.SysFont("arial", 20, bold=True)

    # Botões
    botao_start = pygame.image.load("imagens/Botao.png").convert_alpha()
    botao_start = pygame.transform.scale(botao_start, (200, 60))
    rect_start = botao_start.get_rect(center=(largura // 2 + 120, 500))

    botao_sair = pygame.transform.scale(botao_start.copy(), (200, 60))
    rect_sair = botao_sair.get_rect(center=(largura // 2 - 120, 500))

    botao_creditos = pygame.transform.scale(botao_start.copy(), (180, 50))
    rect_creditos = botao_creditos.get_rect(center=(largura // 2, 570))

    som_clique = pygame.mixer.Sound("musicas/click.wav")

    clock = pygame.time.Clock()
    rodando = True
    while rodando:
        tela.blit(fundo, (0, 0))
        tela.blit(fundo_letreiro, (letreiro_rect.left - 10, letreiro_rect.top - 5))
        tela.blit(letreiro, letreiro_rect.topleft)

        mouse_pos = pygame.mouse.get_pos()

        def desenhar_botao(botao_img, rect, texto):
            tela.blit(botao_img, rect.topleft)
            if rect.collidepoint(mouse_pos):
                overlay = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
                overlay.fill((0, 0, 0, 100))
                tela.blit(overlay, rect.topleft)
            texto_render = fonte.render(texto, True, (148, 0, 211))  # Roxo uva
            texto_rect = texto_render.get_rect(center=rect.center)
            tela.blit(texto_render, texto_rect)

        desenhar_botao(botao_sair, rect_sair, "Quit")
        desenhar_botao(botao_start, rect_start, "Start")
        desenhar_botao(botao_creditos, rect_creditos, "Créditos")

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if rect_start.collidepoint(mouse_pos):
                    som_clique.play()
                    pygame.time.wait(200)
                    cena_intro_com_narrador(tela)
                    return
                elif rect_sair.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()
                elif rect_creditos.collidepoint(mouse_pos):
                    som_clique.play()
                    pygame.time.wait(200)
                    mostrar_creditos(tela)
                    return

        pygame.display.update()
        clock.tick(60)


def cena_intro_com_narrador(tela):
    largura, altura = 800, 600

    fundo = pygame.image.load("imagens/fundo_menu.jpg").convert()
    fundo = pygame.transform.scale(fundo, (largura, altura))

    narrador = pygame.image.load("imagens/Narrador maluco.png").convert_alpha()
    narrador = pygame.transform.scale(narrador, (220, 220))

    fonte = pygame.font.SysFont("arial", 22)
    fonte_pequena = pygame.font.SysFont("arial", 16, italic=True)

    # Agrupando as falas em blocos maiores
    falas = [
        "Narrador Maluco: Aê, meu filho! Estamos sendo atacados por criaturas inimagináveis! E você! Um novato, noob, nível 0... da ralé. Bem... todo o Reino acredita que você é o escolhido para nos salvar. Portanto, sem delongas... escolha sua classe e vai pro fight!"
    ]

    indice_fala = 0
    texto_renderizado = ""
    clock = pygame.time.Clock()

    narrador_x = 850
    narrador_final_x = 560

    tempo_digito = pygame.time.get_ticks()
    velocidade = 20

    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if len(texto_renderizado) >= len(falas[indice_fala]):
                    indice_fala += 1
                    texto_renderizado = ""
                    tempo_digito = pygame.time.get_ticks()
                    if indice_fala >= len(falas):
                        tela_escolha_personagem(tela)
                        return

        tela.blit(fundo, (0, 0))

        if narrador_x > narrador_final_x:
            narrador_x -= 8
        else:
            narrador_x = narrador_final_x
        tela.blit(narrador, (narrador_x, 360))

        # Balão maior e centralizado
        balao_x, balao_y = 40, 280
        balao_largura, balao_altura = 600, 200
        pygame.draw.rect(tela, (255, 255, 255), (balao_x, balao_y, balao_largura, balao_altura))
        pygame.draw.rect(tela, (0, 0, 0), (balao_x, balao_y, balao_largura, balao_altura), 4)

        if indice_fala < len(falas):
            atual = falas[indice_fala]
            agora = pygame.time.get_ticks()
            num_chars = (agora - tempo_digito) // velocidade
            texto_renderizado = atual[:num_chars]

            linhas_renderizadas = renderizar_texto_multilinha(texto_renderizado, fonte, balao_largura - 30)

            # Centraliza verticalmente as linhas dentro do balão
            total_altura = len(linhas_renderizadas) * 25
            y_inicial = balao_y + (balao_altura - total_altura) // 2

            for i, linha in enumerate(linhas_renderizadas):
                tela.blit(linha, (balao_x + 15, y_inicial + i * 25))

        # Texto de instrução
        texto_clique = fonte_pequena.render("Clique para continuar...", True, (80, 80, 80))
        texto_rect = texto_clique.get_rect(center=(balao_x + balao_largura // 2, balao_y + balao_altura - 20))
        tela.blit(texto_clique, texto_rect)

        pygame.display.update()
        clock.tick(60)


def renderizar_texto_multilinha(texto, fonte, largura_max):
    palavras = texto.split(" ")
    linhas = []
    linha_atual = ""
    for palavra in palavras:
        teste = linha_atual + palavra + " "
        if fonte.size(teste)[0] <= largura_max:
            linha_atual = teste
        else:
            linhas.append(fonte.render(linha_atual.strip(), True, (0, 0, 0)))
            linha_atual = palavra + " "
    linhas.append(fonte.render(linha_atual.strip(), True, (0, 0, 0)))
    return linhas

def mostrar_creditos(tela):
    largura, altura = tela.get_size()
    fundo = pygame.Surface((largura, altura))
    fundo.fill((0, 0, 0))

    fonte = pygame.font.SysFont("arial", 26)
    textos = [
        "Créditos:",
        "Thuani Sampaio da Silva [reup]",
        "E não menos importantes... Google, YouTube e ChatGPT️",
        "",
        "Agradecemos por jogar!",
    ]

    espacamento = 40
    pos_y_inicial = altura
    clock = pygame.time.Clock()
    velocidade = 1  # pixels por frame

    rodando = True
    while rodando:
        tela.fill((0, 0, 0))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                return

        for i, linha in enumerate(textos):
            y = pos_y_inicial + i * espacamento
            texto_render = fonte.render(linha, True, (255, 255, 255))
            rect = texto_render.get_rect(center=(largura // 2, y))
            tela.blit(texto_render, rect)

        pos_y_inicial -= velocidade

        if pos_y_inicial + len(textos) * espacamento < 0:
            return  # Sai automaticamente ao final da rolagem

        pygame.display.update()
        clock.tick(60)

def tela_escolha_personagem(tela):
    from battle import iniciar_jogo
    from player import Mago, Guerreiro

    largura, altura = tela.get_size()
    fundo = pygame.Surface((largura, altura))
    fundo.fill((0, 0, 0))  # Fundo preto

    mago_img = pygame.image.load("imagens/Mago.png").convert_alpha()
    guerreiro_img = pygame.image.load("imagens/Guerreiro.png").convert_alpha()
    mago_img = pygame.transform.scale(mago_img, (120, 140))
    guerreiro_img = pygame.transform.scale(guerreiro_img, (120, 140))

    fonte_titulo = pygame.font.SysFont("arial", 20, bold=True)
    fonte_texto = pygame.font.SysFont("arial", 16)

    card_largura, card_altura = 260, 340
    espacamento = 60
    total_largura = card_largura * 2 + espacamento
    inicio_x = (largura - total_largura) // 2

    rect_mago = pygame.Rect(inicio_x, 140, card_largura, card_altura)
    rect_guerreiro = pygame.Rect(inicio_x + card_largura + espacamento, 140, card_largura, card_altura)

    atributos = {
        "Mago": [
            "Fraco dos músculos",
            "Forte no blá-blá-blá arcano",
            "Camper profissional",
            "Vai com calma que mana evapora fácil",
            "Morre assim que bate o dedinho do pé!",
            "Ideal pra causar sem sujar a túnica"
        ],
        "Guerreiro": [
            "Forte dos músculos",
            "Neurônio não é o ponto forte",
            "Bate primeiro, pensa depois",
            "Resolve com a delicadeza de um bode raivoso",
            "Ideal pra quem acha que 'tática' é nome de remédio"
        ]
    }

    clock = pygame.time.Clock()

    while True:
        tela.blit(fundo, (0, 0))
        mouse_pos = pygame.mouse.get_pos()

        for rect, personagem, imagem in [
            (rect_mago, "Mago", mago_img),
            (rect_guerreiro, "Guerreiro", guerreiro_img)
        ]:
            hover = rect.collidepoint(mouse_pos)

            # fundo do card com cor diferente no hover
            fundo_card = pygame.Surface((card_largura, card_altura), pygame.SRCALPHA)
            cor_hover = (255, 255, 0, 50)  # amarelo claro
            cor_normal = (0, 0, 0, 180)
            fundo_card.fill(cor_hover if hover else cor_normal)
            tela.blit(fundo_card, rect.topleft)

            # borda
            pygame.draw.rect(tela, (255, 255, 100) if hover else (255, 255, 255), rect, 2)

            # imagem
            img_x = rect.x + (card_largura - imagem.get_width()) // 2
            tela.blit(imagem, (img_x, rect.y + 10))

            # título
            titulo = f"🪄 {personagem}" if personagem == "Mago" else f"⚔️ {personagem}"
            titulo_txt = fonte_titulo.render(titulo, True, (255, 255, 255))
            tela.blit(titulo_txt, (rect.x + 10, rect.y + 160))

            # atributos
            for i, linha in enumerate(atributos[personagem]):
                texto = fonte_texto.render("- " + linha, True, (255, 255, 255))
                tela.blit(texto, (rect.x + 10, rect.y + 190 + i * 22))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if rect_mago.collidepoint(evento.pos):
                    iniciar_jogo(jogador=Mago())
                    return
                elif rect_guerreiro.collidepoint(evento.pos):
                    iniciar_jogo(jogador=Guerreiro())
                    return

        pygame.display.update()
        clock.tick(60)

def cena_pos_escolha(tela, jogador):
    import time
    largura, altura = tela.get_size()

    fundo = pygame.Surface((largura, altura))
    fundo.fill((0, 0, 0))

    narrador = pygame.image.load("imagens/Narrador maluco.png").convert_alpha()
    narrador = pygame.transform.scale(narrador, (220, 220))

    fonte = pygame.font.SysFont("arial", 22)
    fonte_pequena = pygame.font.SysFont("arial", 16, italic=True)

    falas = [
        f'“Ah, maravilha. O destino do Reino nas mãos de um acéfalo {jogador.nome}... AHAHAH cof, cof, digo... corajoso soldado.”',
        '“Fica tranquilo que não é nenhum soulslike, jovem, o tutorial é básico mesmo! O tempo para aprender é sempre curto...',
        'em compensação, os requisitos para qualificação mínima pra esse estágio seriam 12 anos de experiência na NASA',
        'e mestrado em Necromancia Quântica aplicada à pancadaria...”',
        'aproveita então que tamo te dando essa chance de aprendizado prático!!',
        '“Mas olha... a tarefa é árdua, o monstro é feio, o chão é escorregadio e a taxa de sucesso é de 3%',
        '(sem garantia, nem que venha com o Celso Russomanno).',
        'Portanto...\n... TE VIRAAAA!”',
        '💨 *POOF!*'
    ]

    indice_fala = 0
    texto_renderizado = ""
    clock = pygame.time.Clock()
    tempo_digito = pygame.time.get_ticks()
    velocidade = 25

    narrador_x = 850
    narrador_final_x = 560

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if len(texto_renderizado) >= len(falas[indice_fala]):
                    indice_fala += 1
                    texto_renderizado = ""
                    tempo_digito = pygame.time.get_ticks()
                    if indice_fala >= len(falas):
                        tela_escolha_caminho(tela, jogador)
                        return

        tela.blit(fundo, (0, 0))

        if narrador_x > narrador_final_x:
            narrador_x -= 8
        else:
            narrador_x = narrador_final_x
        tela.blit(narrador, (narrador_x, 360))

        # Balão de fala
        balao_x, balao_y = 40, 280
        balao_largura, balao_altura = 700, 200
        pygame.draw.rect(tela, (255, 255, 255), (balao_x, balao_y, balao_largura, balao_altura))
        pygame.draw.rect(tela, (0, 0, 0), (balao_x, balao_y, balao_largura, balao_altura), 4)

        if indice_fala < len(falas):
            atual = falas[indice_fala]
            agora = pygame.time.get_ticks()
            num_chars = (agora - tempo_digito) // velocidade
            texto_renderizado = atual[:num_chars]

            linhas_renderizadas = renderizar_texto_multilinha(texto_renderizado, fonte, balao_largura - 30)
            total_altura = len(linhas_renderizadas) * 25
            y_inicial = balao_y + (balao_altura - total_altura) // 2

            for i, linha in enumerate(linhas_renderizadas):
                tela.blit(linha, (balao_x + 15, y_inicial + i * 25))

        texto_clique = fonte_pequena.render("Clique para continuar...", True, (80, 80, 80))
        texto_rect = texto_clique.get_rect(center=(balao_x + balao_largura // 2, balao_y + balao_altura - 20))
        tela.blit(texto_clique, texto_rect)

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    menu_visual()
