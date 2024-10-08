# -*- coding: utf-8 -*-
"""Exercício_Python_1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/133XOx3cHZufO-apic2o3PVg-wM0-8hkT

**Exercício 1 - Aquecimento de Python para Ciência de Dados**

1. Imprima "Hello, World!" no console.
"""

print ("Hello, World!")

"""2. Crie uma variável x com valor 10 e imprima seu valor."""

x = 10

print (x)

"""3. Some dois números e exiba o resultado."""

num1 = 10
num2 = 15


resultado = num1 + num2


print("A soma de", num1, "e", num2, "é:", resultado)

"""4. Verifique se um número é par ou ímpar.

"""

numero = 7

if numero % 2 == 0:
    print(f"{numero} é par.")
else:
    print(f"{numero} é ímpar.")

"""5. Crie uma função que receba dois números e retorne a soma deles."""

def somar(num1, num2):
    return num1 + num2


resultado = somar(10, 15)
print("A soma é:", resultado)

"""6. Crie uma lista com os números de 1 a 5 e imprima-a.

"""

numeros = [1, 2, 3, 4, 5]


print(numeros)

"""7. Adicione o número 6 à lista criada na questão anterior.

"""

numeros = [1, 2, 3, 4, 5]


numeros.append(6)


print(numeros)

"""8. Remova o número 3 da lista."""

numeros = [1, 2, 3, 4, 5, 6]


numeros.remove(3)


print(numeros)

"""9. Acesse o terceiro elemento da lista."""

numeros = [1, 2, 4, 5, 6]

terceiro_elemento = numeros[2]

print("O terceiro elemento é:", terceiro_elemento)

"""10. Imprima o tamanho da lista."""

numeros = [1, 2, 4, 5, 6]

tamanho = len(numeros)
print("O tamanho da lista é:", tamanho)

"""11. Crie um dicionário com informações de um carro (marca, modelo, ano)."""

carro = {
    "marca": "Lamborghini",
    "modelo": "Gallardo",
    "ano": 2020
}

print(carro)

"""12. Acesse o valor associado à chave "marca" no dicionário."""

carro = {
    "marca": "Lamborghini",
    "modelo": "Gallardo",
    "ano": 2020
}


marca = carro["marca"]


print("A marca do carro é:", marca)

"""13. Adicione uma nova chave "cor" com valor "preto" ao dicionário."""

carro = {
    "marca": "Lamborghini",
    "modelo": "Gallardo",
    "ano": 2020
}


carro["cor"] = "preto"


print(carro)

"""14. Verifique se a chave "modelo" existe no dicionário.

"""

carro = {
    "marca": "Lamborghini",
    "modelo": "Gallardo",
    "ano": 2020
}


if "modelo" in carro:
    print("A chave 'modelo' existe no dicionário.")
else:
    print("A chave 'modelo' não existe no dicionário.")

"""15. Itere sobre as chaves do dicionário e imprima cada uma delas."""

carro = {
    "marca": "Lamborghini",
    "modelo": "Gallardo",
    "ano": 2020
}

chaves = carro.keys()

for chave in chaves:
    print(chave)

"""15. Itere sobre as chaves do dicionário e imprima cada uma delas."""

carro = {
    "marca": "Lamborghini",
    "modelo": "Gallardo",
    "ano": 2020,
    "cor": "preto"
}

for chave in carro:
    print(chave)

"""17. Crie uma função que receba uma lista e retorne a soma dos elementos."""

def somar_elementos(lista):
    return sum(lista)

numeros = [1, 2, 3, 4, 5]
resultado = somar_elementos(numeros)
print("A soma dos elementos é:", resultado)

"""18. Crie uma função que receba um dicionário e retorne todas as suas chaves.

"""

def obter_chaves(dicionario):
    return list(dicionario.keys())


carro = {
    "marca": "Lamborghini",
    "modelo": "Gallardo",
    "ano": 2020,
    "cor": "preto"

}

chaves = obter_chaves(carro)
print("As chaves do dicionário são:", chaves)

"""
19. Crie uma função que receba um dicionário e imprima chave e valor em linhas separadas."""

def imprimir_chaves_valores(dicionario):
    for chave, valor in dicionario.items():
        print(f"Chave: {chave}, Valor: {valor}")


carro = {
    "marca": "Lamborghini",
    "modelo": "Gallardo",
    "ano": 2020,
    "cor": "preto"
}

imprimir_chaves_valores(carro)

"""20. Crie uma classe chamada Pessoa com atributos nome e idade, e um método que imprima esses dados."""

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def imprimir_dados(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")


pessoa1 = Pessoa("Hester", 23)
pessoa1.imprimir_dados()