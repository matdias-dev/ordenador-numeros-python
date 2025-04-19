print("Esse algoritmo organiza os números em forma crescente")
print("Digite o número A: ")
numberA = int(input())

print("Digite o número B: ")
numberB = int(input())

print("Digite o número C: ")
numberC = int(input())
print(" ")

if numberA < numberB and numberB < numberC:
    print(numberA)
    print(numberB)
    print(numberC)
elif numberA < numberC and numberC < numberB:
    print(numberA)
    print(numberC)
    print(numberB)
elif numberB < numberA and numberA < numberC:
    print(numberB)
    print(numberA)
    print(numberC)
elif numberB < numberC and numberC < numberA:
    print(numberB)
    print(numberC)
    print(numberA)
elif numberC < numberA and numberA < numberB:
    print(numberC)
    print(numberA)
    print(numberB)
elif numberC < numberB and numberB < numberA:
    print(numberC)
    print(numberB)
    print(numberA)
else:
    print("Alguns números podem ser iguais. Tente novamente.")
    
#123
#132
#213
#231
#312
#321