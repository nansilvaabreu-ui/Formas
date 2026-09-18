notas = [7.0, 1.5, 10.0, 8.5, 3.0, 5.5]

# contador = 0
# limite = len(notas) -1
# print(limite)
# while contador <= limite:
#     print (f" Sua nota é: {notas[contador]}")
#     contador += 1

notas.append(7.7)
notas.pop(1)
notas.remove(1.5)
notas[2] = "0.0"
print = notas .index(8.5)
for x in notas:
    print(f"Sua nota é: {x}")