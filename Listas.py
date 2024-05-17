#problema 1
#def encontrar_mayor(precios):
#    return max(precios)

#def encontrar_menor(precios):
#    return min(precios)

#precios = [50, 75, 46, 22, 80, 65, 8]

#print("El menor precio es: ", encontrar_menor(precios))
#print("El mayor precio es: ", encontrar_mayor(precios))




#Problema 2
#abecedario =[chr(i) for i in range(97, 123)]

#abecedario = [letra for indice, letra in enumerate (abecedario, 1) if indice % 3 != 0]

#print(abecedario)}


#Problema 3 
lista_palabras = []


palabra = input("Ingresa una palabra para añadir a la lista (escribe 'fin' para terminar): ")
while palabra.lower() != 'fin':
    lista_palabras.append(palabra)
    palabra = input("Ingresa otra palabra (o escribe 'fin' para terminar): ")


palabra_buscar = input("¿Qué palabra quieres buscar en la lista? ")


contador = lista_palabras.count(palabra_buscar)
print(f"La palabra '{palabra_buscar}' aparece {contador} veces en la lista.")