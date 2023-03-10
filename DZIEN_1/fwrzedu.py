#użyj funkcji wyższego rzędu filter do wyfiltrwania
# dowolnej kolekcji po warunku parzystości (tylko liczby parzyste)

n1 = [563,56,1,2,4,88,9,112,0,-99,24,5,6,7,18,90,2]
n2 = (6,8,9,-1,0,8,4,12,3,56,7,9,1,2)
n3 = {3,5,6,8,9,12,13,24,13,12,8}

n1parz = list(filter(lambda x:x%2==0,n1))
print(n1parz)

n2parz = list(filter(lambda x:x%2==0,n2))
print(n2parz)

n3parz = list(filter(lambda x:x%2==0,n3))
print(n3parz)

#za pomocą funckji map zamapuj trzy kolekcje n1,n2,n3 na nowe listy podnosząc każdą wartość do potęgi 5

cubelist = list(map(lambda x:x**5,n1))
print(cubelist)

cubekrotka = list(map(lambda x:x**5,n2))
print(cubekrotka)

cubezbior = list(map(lambda x:x**5,n3))
print(cubezbior)


#własna fukcja filtrująca

def filtrowanie(dane,test):
    plus = []
    for element in dane:
        if(test(element)):
            plus.append(element)
    return plus

def ekstra_liczba(n):
    return n>=100
print(filtrowanie(n1,ekstra_liczba))

#własna fukcja mapująca
def mapowanie(dane,transformacja):
    mapa = []
    for element in dane:
        mapa.append(transformacja(element))
    return mapa

def addFive(n):
    return n+5

print(mapowanie(n1,addFive))
