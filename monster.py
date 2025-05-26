import random


# Subclasses de monstros com características únicas---------
class Monsters:
    def __init__(self, nome, dano, defesa, hp):
        self.nome = nome
        self.dano = dano
        self.defesa = defesa
        self.hp = hp

    def atacar(self):
        return self.dano

    def defender(self):
        return self.defesa * 1.1  # Defesa aumentada em 10%
#--------------------------------Goblin(Monsters)---------------------------------------
class Goblin(Monsters):
    def __init__(self):
        super().__init__("Goblin Agricultor", dano=8, defesa=4, hp=40)

    def frase_entrada(self):
        frases = [
            "Quem pisa no meu alface... VAI PRO CALDEIRÃO!",
            "Bem-vindo à agrofloresta do caos, otário!",
            "Quer tomate orgânico? Eu dou... NO SEU ROSTO!"
        ]
        return random.choice(frases)

    def frase_ataque(self):
        frases = [
            "Pegue esse pepino mutante!!!",
            "Toma um nabo do mal!",
            "Salada com dor, especial da casa."
        ]
        return random.choice(frases)

    def frase_defesa(self):
        frases = [
            "Ih rapaz, fechei a porteira... Aqui ninguém passa não, sô!",
            "Vou me defender aqui. Se bater, eu devolvo com enxadada!",
            "Recolhi as galinhas, tranquei a cerca e ergui o espantalho. Tá protegido!"
        ]
        return random.choice(frases)

    def frase_erro(self):
        frases = [
            "Droga, bati no meu pé de couve...",
            "Ai não, esbarrei no espantalho de novo!",
            "Esse arado tava torto, juro!"
        ]
        return random.choice(frases)

    def frase_dano(self):
        frases = [
            "Meus legumeees!",
            "Você vai pagar com juros e compostagem!",
            "Isso vai pro relatório do SENAC, hein?"
        ]
        return random.choice(frases)

    def frase_derrota(self):
        frases = [
            "Meus legumes... nunca mais verão o sol!",
            "Maldição! Agora vou virar adubo!",
            "Essa pancada acabou com minha horta inteira..."
        ]
        return random.choice(frases)

#-------------------------------Orc(Monsters)----------------------------------------
class Orc(Monsters):
    def __init__(self):
        super().__init__("Orc Maromba", dano=12, defesa=6, hp=50)

    def frase_entrada(self):
        frases = [
            "BORA PO##A! Eu ia estar ganhando mais no Baldur’s Gate 3... Já tô me arrependendo de ter vindo, já...",
            "MEU WHEY TÁ BATENDO, CUIDADO!",
            "Você é meu novo supino humano!"
        ]
        return random.choice(frases)

    def frase_ataque(self):
        frases = [
            "Toma agachamento reverso NA CARA!",
            "SUPINO EXPLOSIVO!!!",
            "Bate aqui... com a cara mesmo!"
        ]
        return random.choice(frases)

    def frase_defesa(self):
        frases = [
            "Ativando modo tanque... aqui é fibra, parceiro!",
            "Pode bater, baby... cê acha que esse tríceps é só enfeite?",
            "Tô segurando no pump! Hoje é treino de resistência!"
        ]
        return random.choice(frases)

    def frase_erro(self):
        frases = [
            "Droga! Escorreguei no whey!",
            "Esse golpe foi só aquecimento.",
            "Acho que treinei perna ontem... não tô bem."
        ]
        return random.choice(frases)

    def frase_dano(self):
        frases = [
            "MINHA DIGNIDADE!!!",
            "Vai pagar por arranhar meu tanquinho!",
            "Você tá atrapalhando minha hipertrofia!!"
        ]
        return random.choice(frases)

    def frase_derrota(self):
        frases = [
        "Caí...",
        "A proteína... me abandonou...",
        "Foi-se minha vida de marombeiro..."
    ]
        return random.choice(frases)

#------------------------------Esqueleto(Monsters)-----------------------------------------
class Esqueleto(Monsters):
    def __init__(self):
        super().__init__("Esqueleto Coach", dano=8, defesa=4, hp=40)

    def frase_entrada(self):
        frases = [
            "Você só apanhará se quiser... Eu nunca apanho, MUHAHAHAH, só penso positivo!",
            "ACREDITE NO SEU PESCOÇO! (Mesmo que eu não tenha um.)",
            "Dor é só falta de mindset!"
        ]
        return random.choice(frases)

    def frase_ataque(self):
        frases = [
            "QUEBREI SEUS LIMITES! E sua costela!",
            "Visualiza o sucesso... da minha pancada!",
            "Essa é a força da mentalidade óssea!"
        ]
        return random.choice(frases)

    def frase_defesa(self):
        frases = [
            "Pensa comigo: dor é temporária, ossos... também eram, mas superei!",
            "Boraaa, mente blindada, pancada não me afeta! Cê só perde se quiser!",
            "A vida te bate? Defendido!"
        ]
        return random.choice(frases)

    def frase_erro(self):
        frases = [
            "Ops, falha do universo... ou minha energia tá baixa, só pode.",
            "Tá vibrando na frequência errada, esqueletón, bora, se reergue e foco pra não errar o próximo!!",
            "É tudo aprendizado... menos quando eu revidar na sua cara hoje."
        ]
        return random.choice(frases)

    def frase_dano(self):
        frases = [
            "Você tá me desconstruindo emocionalmente!",
            "Vou me alinhar nos chakras e voltar mais forte!",
            "Golpes psicológicos? Que atitude limitada..."
        ]
        return random.choice(frases)

    def frase_derrota(self):
        frases = [
            "Meu mindset... quebrou junto com a bacia!",
            "Me explodiu em pedaços... A última coisa que vi passar na frente dos meus olhos foi... minha bunda...",
            "Mente blindada... ossos nem tanto!"
        ]
        return random.choice(frases)
