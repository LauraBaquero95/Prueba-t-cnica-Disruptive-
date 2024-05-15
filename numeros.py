"""
Ejercicio: Ordenamiento de Números Pares e Impares
Descripción del problema:
Dado un conjunto de números enteros, desarrolla un algoritmo que ordene estos números de tal
manera que primero se muestren todos los números pares en orden ascendente y luego todos los
números impares en orden ascendente.
Ejemplo:
Entrada: [5, 2, 7, 9, 10, 4, 3]
Salida: [2, 4, 10, 3, 5, 7, 9]
Requerimientos:
1. Desarrolla un algoritmo eficiente para resolver este problema.
2. Considera la implementación de una función o método que reciba como parámetro la lista
de números enteros y devuelva la lista ordenada según lo especificado en el problema.
3. Asegúrate de manejar correctamente casos de entrada vacía o listas que contengan solo
números pares o impares.
"""
resp="s"
while resp!="n":
    def crear_lista_numeros():
        """Función que crea una lista de números a partir de la entrada del usuario."""
        lista_numeros = []  # Lista para almacenar los números ingresados

        # Bucle `for` para leer cada número separado por coma
        n = input("Ingrese los números que quieras separados por comas-> ")
        ingreso = n.split(",")
        for numero_str in ingreso:  # Recorre cada cadena de número individual
            try:
                # Convierte cada cadena de número a un entero
                numero = int(numero_str)
                # Agrega el número entero a la listas
                lista_numeros.append(numero)
            except ValueError: # verifica que no se envien espacios o caracteres incorrectos
                print(f"Error: '{numero_str}' no es un número válido.")

        return lista_numeros
    lista_creada = crear_lista_numeros() #llamamos la funcion 

    def organizar_par_impar(lista_creada): 
        """Función que crea dos listas con numeros pares e impares."""
        #inicializando las listas 
        par=[] 
        impar=[]
        #for que recorre la lista verificando numero x numero si es par o impar 
        for i in lista_creada:
            if i%2==0:
                par.append(i) # agregando a la lista numeros par
            else:
                impar.append(i)# agregando a la lista numeros impar
        par.sort() #organizamos de forma ascendente los datos alamacenados en la lista 
        impar.sort()  #organizamos de forma ascendente los datos alamacenados en la lista 
        return par,impar

    pares,impares=organizar_par_impar(lista_creada) #Llamamos la funcion 


    print(f" Esta es la lista de numeros que creaste \n{lista_creada}")  # mostramos la lista que ingreso el usuario 
    
    lista_nueva=pares+impares #concatenamos las listas para unirlas 
    # verificamos si los numeros ingresados son solo pares o impares. 
    if len(impares)==0:
        print(f"Todos los numeros que ingresaste fueron pares Aqui esta la lista de forma ascendente  \n{lista_nueva} ")
    elif len(pares)==0:
        print(f"Todos los numeros que ingresaste fueron impares Aqui esta la lista de forma ascendente \n{lista_nueva}")
    elif  len(pares) >= 1 and len(impares) >= 1: # verificamos si las listas impares y pares tienen datos 
        print(f" Esta es la lista con los numeros pares e impares organizados de forma ascendete \n{lista_nueva}")

    resp=input("Quieres probar con otros numeros S/N ? ")
    resp.lower()
