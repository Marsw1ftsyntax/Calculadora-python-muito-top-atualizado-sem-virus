import math as m 
operaçao = input("Escolha a operação (+, -, *, /, $): ")
numero = input("Digite um numero: ")
numero2 = input("Caso seja raiz quadrada ignore Digite outro numero: ")

try:
    numero=int(numero)
    numero2=int(numero2)
except:
    print("Cade o numero otalu?")
    exit()

if operaçao == "+":
    print(f"A soma é: {numero + numero2}")
elif operaçao == "-":
    print(f"A subtração é: {numero - numero2}")
elif operaçao == "*":
    print(f"A multiplicação é: {numero * numero2}")
elif operaçao == "/":
    print(f"A divisão é: {numero / numero2}")
elif operaçao == "$":
    print(f"A Raiz quadrada é: {m.sqrt(numero)}")
else:
    print("Cadeeeeeeee")
