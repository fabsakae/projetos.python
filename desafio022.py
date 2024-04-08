nome = str(input('digite seu nome completo:')).strip()
print('Analisando seu nome....')
print('Seu nome em letras maiúsculas é {}'.format(nome.upper()))
print('Seu nome em letras minúsculas é {}'.format(nome.lower()))
# print(nome.replace(' ', '')) #substitui o espaço por sem espaço
nomeid = (nome.replace(' ', '')) #criei uma nova variavel que substitui o espaço por sem espaço
print('Seu nome possui {} letras'.format(len(nomeid))) #dessa forma tbm conta sem o espaço
print('seu nome possui {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print(separa)
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
