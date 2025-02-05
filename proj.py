#Análise de inadimplência

#Contexto:
#Ao se avaliar cada variável percebe-se a sua relação com a inadimplência. A idade, por exemplo, pode indicar se o cliente já está 
#aposentado(com mais estabilidade financeira e menos chance de se tornar inadimplente) ou não(sem tanta estabilidade e com maior 
#chance de se tornar inadimplente). Já em relação a renda mensal e o valor do empréstimo: pode-se observar o quanto a renda é maior
#do que o valor do empréstimo para saber se há possibilidade dele pagar( o empréstimo equivale a quanto por cento da renda?).Ademais,
#outras variáveis como tempo de emprego, parcelas e score também influenciam no risco de inadimplência.
#Outrossim, em relação a análise em si: a análise dos dados foi iniciada por meio da limpeza daqueles que são nulos ou que estão
#duplicados juntamente com a a verificação da existência ou não de outliers. Após isso, iniciei a parte de "Treino e Teste", 
#utilizando a variável inadimplente(1 para inadimplente, 0 para não inadimplente) como target(Y). Posteriormente, executei o 
#SelectKBest(score_func=f_classif) para saber quais eram os recursos mais relevantes para analisar se o cliente é inadimplente 
#ou não, seguido da visualização das relações entre a variável "inadimplente" e as demais através do heatmap. Por fim, utilizei
#a regressão logística(modelo de classificação) para determinar a probabilidade do evento "inadimplente" acontecer(correspondente=1)
#ou não(correspondente=0); o que foi confirmado pela matriz de confusão e acurácia.

#O problema analisado ao longo do projeto é a necessidade de se verificar a chance de outros clientes se tornarem inadimplentes, 
#prejudicando assim a empresa do setor financeiro que foi avaliada. Dessa forma, vê-se necessário,por meio do Machine Learning,
#averiguar se outros clientes se tornarão inadimplentes ou não, levando em conta as variáveis: idade, renda, tempo de emprego, 
#valor do empréstimo, parcelas mensais e score de 1.029 clientes. Sendo assim, ao verificar quais são os clientes que podem também 
#se tornar inadimplentes, a empresa poderá tomar as ações cabíveis para evitar que isso aconteça.


#Importações:
#import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt
#import seaborn as sns
#from sklearn.model_selection import train_test_split
#from sklearn.metrics import r2_score
#from sklearn.feature_selection import SelectKBest
#from sklearn.datasets import load_digits
#from sklearn.feature_selection import f_classif
#from sklearn.model_selection import train_test_split
#from sklearn.linear_model import LogisticRegression
#from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


#Upload dos dados
dados =  pd.read_csv(r'C:\Users\Usuario\Downloads\dados_inadimplencia.csv')

#Visualizar primeiras linhas e a descrição

dados.head()

dados.describe()

#Limpeza de nulos e duplicados

dados.isnull().sum()
dados = dados.dropna()
dados
dados.isnull().sum()


print(dados.duplicated)
dados.drop_duplicates(keep='first', inplace=False )
print(dados.duplicated)

#Detecção de outliers
#Na Idade
q1 = np.percentile(dados['idade'], 25)
q3 = np.percentile(dados['idade'], 75)
iqr = q3 - q1
threshold = 1.5 * iqr
outliers = np.where((dados['idade'] < q1 - threshold) | (dados['idade'] > q3 + threshold))
print(outliers)
#Na Renda Mensal
q1 = np.percentile(dados['renda_mensal'], 25)
q3 = np.percentile(dados['renda_mensal'], 75)
iqr = q3 - q1
threshold = 1.5 * iqr
outliers = np.where((dados['renda_mensal'] < q1 - threshold) | (dados['renda_mensal'] > q3 + threshold))
print(outliers)
#No Tempo emprego
q1 = np.percentile(dados['tempo_emprego'], 25)
q3 = np.percentile(dados['tempo_emprego'], 75)
iqr = q3 - q1
threshold = 1.5 * iqr
outliers = np.where((dados['tempo_emprego'] < q1 - threshold) | (dados['tempo_emprego'] > q3 + threshold))
print(outliers)
#Na Valor empréstimo
q1 = np.percentile(dados['valor_emprestimo'], 25)
q3 = np.percentile(dados['valor_emprestimo'], 75)
iqr = q3 - q1
threshold = 1.5 * iqr
outliers = np.where((dados['valor_emprestimo'] < q1 - threshold) | (dados['valor_emprestimo'] > q3 + threshold))
print(outliers)
#Nas Parcelas mensais
q1 = np.percentile(dados['parcelas_mensais'], 25)
q3 = np.percentile(dados['parcelas_mensais'], 75)
iqr = q3 - q1
threshold = 1.5 * iqr
outliers = np.where((dados['parcelas_mensais'] < q1 - threshold) | (dados['parcelas_mensais'] > q3 + threshold))
print(outliers)
#No Score crédito
q1 = np.percentile(dados['score_credito'], 25)
q3 = np.percentile(dados['score_credito'], 75)
iqr = q3 - q1
threshold = 1.5 * iqr
outliers = np.where((dados['score_credito'] < q1 - threshold) | (dados['score_credito'] > q3 + threshold))
print(outliers)


