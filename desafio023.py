#fazer como uma string
#num = int(input('Digite um número de 0 a 9999:'))
#n = str(num)
#print('unidade : {}\ndezena  : {}\ncentena : {}\nmilhar  : {}'.format(n[3], n[2], n[1], n[0]))

#ou pode fazer como numero inteiro usando matematica
num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('analisando o número: {}'.format(num))
print('unidade : {}\ndezena  : {}\ncentena : {}\nmilhar  : {}'.format(u, d, c, m))
