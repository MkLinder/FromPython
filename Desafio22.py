nome = str(input('Digite seu nome completo:')).strip() #strip() serve para já eliminar possíveis espaços na contagm de caracteres
print('Analisando seu nome...')
print('Seu nome em maíusculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem {} caracteres'.format(len(nome) - nome.count(' ')))  # -nome.count(' ') Elimina a contagem de espaços entre caracteres
print('Seu primeiro nome tem {} caracteres'.format(nome.find(' ')))  # Desta forma ele encontrará a posição do primeiro espaço entre palavras
                                                                     # que coincidentemente será o mesmo valor de quantidade de caracteres do
                                                                     # primeiro nome.
# Outra forma de contar somente o primeiro nome:
separa = nome.split() #Cria uma lista separando cada nome.
print('Seu primeiro nome é {} e ele tem {} caracteres'.format(separa[0], len(separa[0])))
