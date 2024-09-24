preco = 10
print (preco)
#10

#Convertendo para float
preco = float(preco)
print(preco)
#10.0

preco = 10/2
print(preco)
#5.0

#Convertendo para int
preco = int(preco)
print(preco)
#5

#No calculo de divisão em python, se o operador for com uma barra / trará
#um resultado em FLOAT, se fizer com duas barras // trará o resultado em INT.

preco = 10.50
idade = 28

#Convertendo para string
preco = str(preco)
idade = str(idade)

texto = f'idade {idade} preco {preco}'
print(texto)

#Conversão de string para número

preco = '10.50'
idade = '28'

print(float(preco))
print(int(idade))

#Comando type retorna qual classe é o objeto

valor = 10
valor_str = str(valor)
print(type(valor))
print(type(valor_str))