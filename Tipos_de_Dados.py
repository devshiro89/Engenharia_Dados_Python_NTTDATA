##########                                       Variáveis                          ###############################
# Exemplo da aplicação de variáveis age e name, os valores se alteram conforme necessidade do executável
age = 35
name = 'Luiz'
print(f'Meu nome é {name} e tenho {age} anos.')


name, age = ('Tatianny' , 31)
print(f'Meu nome é {name} e tenho {age} anos.')





##########                                       Constantes                         ###############################
#Exemplo da aplicação de constantes, os valores das constantes diferentemente das variáveis não se altera ao longo do processo.
#Usa-se como convenção de que TODAS Constantes na linguagem python deve-se ser escrita toda em caixa alta por limitação da linguagem não ter essa função em específico.

salario = 4000,00
IMPOSTO_INSS_MAX = 14

print(f'O valor do salário é de R$ {salario} e o imposto aplicado de INSS é no total de {IMPOSTO_INSS_MAX} %')

