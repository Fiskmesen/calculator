def plus(x, y):
    print(x + y)
def minus(x, y):
    print(x-y)
def multiplicera(x, y):
    print(x*y)

print("Vad vill du göra?")
print("1. Plus")
print("2. Minus")
print("3. gånger")

val = input("Skriv 1/2/3")

num1 = int(input("Skriv det första numret: "))
num2 = int(input("Skriv det andra numret: "))
if val == '1':
    plus(num1, num2)
if val == '2':
    minus(num1, num2)
if val == '3':
    gånger(num1, num2)
