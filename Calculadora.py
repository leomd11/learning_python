# Calculadora Simples

print("Selecione o número da operação desejada: \n\n 1 - Soma \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n")

opert = int(input("Digite sua opção (1/2/3/4): "))

num1 = float(input("Digite o primeiro número: "))

num2 = float(input("Digite o segundo número: "))
print("\n")

if opert == 1:
    soma = num1 + num2
    print("%s + %r =" %(num1,num2), soma) 
elif opert == 2:
    sub = num1 - num2
    print("%s - %r =" %(num1,num2), sub) 
elif opert == 3:
    multi = num1 * num2
    print("%s x %r =" %(num1,num2), multi) 
else:
    div = round(num1 / num2, 2)
    print("%s / %r =" %(num1,num2), div)
