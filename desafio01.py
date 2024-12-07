
# Cadastro do usuario
nome_usuario = input("Digite o seu nome")
salario_usuario = float(input("Digite seu salario:"))
perct_bonus =  float(input("Digite seu bonus:"))

#KPI para bonus
total_bonus = 1500 + salario_usuario * perct_bonus

#Mensagem final]
print(f'Olá {nome_usuario}, seu bônus é de: {total_bonus}') 