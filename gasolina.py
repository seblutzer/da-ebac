import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Leitura do arquivo csv
df = pd.read_csv('gasolina.csv')

# Configurações do gráfico
sns.set_style('whitegrid')
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(x='dia', y='venda', data=df, ax=ax)
plt.title('Preço da Gasolina')
plt.xlabel('Dia')
plt.ylabel('Preço (R$)')

# Salvando o gráfico
plt.savefig('gasolina.png')
