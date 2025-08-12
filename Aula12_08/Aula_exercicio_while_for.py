

for x in range(1, 11):
    print(x)

############################################

numero = int(input("Digite um numero"))    
for C in range (1, 11):
    print(f'{numero} x {C} = {numero * C}')

################################################################

num = 0
while True: 
    soma = int(input("Digite um num"))    
    if soma == 0:
        print(num)
        break
    else:
        num = num + soma


