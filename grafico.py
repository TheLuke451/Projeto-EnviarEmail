import pandas as pd
import matplotlib.pyplot as plt
from google.colab import drive

# Monte o Google Drive
drive.mount('/content/drive')

# Caminho para a sua planilha no Google Drive
# Substitua 'Meu Drive/NomeDaSuaPasta/NomeDaSuaPlanilha.xlsx' pelo caminho real
caminho_planilha = '/content/exemplo_automacao.xlsx'

try:
    # Leia a planilha para um DataFrame do pandas
    df = pd.read_excel(caminho_planilha)

    # Exiba as primeiras linhas do DataFrame para verificar se a leitura foi bem-sucedida
    print("DataFrame lido com sucesso:")
    display(df.head())

    # Exemplo de criação de um gráfico simples (substitua conforme a sua necessidade)
    # Este exemplo cria um gráfico de barras da coluna 'Idade'
    plt.figure(figsize=(8, 6))
    plt.bar(df['Nome'], df['Idade'])
    plt.xlabel('Nome')
    plt.ylabel('Idade')
    plt.title('Idade por Nome')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

except FileNotFoundError:
    print(f"Erro: O arquivo '{caminho_planilha}' não foi encontrado no Google Drive.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")