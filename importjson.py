import json

dados = {
    "palavras": ["Hester", "Kariny", "Kath", "Guilherme"]
}

def verifica_palavra(dados, palavra):
    palavras = dados.get('palavras', [])

    if palavra in palavras:
        return f'A palavra "{palavra}" foi encontrada.'
    else:
        return f'A palavra "{palavra}" não foi encontrada.'

resultado = verifica_palavra(dados, 'Hester')
print(resultado)

resultado = verifica_palavra(dados, 'Guilherme')
print(resultado)