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