#Visualização de informações sobre a idade
idade_min = dados['idade'].min()
idade_max = dados['idade'].max()
categorias = ['Idade Miníma', 'Idade Máxima']
valores = [idade_min, idade_max]
plt.bar(categorias, valores, color=['blue', 'green'])
plt.xlabel('Categoria')
plt.ylabel('Idade')
plt.title('Variação entre idades mínima e máxima')
plt.show()


#Visualização de informações sobre a renda
renda_min = dados['renda_mensal'].min()
renda_max = dados['renda_mensal'].max()
categorias = ['Renda Miníma', 'Renda Máxima']
valores = [renda_min, renda_max]
plt.bar(categorias, valores, color=['blue', 'green'])
plt.xlabel('Categoria')
plt.ylabel('Renda')
plt.title('Variação entre rendas mínima e máxima')
plt.show()


#Visualização de informações sobre o tempo de emprego
tempo_min = dados['tempo_emprego'].min()
tempo_max = dados['tempo_emprego'].max()
categorias = ['Tempo de Emprego Minímo', 'Tempo de Emprego Máximo']
valores = [tempo_min, tempo_max]
plt.bar(categorias, valores, color=['blue', 'green'])
plt.xlabel('Categoria')
plt.ylabel('Tempo')
plt.title('Variação entre tempo de emprego mínimo e máximo')
plt.show()


#Visualização de informações sobre os valores do empréstimo
emprestimo_min = dados['valor_emprestimo'].min()
emprestimo_max = dados['valor_emprestimo'].max()
categorias = ['Empréstimo Minímo', 'Empréstimo Máximo']
valores = [emprestimo_min, emprestimo_max]
plt.bar(categorias, valores, color=['blue', 'green'])
plt.xlabel('Categoria')
plt.ylabel('Empréstimo')
plt.title('Variação entre empréstimo mínima e máxima')
plt.show()




#Visualização de informações sobre as parcelas mensais
parcela_min = dados['parcelas_mensais'].min()
parcela_max = dados['parcelas_mensais'].max()
categorias = ['Parcela Miníma', 'Parcela Máxima']
valores = [parcela_min, parcela_max]
plt.bar(categorias, valores, color=['blue', 'green'])
plt.xlabel('Categoria')
plt.ylabel('Parcela')
plt.title('Variação entre parcelas mínima e máxima')
plt.show()


#Visualização de informações sobre o score de crédito
score_min = dados['score_credito'].min()
score_max = dados['score_credito'].max()
categorias = ['Score Minímo', 'Score Máximo']
valores = [score_min, score_max]
plt.bar(categorias, valores, color=['blue', 'green'])
plt.xlabel('Categoria')
plt.ylabel('Score')
plt.title('Variação entre score mínimo e máximo')
plt.show()





#Treino e teste

X = dados.drop('inadimplente', axis=1)
y = dados['inadimplente']
X_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Seleção de características usando f_classif 
select_k_best = SelectKBest(score_func=f_classif, k=3)
x_train_k_best = select_k_best.fit_transform(X_train, y_train)

# Exbição das características selecionadas que mais influenciam o "inadimplente"

selected_features = X_train.columns[select_k_best.get_support()]
print("Selected features:", selected_features)


#Observação das correlações
print(dados.corr())

#Exposição das correlações por meio do hatmap

corrmat = dados.corr()
top_corr_features = corrmat.index
plt.figure(figsize=(20,20))
g=sns.heatmap(dados[top_corr_features].corr(),annot=True,cmap="RdYlGn")
plt.show()



#Regressão logística para saber a possível inadimplência

pd.set_option('display.max_rows', None)
dados

dados.head()
classifier = LogisticRegression(max_iter=1000)
classifier.fit(X_train, y_train)

#Adiciona os valores de idade, renda_mensal, tempo_emprego, dentre outros, no espaço abaixo
print(classifier.predict([[]]))

y_pred = classifier.predict(x_test)

#Matriz de confusão
cm = confusion_matrix(y_test, y_pred)
print('Matriz de Confusão')
print(cm)


#Acurácia
accuracy = accuracy_score(y_test, y_pred)
print(f'Acurácia: {accuracy:.2f}')

#Relatório da classificão
cr = classification_report(y_test, y_pred)
print('Relatório de Classificação')
print(cr)



