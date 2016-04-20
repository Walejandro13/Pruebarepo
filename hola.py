#Probando

t1=(1,"dos",3)
t2= (t1,3.25)

list=[4,5,6,7]
print(list.reverse())
print(list)
list.sort()
print(list)
list.pop(2)
print(list)

### matriz
lista=[[4,5,6],[4,9,0],[3,4,5]]
print((lista[2][2]))
lista[2].insert((2),2)
print(lista)
lista[1][2]=7
print(lista)

for i,v in enumerate(lista):
    print(i,v)
listica=["alejo","velez"]

###################Diccionarios

dir={"velez":1234, listica[0]:"hola"}
print(dir)
print(dir.keys())
print(dir["velez"])
dir["velez"]="cambio"
print(dir.items())
del dir["velez"]
print(dir.items())



