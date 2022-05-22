def operacionesEnSublistas(pLista1, pLista2):
        while pLista1 != []:
            numero1 = pLista1[0]
            pLista1 = pLista1[1:]
            operacion = pLista1[0]
            pLista1 = pLista1[1:]
            numero2 = pLista1[0]
            pLista1 = pLista1[1:]
        if operacion == "+":
            resultado = numero1 + numero2
            print (resultado)
operacionesEnSublistas([[51,"+",2],[8,"-", 25]], [2,14])

