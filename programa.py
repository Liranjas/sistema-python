cont=0
for i in range(10):
  num=int(input("Digite um valor:"))
  if num<0:
    cont=cont+1

print(f"Foram digitados: {cont} números negativos")