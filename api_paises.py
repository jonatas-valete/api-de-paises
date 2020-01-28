import json

import requests
import sys


URL_ALL = 'https://restcountries.eu/rest/v2/all'
URL_NAME = 'https://restcountries.eu/rest/v2/name'



def requisicao(url):
    try:
        resposta = requests.get(url)

        if resposta.status_code == 200:
            return resposta
    except:
        print('Erro ao fazer requisição')


def requisicao_pais(url, pais_nome):
    try:
        resposta = requests.get('{}/{}'.format(url, pais_nome))

        if resposta.status_code == 200:
            return resposta

    except:
        print('Erro ao fazer requisição')


def texto_requisicao(resposta):
    resposta_texto = resposta.text
    return resposta_texto


def parsing(texto_resposta):
    parsing = json.loads(texto_resposta)
    return parsing


def conversao_automatica(url, pais_nome):
    try:
        resposta = requisicao_pais(url, pais_nome)
        texto = texto_requisicao(resposta)
        dados_convertidos = parsing(texto)
        return dados_convertidos

    except:
        print('Erro ao converter')



def contagem_paises():
    try:
        requisicao = requests.get(URL_ALL)

        if requisicao:
            texto_resposta = requisicao.text

            if texto_resposta:
                lista = json.loads(texto_resposta)
                quantidade = lista
                return (len(quantidade))

    except Exception as e:
        print('erro ao fazer requisição ')
        print(e)

def ler_paises():
    pais = sys.argv[2]
    return pais



def mostrar_moeda(pais):
    try:
        requisicao = requests.get('{}/{}'.format(URL_NAME, pais))

        if requisicao:
            texto_resposta = requisicao.text

            if texto_resposta:
                lista = json.loads(texto_resposta)
                nome = (lista[0]['name'])
                symbol = lista[0]['currencies'][0]['symbol']
                print('PAÍS: {} / MOEDA: {}'.format(nome, symbol))

    except Exception as e:
        print('País não encontrado, por favor tente novamente!')
        print(e)


def mostrar_populacao(pais):
    try:
        dados_conv = conversao_automatica(URL_NAME, pais)

        if dados_conv:
            nome = dados_conv[0]['name']
            populacao = dados_conv [0]['population']
            name_n_populacao = ('{} tem {} habitantes'.format(nome, populacao))
            return name_n_populacao

    except Exception as e:
        print('Erro ')
        print(e)


def buscar_idioma(pais):
    try:
        dados_conv = conversao_automatica(URL_NAME, pais)

        if dados_conv:
            nome = dados_conv[0]['name']
            idioma = dados_conv[0]['languages'][0]['nativeName']
            idioma_falado = ('NOME: {} / IDIOMA FALADO: {}'.format(nome, idioma))
            return idioma_falado
    except Exception as e:
        print(e)
        print('Erro ao buscar idioma')


def buscar_fronteiras(pais):
    try:
        dados_conv = conversao_automatica(URL_NAME, pais)

        if dados_conv:
            pais = dados_conv[0]['name']
            fronteiras = dados_conv[0]['borders']
            pais_fronteiras = ('PAÍS: {} / FRONTEIRAS: {}'.format(pais, fronteiras))
            print(pais_fronteiras)

    except Exception as e:
        print('Erro ao buscar fronteiras')
        print(e)


if __name__ == '__main__':
    try:
        if len(sys.argv) == 1:
            print("## Bem vindo ao sistema de países ##")
            print("Uso: python paises.py <ação> <nome do país>")
            print("Ações disponíveis: contagem, moeda, populacao, fronteiras, idioma")
        else:
            argumento1 = sys.argv[1]

            if argumento1 == 'contagem':
                contagem = contagem_paises()
                print('Existe {} paises no planeta'.format(contagem))
            elif argumento1 == 'moeda':
                pais = ler_paises()
                if pais:
                    moeda = mostrar_moeda(pais)
                    print(moeda)
            elif argumento1 == 'populacao':
                pais = ler_paises()
                if pais:
                    population = mostrar_populacao(pais)
                    print(population)
            elif argumento1 == 'idioma':
                pais = ler_paises()
                if pais:
                    idioma = buscar_idioma(pais)
                    print(idioma)
            elif argumento1 == 'fronteiras':
                pais = ler_paises()
                if pais:
                    fronteiras = buscar_fronteiras(pais)
                    print(fronteiras)
    except Exception as e:
        print(e)





