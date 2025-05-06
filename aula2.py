import pandas as pd

#1º
frutas = pd.Series(["maça", 'Banana', 'Laranja', 'Morango'], index = ['A', 'B', 'C', 'D'])
print(frutas)

precos = pd.Series([2.50, 1.80, 3.20, 4], index = ['A', 'B', 'C', 'D'])
print(precos)

#2º
dados_alunos = {
    'Nome':['Ana', 'Bruno', 'Carla', 'Daniel', 'Elisa'],
    'Idade':[20, 22, 21, 23, 19],
    'Curso': ['Engenharia', "Processo Gerenciais", 'Medicina', 'Direito', 'Biologia']
}
alunos = pd.DataFrame(dados_alunos)
print(alunos)

#3º
print(frutas['C'])
print(alunos['Nome'])
print(alunos[['Nome', 'Curso']])

#4º
id_MaiorIgual = alunos["Idade"] >= 21
print(alunos[id_MaiorIgual])

#5º
alunos['Cidades'] = ['Olinda', 'Peixinho', 'Caixa dágua', 'Alto da Bondade', 'Mirueira']
print(alunos['Cidades'])
remove = alunos.drop('Curso', axis=1)
print(remove)

#6º
vendas_categoria = {
    'Produto': ['A', 'B', 'A', 'C', 'B', 'C', 'A'],
    'Categoria': ['Eletrônicos', 'Vestuário', 'Eletrônicos', 'Alimentos', 'Vestuário', 'Alimentos', 'Eletrônicos'],
    'Valor': [100, 50, 120, 30, 60, 40, 110]
}
df_vendas_cat = pd.DataFrame(vendas_categoria)
df_vendas = df_vendas_cat.groupby(by=['Categoria'])['Valor'].sum()
print(df_vendas)

#8º
alunos['Idade2x'] = alunos['Idade']*2
print(alunos)
