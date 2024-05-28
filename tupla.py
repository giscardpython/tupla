
# lista podes mudar os itens
lista_frutas = ['Maçã', 'Uva', 'Laranja']
print(lista_frutas)

# isto é uma tupla
tupla_frutas = ('Maçã', 'Uva', 'Laranja')
print(tupla_frutas)

# Listar valores Tupla em um loop
tupla_frutas = ('Maçã', 'Uva', 'Laranja', 'Mamão', 'Melão', 'Pêra')
for fruta in tupla_frutas:
    print(fruta)

# Consulta Tupla na posição X
tupla_frutas = ('Maçã', 'Uva', 'Laranja', 'Mamão', 'Melão', 'Pêra')
print(tupla_frutas[2])    

# Pesquisa na Tupla
tupla_frutas = ('Maçã', 'Uva', 'Laranja', 'Mamão', 'Melão', 'Pêra')
fruta = input('Informe o nome da fruta que deseja encontrar: ')
if fruta in tupla_frutas:
    print(fruta)
else:
    print(f'{fruta} não encontrada.')

# Join
tupla_frutas = ('Maçã', 'Uva', 'Laranja', 'Mamão', 'Melão', 'Pêra')
separador = ','
frutas_string = separador.join(tupla_frutas)
print(frutas_string)    

# Ordenar
tupla_frutas = ('Maçã', 'Uva', 'Laranja', 'Mamão', 'Melão', 'Pêra')
frutas_ordenadas = sorted(tupla_frutas)
for fruta in frutas_ordenadas:
print(fruta)