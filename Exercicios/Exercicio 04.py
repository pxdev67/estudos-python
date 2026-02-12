def soma(a, b):
    return a + b
def sub(a, b):
    return a - b
def multi(a, b):
    return a * b
def div(a, b):
    if b != 0:
        return a / b
    else:
        return 'Nao e possivel divir por zero'
operacao = (input('Digite qual a sua operacao +,-,*,/'))
num1 = float(input("Escolha o primeiro numero:"))
num2 = float(input('Escolha o segundo numero:'))

if operacao == '+':
    print(soma(num1, num2))
elif operacao == '-':
    print(sub(num1, num2))
elif operacao == '*':
        print(multi(num1, num2))
elif operacao == '/':
         print (div(num1, num2))
else:
     print('operação invalida')

       


