num = int(input("Digite um número: "))

if num < 0:
    print("O número deve ser maior ou igual a 0: ")
    num = int(input("Digite um número: "))
for i in range (1, num + 1):
    print(" ", i)   