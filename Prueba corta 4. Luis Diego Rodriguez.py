def calculadora(lista, operacion):
    total = 0
    if(lista == []):
        return []
        
    if(operacion == "suma"):
        for elemento in lista:
            total += elemento
        return total
    elif(operacion == "multiplicacion"):
        total = 1
        for elemento in lista:
            total = total * elemento
        return total
    elif(operacion == "promedio"):
        cantidadDigitos = 0
        lista2 = lista 
        while(lista2 != []):
            cantidadDigitos += 1
            lista2 = lista2[1:]
        for elemento in lista:
            total += elemento
        total = total / cantidadDigitos
        return total

#print(calculadora([1,2,3,4,5], "suma"))


def sustituir(sublista,caracter,lista):
    lista2 = []
    if(sublista  == [] or lista == []):
        return []
    for elemento in lista:
        if(elemento in sublista):
           lista2.append(caracter)
        else:
            lista2.append(elemento)
    return lista2

#print(sustituir(["a","b","c"], "x", ["a","t","u","b","c"]))


def repetir(numero, caracter, lista):
    lista2 = []
    numero2 = numero
    if(lista == []):
        return []
    for elemento in lista:
        if(elemento == caracter):
            while(numero2 != 0):
                lista2.append(caracter)
                numero2 -= 1
            numero2 = numero
        else:
            lista2.append(elemento)
    return lista2

#print(repetir(2, "a", ["b","c","d","a","e","f"]))
#print(repetir(4, 4, [1, 2, 3, 4, 5, 6]))


def sumaNumeros(lista):
    resultado = 0
    if(lista == []):
        return []
    for numero in lista:
        if(type(numero) == int):
            resultado = numero + resultado
    
    return resultado

#print(sumaNumeros([1,"a",2,"b",3,"c"]))

_____________________________________________________________
def operacionesEnSublistas(pLista1, pLista2):
    nuevaLista = []
    nuevaSubLista = []
    if pLista1 == []  or pLista2 == []:
        return []
    while pLista1 != []:
        subLista1 = pLista1[0]
        numero1 = subLista1[0]
        subLista1 = subLista1[1:]
        operacion = subLista1[0]
        subLista1 = subLista1[1:]
        numero2 = subLista1[0]
        subLista1 = subLista1[1:]
        pLista1 = pLista1[1:]
        if operacion == "+":
            resultado = numero1 + numero2
        elif operacion == "-":
            resultado = numero1 - numero2
        elif operacion == "*":
            resultado = numero1 * numero2
        elif operacion == "/":
            resultado = numero1 / numero2
        else:
            print("Las operaciones válidas son ‘+’, ‘-’, ‘*’, ‘/’")
        for elemento in pLista2:
            if elemento < resultado:
                nuevaSubLista.append(resultado)
            elif elemento == resultado:
                nuevaSubLista.append(0)
            else:
                nuevaSubLista.append(elemento)
        nuevaLista.append(nuevaSubLista)
        nuevaSubLista = []
    return nuevaLista   
print(operacionesEnSublistas([[2,"+",3],[4,"/",2],[4,"*",3]], [2,14]))
________________________________________________________________________________-
