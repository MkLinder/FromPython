nome = input('Qual o seu nome?')
if nome == 'Mike':
    print('Que nome bonio!')
elif nome == 'Pedro' or nome == 'Maria':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Ana Claudia Juliana':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem comum')
print('Tenha um bom dia, {}.'.format(nome))