#-----------------------------------Troll(Monsters)------------------------------------
class Troll(Monsters):
    def __init__(self):
        super().__init__("Troll do Wifi Ruim", dano=12, defesa=6, hp=50)

    def frase_entrada(self):
        frases = [
            "Tentei carregar minha raiva... ERRO 404!",
            "TO LAGADO MAS TÔ FORTE!",
            "Você será desconectado... permanentemente... MUAHAHAHAH!"
        ]
        return random.choice(frases)

    def frase_ataque(self):
        frases = [
            "Ping alto, força maior, toma!",
            "Lagou? Lagou você!",
            "Buffer isso aqui: PAH!"
        ]
        return random.choice(frases)

    def frase_defesa(self):
        frases = [
            "Ativando... Defe... 🛑❌🛑 conexão perdida...",
            "Travou, bebê. Se me acertar, a culpa é do lag!",
            "Ping 9999, pode bater... mas só chega daqui meia hora!"
        ]
        return random.choice(frases)

    def frase_erro(self):
        frases = [
            "Ai, caí da rede!",
            "Esse ataque tava em download ainda...",
            "Glitch no músculo esquerdo."
        ]
        return random.choice(frases)

    def frase_dano(self):
        frases = [
            "VOCÊ VAI PAGAR PELO MEU PLANO DE 2MB!",
            "Isso foi... só por causa do... delay... doloroso!!!",
            "Preciso atualizar meu antivírus emocional."
        ]
        return random.choice(frases)

    def frase_derrota(self):
        frases = [
        "Aaaaaaai... foi lag! Eu juro!",
        "Desconectando... última mensagem: eu vou voltar!",
        "Fui trollado pelo destino...."
        ]
        return random.choice(frases)
#------------------------------FinalBoss(Monsters)-----------------------------------------
class FinalBoss(Monsters):
    def __init__(self):
        super().__init__("ERROR-9090", dano=25, defesa=20, hp=100)

    def ataque_especial(self):
        self.dano = self.dano * 1.3

    def frase_entrada(self):
        frases = [
            "Quem ousa reiniciar minha fúria?!",
            "Seu dispositivo será desconectado... da existência.",
            "Ah não, mais um usuário que não sabe o que é limpar o cache!",
            "Backup? Eu como no café da manhã."
        ]
        return random.choice(frases)

    def frase_ataque(self):
        frases = [
            "Você acaba de tomar um ALT+F4 na alma!",
            "Erro fatal detectado: sua existência.",
            "Prepare-se para o boot no nariz!",
            "CTRL+ALT+SOCO!"
        ]
        return random.choice(frases)

    def frase_defesa(self):
        frases = [
            "Firewall ativado. Boa sorte tentando me crackear!",
            "Modo segurança: ON. Agora nem admin bate aqui!",
            "Ataques bloqueados. Tente novamente após reiniciar sua esperança."
        ]
        return random.choice(frases)

    def frase_erro(self):
        frases = [
            "Hmm... lag no sistema. Tenta de novo, ERROR-9000.",
            "Erro 404: golpe não encontrado.",
            "Não foi falha, foi simulação.",
            "O mouse travou, me dá um segundo!"
        ]
        return random.choice(frases)

    def frase_dano(self):
        frases = [
            "Você ousa corromper meu código?!",
            "RAM danificada! RAM danificada!",
            "Aaaai! Isso doeu mais que bug sem debug!",
            "Isso não estava nos termos de uso!"
        ]
        return random.choice(frases)

    def fala_random(self):
        frases = [
            "Você leu a política de privacidade antes de apanhar?",
            "Estou 98% carregado de raiva. Os 2% tão em loading",
            "Chamo isso de 'ataque de negação de serviço pessoal'!",
            "Eu sou o erro que aparece às 3 da manhã e ninguém consegue consertar!"
        ]
        return random.choice(frases)

    def frase_derrota(self):
        frases = [
            "S-Sistema corrompido... Reinstale sua vitória... zzzZZZZZzz...",
            "Desligando... mas lembra... eu volto na próxima versão beta, MUHHAHAH!"
        ]
        return random.choice(frases)

    def ataque_especial(self):
        self.dano = self.dano *1.3
