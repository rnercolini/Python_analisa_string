# Analisa em uma string quantas vezes aparece a letra a e sua posição.
frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra "a" aparece {} vezes na frase'.format(frase.count('A')))
print('A posição da primeira letra "a" é {}'.format(frase.find('A') + 1))
print('A posição da última letra "a" é {}'.format(frase.rfind('A') + 1))
