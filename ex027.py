'''Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.'''
n = str(input('Escreva o seu nome completo: ')).strip().upper()
nome = n.split(' ')
print('Seu primeiro nome é: {}'.format(nome[0]))
print('Seu ultimo sobrenome é: {}'.format(nome[len(nome)-1]))
