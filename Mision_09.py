#Autor: Víctor Manuel Rodríguez Loyola
#Misión 09

def extraerPares (lista): #Recibe una lista y crea una nueva extrayendo los valores pares de la lista original.
    listaPares=[]
    for pares in lista:
        if pares %2==0:
            listaPares.append(pares)
    print(listaPares)


def extraerMayoresPrevio(lista): #Lee una lista y extrae el valor mayor de un valor previo
    listaMayores=[]
    for datos in range(0,len(lista)-1,1):
        if lista[datos]<lista[datos+1]:
            listaMayores.append(lista[datos+1])
    print(listaMayores)


def intercambiarParejas(lista): #Recibe una lista e intercambia de lugar las diferentes parejas de datos que se forman
    listaParejas=[]
    for dato in range(0, len(lista)-1,2):
        listaParejas.append(lista[dato+1])
        listaParejas.append(lista[dato])
    if len(lista)%2 !=0:
        listaParejas.append(lista[len(lista)-1])

    print(listaParejas)


def intercambiarMM(lista): #Recibe una lista e intercambia de lugar el valor mayor y menor de la misma.
    if len(lista)>1:
        mayorPos = lista.index(max(lista))
        menorPos = lista.index(min(lista))
        mayor = max(lista)
        menor = min(lista)
        lista[mayorPos]= menor
        lista[menorPos]=mayor

    print(lista)


def promediarCentro(lista): #Recibe una lista y devuelve el promedio de los valores centrales de la misma.
    if len(lista)>2:
        promedio= (sum(lista)-max(lista)-min(lista))//(len(lista)-2)
        print(promedio)
    else:
        print(0)


def calcularEstadistica(lista): #Calcula los valores de Media y Desviación estándar de una lista
    sumaMedia=0
    sumaDesviacion=0
    if len(lista)>1:
        for indice in range(0,len(lista),1):
            sumaMedia+=lista[indice]
        media= sumaMedia/len(lista)

        for indice in range(0,len(lista),1):
            sumaDesviacion+=(lista[indice]-media)**2
        desviacion=(sumaDesviacion/(len(lista)-1))**0.5
    elif len(lista)==1:
        media =sum(lista)/(len(lista))
        desviacion=0
    else:
        media=0
        desviacion=0
    print("%.1f,%f"%(media,desviacion))


def calcularSuma(lista):  #Recibe una lista y regresa la suma de la misma sin considerar los valores 13 y los que estén alrededor.
    lugar = lista.index(13)
    if len(lista) == 1:
        lista[lugar] = 0
    else:
        if lugar == 0 and len(lista) > 1:
            lista[lugar] = 0
            lista[lugar + 1] = 0
        elif lugar > 0 and lugar < len(lista) - 1:
            lista[lugar] = 0
            lista[lugar + 1] = 0
            lista[lugar - 1] = 0
        elif lugar == len(lista) - 1:
            lista[lugar] = 0
            lista[lugar - 1] = 0

    print(sum(lista))
