import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('gasolina.csv')
df['dia'] = pd.to_datetime(df['dia'])
sns.set_style('whitegrid')
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x='dia', y='venda', data=df, ax=ax)
plt.title('Preço da Gasolina')
plt.xlabel('Dia')
plt.ylabel('Preço (R$)')
plt.savefig('gasolina.png')
