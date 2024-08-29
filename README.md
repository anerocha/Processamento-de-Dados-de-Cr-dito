# Processamento de Dados de Crédito

Este projeto foi desenvolvido como parte do curso de **Analista de Dados da EBAC**. Ele demonstra como processar dados de um arquivo Excel para extrair informações específicas, como criar um CSV e um JSON a partir dos dados filtrados.

## Objetivo

O objetivo principal é entender o comportamento dos clientes inadimplentes com base em atributos como escolaridade, estado civil, tipo de cartão, entre outros.

## Descrição das Etapas

### 1. Excel para CSV
- Utiliza o pacote `pandas` para ler o arquivo Excel.
- Filtra os clientes que são inadimplentes (`default = 1`) e solteiros (`estado_civil = 'solteiro'`).
- Extrai as colunas `id`, `sexo` e `idade` e salva os dados em um arquivo CSV (`credito.csv`) separado por ponto e vírgula (`;`).

### 2. Excel para JSON
- Extrai as colunas `escolaridade` e `tipo_cartao`, removendo duplicados.
- Cria um dicionário Python com as informações extraídas e o converte para JSON.
- Salva o dicionário em um arquivo JSON (`credito.json`).

## Tecnologias Utilizadas

- Python
- Pandas
- JSON

## Como Executar

1. Clone este repositório.
2. Certifique-se de ter o Python instalado (recomendado 3.7+).
3. Instale as bibliotecas necessárias:
   ```bash
   pip install pandas

 ## OBSERVAÇÕES
Este projeto é um exercício básico para entender manipulação de dados em Python.
Como iniciante, o foco principal foi aprender e aplicar as funcionalidades básicas de manipulação de dados com pandas e json.
