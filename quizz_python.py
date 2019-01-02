# -*- coding: utf-8 -*-

def boas_vindas():
    """
    Mensagem de boas boas vindas
    """
    print 'Bem-vindo ao jogo!'

def escolher_nivel():
    """
    Pergunta para o jogador o nível de dificuldade.
    Retorna a frase com o nível correspondente.
    """
    escolha = raw_input('Escolha o nivel: facil, medio ou dificil ')
    escolha = escolha.lower()
    if escolha == 'facil':
        print 'Nivel facil:'
        return frase_facil
    if escolha == 'medio':
        print 'Nivel medio:'
        return frase_medio
    if escolha == 'dificil':
        print 'Nivel dificil:'
        return frase_dificil
    else:
        print 'Nivel invalido'
        return escolher_nivel()

def inicio_de_jogo(frase, respostas):
    """
    Pergunta para o jogador a resposta.
    Se a resposta for correta, segue para a próxima pergunta da lista. Conforme o acerto, ocorre o replace da 'pergunta'
    pela 'resposta_jogador'.
    Se a resposta for incorreta, aparecerá a mensagem 'Tente novamente' e perguntará novamente a respota correspondente a
    questão errada.
    Quando 'jogo_terminado = True' aparecerá a mensagem 'Parabens! Fim de jogo'.
    """
    for pergunta in lista_perguntas:
        resposta_jogador = raw_input('Qual a palavra: ' + pergunta + '? ')
        resposta_jogador = resposta_jogador.lower()
        jogo_terminado = False

        while jogo_terminado != True:
            if resposta_jogador in respostas:
                print 'Correto'
                frase = frase.replace(pergunta, resposta_jogador)
                print frase
                jogo_terminado = True
            else:
                print 'Tente novamente'
                resposta_jogador = raw_input('Qual a palavra: ' + pergunta + '? ')
                resposta_jogador = resposta_jogador.lower()

    print 'Parabens! Fim de jogo'

"""
Listas utilizadas
"""
frase_facil = 'O __1__ roeu a rica roupa do __2__ de __3__! A rainha raivosa __4__ o resto e depois resolveu remendar!'
frase_medio = 'Trazei tres __1__ de __2__ para tres __3__ __4__ comerem.'
frase_dificil = 'Num ninho de __1__ ha sete __2__. Quando a __3__ gafa, __4__ os sete __2__.'

lista_perguntas = ['__1__','__2__','__3__','__4__']

respostas_facil = ['rato', 'rei', 'roma', 'rasgou']
respostas_medio = ['pratos', 'trigo', 'tigres', 'tristes']
respostas_dificil = ['mafagafos', 'mafagafinhos', 'mafagafa', 'gafam']

"""
Chamada das funções
"""
boas_vindas()
nivel = escolher_nivel()
print nivel
if nivel == frase_facil:
    inicio_de_jogo(frase_facil, respostas_facil)
elif nivel == frase_medio:
    inicio_de_jogo(frase_medio, respostas_medio)
else:
    inicio_de_jogo(frase_dificil, respostas_dificil)
