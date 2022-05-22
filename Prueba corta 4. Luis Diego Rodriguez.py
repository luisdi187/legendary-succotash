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
#Reto 1

def operacionesEnSublistas(pLista1, pLista2):
    nuevaLista = []
    nuevaSubLista = []
    if pLista1 == []  or pLista2 == []:
        return []
    while pLista1 != []:
        subLista1 = pLista1[0]
        numero1 = subLista1[0]
        operacion = subLista1[1]
        numero2 = subLista1[2]
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
            return ("Las operaciones válidas son ‘+’, ‘-’, ‘*’, ‘/’")
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

#print(operacionesEnSublistas([[4, "*", 4],[8, "-", 1]], [5, 9, 16]))
________________________________________________________________________________
#Reto 3

def trioListas(pLista1, pLista2):
    nuevaLista = []
    indice = 0
    ciclo = 0
    if pLista1 == []  or pLista2 == []:
        return []
    while pLista2 != []:
        elemento = pLista2[0]
        if indice != len(pLista1):
            while indice < len(pLista1):
                subLista = pLista1[indice]
                numero = subLista[2]
                if elemento == subLista[0]:
                    while(numero != 0):
                        nuevaLista.append(subLista[1])
                        numero -= 1
                        ciclo += 1
                indice += 1
            if ciclo == 0 : 
                nuevaLista.append(elemento)
        pLista2 = pLista2[1:]
        indice = 0
        ciclo = 0
    return nuevaLista

# print(trioListas([['s',  'z',  2], ['a',  'i',  4]],['e',  's',  'p',  'a', 'ñ',  'a']))
# print(trioListas([['a',  'e',  2], ['m',  'p',  3]],['m',  'a',  'm',  'a']))
# print(trioListas([['t',  't',  1], ['e',  'e',  1]],['k',  'e',  'n',  'n', 'e',  't']))

#///////////////////////////////////////////////////////////////////////////////////////////////////////////#

#Reto 2

def totalDivisores(pNum):
    divisor = pNum
    divisores = 0
    total = 0
    
    while(pNum > 1):
        if(divisor % pNum == 0):
            divisores = pNum
            pNum = pNum - 1
            total += divisores
        else:
            pNum = pNum - 1
    return total

def encontrarNumerosAmigos(pNumero):
    numero = 0 
    pareja = []
    amigos = []
    
    if pNumero < 2:
        return "El numero debe ser mayor a 2"
    for elemento in range(2, pNumero+1):
        numero = elemento + 1
        while(numero != pNumero):
            if(totalDivisores(numero) == elemento):
                if(totalDivisores(elemento) == numero):
                    pareja.append(numero)
                    pareja.append(elemento)
                    amigos.append(pareja)
            numero += 1
    return amigos

print(encontrarNumerosAmigos(1220))
