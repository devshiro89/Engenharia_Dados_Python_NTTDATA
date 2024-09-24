#A função builtin input é utilizada quando queremos ler dados da entrada padrão (teclado). Ela recebe um argumento do tipo string, que é exibido para o usuário na saída
#padrão (tela). A função ê a entrada, converte para string e retorna o valor.

nome = input ("Digite o seu nome: ")
print(f"Seja bem vindo {nome}")

#A função builtin print é utilizada quando queremos exibir dados na saída padrão (tela). Ela recebe um argumento obrigatório do tipo varargs de objetos e 4 argumentos opcionais
#(sep, end, file e flush). Todos os objetos são convertidos para string, separado por sep e terminados por end. A string final é exibida para o usuário.
#end é usado no final de um print, como final de uma saída string.
#sep é usado como o separador entre as strings.

nome = "Luiz"
sobrenome = "Shiraishi"

print(nome, sobrenome)
print(nome, sobrenome, end="... \n")
print(nome, sobrenome, sep="#")