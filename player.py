import random
import time
import sys
import msvcrt

#----------------- CLASSE PLAYER-----------------------------------------------------
class Player:
    def __init__(self,nome,ataque,defesa,cura, hp):
        self.nome = nome
        self.ataque = ataque
        self.defesa = defesa
        self.cura = cura
        self.hp = hp
        self.hp_max = hp
        self.defesa_base = defesa
        
    def atacar(self):
        frase = self.frase_ataque()  # Obtém a frase aleatória da classe específica
        
        return self.ataque

    def frase_ataque(self):
        return "Ataque realizado!"

    def defender(self):
        self.defesa *= 1.2  # Defesa aumentada em 20% ao ativar
        print (f"{self.nome} se defendeu, reduzindo o dano em {self.defesa:.2f}!")
        return self.defesa

    def curar(self):
        vida_recuperada = self.cura * 5
        self.hp += vida_recuperada
          # Atualiza o HP do jogador
        
        if self.hp > self.hp_max:
            self.hp = self.hp_max
        print(f"DEBUG: {self.nome} curou {vida_recuperada:.2f}. HP atualizado para {self.hp:.2f}")
        

    def restaurar_hp(self):
        self.hp = self.hp  # Restaura o HP ao valor inicial
        return f"{self.nome} recuperou todo o HP após vencer a batalha! 💖"
#------------------------------------------------------------------------------------
#----------------- CLASSE MAGO-----------------------------------------------------
class Mago(Player):
    def __init__(self):
        super().__init__(nome='Mago', ataque=10, defesa=5, cura=8, hp=70)
        self.ataque_especial = 'bola de fogo'
        

    def frase_ataque(self):
        frases = [
            "Sinta o poder do meu... cajadão!!",
            "Abracadabra! Ou era Abacatebraba... enfim, toma!",
            "Ué, funcionou? FUNCIONOU! Anota aí, primeiro sucesso da carreira!"
        ]
        return(random.choice(frases))

    def frase_defesa(self):
        frases = [
            "Melhor defender!",
            "Eu sou frágil, mas sou brabo!",
            "Escudo mágico! Agora só falta o seguro de vidaaa!"
        ]
        return random.choice(frases)

    def frase_erro(self):
        frases = [
            "Errei? Deve ter sido interferência mágica... ou gases.",
            "Droga! Bati o cajado no próprio pé...",
            "Alguém viu pra onde foi o meu feitiço? Tá com lag, certeza. Só pode ser dessa net!"
        ]
        return random.choice(frases)

    def frase_dano(self):
        frases = [
            "AI, MINHA MANA! ... e minha dignidade!",
            "Meu manto foi atingido! Era edição limitada!",
            "Esse golpe doeu mais que ver o saldo da minha conta."
        ]
        return random.choice(frases)

    def frase_cura(self):
        frases = [
            "Recuperando... espere... isso é... Estus Flask ou chá detox?",
            "Ahhh... mana restaurada, ego inflado!",
            "Já tô quase novo! Só falta desentortar a coluna."
        ]
        return random.choice(frases)

    def frase_derrota(self):
        frases = [
            "Hogwarts...? É você que me chama? Ou... sou um trouxa!",
            "Morre-se o mago... Talvez na próxima vida",
            "Talvez eu devesse ter malhado mais... pra usar armadura pesada..."
        ]
        return random.choice(frases)

    def usar_ataque_especial(self):
        dano_especial = self.ataque * 3
        print("🔥 Magia suprema ativada! 🔥")
        return dano_especial
#------------------------------------------------------------------------------------    

#----------------- CLASSE GUERREIRO-----------------------------------------------------
class Guerreiro(Player):
    def __init__(self):
        super().__init__(nome='Guerreiro', ataque=12, defesa=8, cura=5, hp=90)
        self.ataque_especial = "Golpe Poderoso"

    def frase_ataque(self):
        frases = [
            "BOOOM! ISSO que eu chamo de aperto de mão!",
            "Derrubei? Hmmm… pensei que fosse mais forte.",
            "Tá sentindo esse cheiro? É cheiro de vitória (ou queimado, sei lá)."
        ]
        return(random.choice(frases))

    def frase_defesa(self):
        frases = [
            "Subi a defesa! Hoje eu tô só o concreto armado, pode bater!",
            "Defendi. Quem bater, voltará!",
            "Segurando aqui, na marra!"
        ]
        return random.choice(frases)

    def frase_erro(self):
        frases = [
            "Errei nada! Era só um aquecimento!",
            "Tava testando o vento… e o chão… e minha própria cara.",
            "Eu nunca erro. Eu... redireciono."
        ]
        return random.choice(frases)

    def frase_dano(self):
        frases = [
            "AI! Eu sou forte, mas não sou de aço não, pô!",
            "Isso foi um golpe? Eu pensei que fosse um abraço agressivo.",
            "Respira... respira... finge que foi só um mosquito bravo."
        ]
        return random.choice(frases)

    def frase_cura(self):
        frases = [
            "Tô novo! Igual a carne de ontem que ficou fora da geladeira.",
            "Comi um pedaço de pedra e melhorei. Guerreiro raiz!",
            "Isso vai sarar... se não sarar, a gente finge que tá bem."
        ]
        return random.choice(frases)

    def frase_derrota(self):
        frases = [
            "Aguentei firme... mas não tanto.",
            "Me vou... mas vou na marra!",
            "Cai de pé... tropeçando, mas de pé!"
        ]
        return random.choice(frases)

    def usar_ataque_especial(self):
        dano_especial = self.ataque * 2
        print("⚔️ Espada Flamejante em ação! ⚔️")
        return dano_especial
#------------------------------------------------------------------------------------
        
#---------------------------ESCOLHER PERSONAGEM---------------------------------------------------
def digitar_texto(texto, velocidade=0.03):
    for caractere in texto:
        if msvcrt.kbhit():
            tecla = msvcrt.getch()
            if tecla == b'\r':
                print(texto)
                return
        sys.stdout.write(caractere)
        sys.stdout.flush()
        time.sleep(velocidade)
    print()

def escolher_classe():
    digitar_texto("\n1. 🪄 Mago - Atributos:")
    digitar_texto("Fraco dos músculos;")
    digitar_texto("Forte no blá-blá-blá arcano;")
    digitar_texto("Camper profissional;")
    digitar_texto("Vai com calma que mana evapora fácil;")
    digitar_texto("Morre assim que bate o dedinho do pé!")
    digitar_texto("🧙 Ideal pra quem quer causar estrago sem sujar a túnica.\n")

    digitar_texto("2. ⚔️ Guerreiro - Atributos:")
    digitar_texto("Forte dos músculos;")
    digitar_texto("Neurônio não é o ponto forte;")
    digitar_texto("Bate primeiro, pensa depois (se conseguir pensar, é claro);")
    digitar_texto("Capaz de resolver conflitos com a delicadeza de um bode raivoso.")
    digitar_texto("💪 Ideal pra quem acha que ‘tática’ é nome de remédio.\n")

    escolha = input("Digite o número correspondente à sua classe: ")

    if escolha == "1":
        return Mago()
    elif escolha == "2":
        return Guerreiro()
    else:
        print("Escolha inválida! Tente novamente.")
        return escolher_classe()
#------------------------------------------------------------------------------------