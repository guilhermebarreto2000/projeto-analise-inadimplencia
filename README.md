# Análise de Inadimplência

![Image](https://github.com/user-attachments/assets/88712f90-0757-4185-84bf-3e9ad5d95218)

# Descrição:

 Esse projeto utiliza o Machine Learning, especificamente a parte de Feature Selection e Logistic Regression, para determinar as variáveis que mais influenciam na inadimplência e verificar  se o cliente é inadimplente ou não com base no preenchimento dessas variáveis.
 A análise dos dados foi iniciada por meio da limpeza daqueles que são nulos ou que estão duplicados juntamente com a a verificação da existência ou não de outliers. Após isso, iniciei a parte de "Treino e Teste", utilizando a variável inadimplente(1 para inadimplente, 0 para não inadimplente) como target(Y). 
 Posteriormente, executei o SelectKBest(score_func=f_classif) para saber quais eram os recursos mais relevantes para analisar se o cliente é inadimplente ou não, seguido da visualização das relações entre a variável "inadimplente" e as demais através do heatmap. 
 Por fim, utilizei a regressão logística(modelo de classificação) para determinar a probabilidade do evento "inadimplente" acontecer(correspondente=1) ou não(correspondente=0); o que foi confirmado pela matriz de confusão e acurácia.
 
# Tecnologias:

 As tecnologias usadas foram Python(Pandas, Numpy, Matplotlib, Seaborn e Scikit-learn), Machine Learning(Feature Selection e Logistic Regression) e o Visua Studio Code(ambiente de desenvolvimento do proeto)


# Problema e objetivo:
 O problema analisado ao longo do projeto é a quantidade de clientes que estão inadimplentes, prejudicando assim a empresa do setor financeiro que foi avaliada. Dessa forma, vê-se necessário analisar por meio do Machine Learning averiguar se outros clientes se tornarão inadimplentes ou não, levando em conta as variáveis: idade, renda, tempo de emprego, valor do empréstimo, parcelas mensais e score de 1.029 clientes. Sendo assim, ao verificar quais são os clientes que podem também se tornar inadimplentes, a empresa poderá tomar as ações cabíveis para evitar que isso aconteça.
 

# Variações dos atributos:

Idade \
![Image](https://github.com/user-attachments/assets/e48110f5-3948-4304-9727-f37dfba6c9d6)  \
Renda Mensal  \
![Image](https://github.com/user-attachments/assets/f33dcc40-ca09-458c-929d-06656bcc602c)
Tempo de emprego  \
![Image](https://github.com/user-attachments/assets/1df009ba-f9aa-4a57-9c9d-66eba4f85b02)
Valor de empréstimo  \
![Image](https://github.com/user-attachments/assets/af8959a8-3054-44a0-8504-633cb7bdf3f4)
Parcelas mensais  \
![Image](https://github.com/user-attachments/assets/cd275c99-2c25-4297-a263-46d1559c8bfd)
Score de crédito  \
![var_score](https://github.com/user-attachments/assets/7d77b63b-c33d-42cb-a782-11c64d14793d)









