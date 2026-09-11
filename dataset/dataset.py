import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

tips.to_csv('./csv/tips.csv', index=False)

print('Formato do dataset (linhas, colunas):', tips.shape)

print('Primeiras 5 linhas')

print(tips.head())

print('=' * 50)

print()

print('Últimas 5 linhas')

print(tips.tail())

print('=' * 50)

print('1. INFO GERAL (tipos de dados)')

print('=' * 50)

tips.info()

print()

print('=' * 50)

print('2. VALORES NULOS POR COLUNA')

print('=' * 50)

print(tips.isnull().sum())

print()

print('=' * 50)

print('3. ESTATÍSTICAS DESCRITIVAS (colunas numéricas)')

print('=' * 50)

print(tips.describe())

print('=' * 50)


	


