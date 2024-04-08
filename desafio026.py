frase = str(input('Digite um frase:')).strip().upper()
A = 'A'
print('Quantas letras A tem na frasem ? {}'.format(frase.count(A)))
print('O primeiro A está na posição : {}'.format(frase.find(A) + 1))
print('O ultimo a está na posição : {}'.format(frase.rfind(A) + 1))

