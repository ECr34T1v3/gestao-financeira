import pandas as pd
import matplotlib.pyplot as plt

# Simulação de dados financeiros
data = {
    'transaction_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'transaction_name': ['Groceries', 'Rent', 'Utilities', 'Dining', 'Entertainment', 'Travel', 'Savings', 'Investment', 'Insurance', 'Education'],
    'amount': [150, 800, 200, 50, 100, 300, 200, 500, 100, 150],
    'category': ['Necessities', 'Necessities', 'Necessities', 'Discretionary', 'Discretionary', 'Discretionary', 'Savings', 'Savings', 'Necessities', 'Education'],
    'date': pd.date_range(start='2023-01-01', periods=10, freq='M')
}

# Criação do DataFrame
df = pd.DataFrame(data)

# Visualização dos dados
print("Dados Financeiros:\n", df)

# Função para exibir relatório mensal
def monthly_report(df):
    df['month'] = df['date'].dt.to_period('M')
    monthly_expenses = df.groupby('month')['amount'].sum()
    print("\nDespesas Mensais:\n", monthly_expenses)
    monthly_expenses.plot(kind='bar')
    plt.title('Despesas Mensais')
    plt.xlabel('Mês')
    plt.ylabel('Total de Despesas')
    plt.show()

# Função para exibir relatório por categoria
def category_report(df):
    category_expenses = df.groupby('category')['amount'].sum()
    print("\nDespesas por Categoria:\n", category_expenses)
    category_expenses.plot(kind='pie', autopct='%1.1f%%')
    plt.title('Despesas por Categoria')
    plt.ylabel('')
    plt.show()

# Exibição dos relatórios
monthly_report(df)
category_report(df)

# Salvando o DataFrame para uso futuro
df.to_csv('financial_data.csv', index=False)
