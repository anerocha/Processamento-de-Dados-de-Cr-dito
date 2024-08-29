# Instale as bibliotecas necessárias, caso ainda não tenha
# !pip install pandas openpyxl

import pandas as pd
import json

# URL do arquivo Excel
file_url = 'https://raw.githubusercontent.com/andre-marcos-perez/ebac-course-utils/main/dataset/credito.xlsx'

# Carregar o arquivo Excel para um DataFrame
df = pd.read_excel(file_url)

# 1º Exercício: Excel para CSV
# Filtrar os clientes inadimplentes (default = 1) e solteiros (estado_civil = 'solteiro')
df_filtered = df[(df['default'] == 1) & (df['estado_civil'] == 'solteiro')]

# Selecionar as colunas id, sexo e idade
df_result = df_filtered[['id', 'sexo', 'idade']]

# Salvar o resultado no arquivo credito.csv com o separador ;
df_result.to_csv('credito.csv', sep=';', index=False)
print("Arquivo 'credito.csv' criado com sucesso.")

# 2º Exercício: Excel para JSON
# Extrair dados das colunas 'escolaridade' e 'tipo_cartao' removendo duplicados
escolaridade = list(set(df['escolaridade'].dropna()))
tipo_cartao = list(set(df['tipo_cartao'].dropna()))

# Criar o dicionário com as listas extraídas
credito = {
    'tipo_cartao': tipo_cartao,
    'escolaridade': escolaridade
}

# Converter o dicionário para JSON
credito_json = json.dumps(credito, indent=4)
print("Dicionário de crédito convertido para JSON:")
print(credito_json)

# Salvar o JSON em um arquivo
with open('credito.json', 'w') as json_file:
    json_file.write(credito_json)
print("Arquivo 'credito.json' criado com sucesso.")
