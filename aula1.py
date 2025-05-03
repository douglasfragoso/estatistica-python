import pandas as pd

#Series
idades = pd.Series([25,30,46,58])

print(idades)
print(idades.index)
print(idades.values)

idades = pd.Series([25,30,46,58], index=['Ana', 'Joao', 'Paulo', 'Lucas'])
print(idades)
print(idades['Ana'])

#DataFrame
dados = {'Nome' : ['Alice', 'Bob', 'Charlie', 'Paulo'],
         'Idade' : [15, 55, 66, 77]}

idades = pd.DataFrame(dados)
print(idades)
print(idades['Nome'])
print(idades[['Nome', 'Idade']])

maior_de_idade = idades['Idade'] > 18
print(maior_de_idade)
print(idades[idades['Idade']>18])

idades['Cidade']=['Recife', 'Olinda', 'Ct', 'm1' ]
print(idades)

idades = idades.drop('Idade', axis=1)
print(idades)

idades = idades.drop(2, axis=0)
print(idades)

print(idades.describe())

#Import de arquivos
funcionarios = pd.read_csv('funcionario.csv')
print(funcionarios)
print(funcionarios.tail())
print(funcionarios.head())

funcionarios = pd.read_excel('funcionario.xlsx', sheet_name='nome')
print(funcionarios)