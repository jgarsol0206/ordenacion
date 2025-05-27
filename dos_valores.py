#Archivo: tres_valores.py
#Fecha: 08/04/2025
#Proy.: estudio de algorismos

#Ordenar crecientemente una lista de tres valores.
#Existe un error, ya que segun los valores, puede cambiar
#dos que entre ellos habia que cambiar, pero genera mal orden
# en los posteriores.

n = []


#Bucle para tomar datos del teclado y guardarlos en la variable n de tipo lista
for i in range(6):

    n.append(int(input())) #append es un metodo de las listas


s = n # Voy a hacer dos intentos de ordenar. Para tener
      # la lista oroginal sin cambios, tendre que copiarla a otra lista
      # y asi trabajamos con la copia
for i in range(5):  #Aqui se refleja el error p.ej. com [7, 5, 3]
    if s[i] > s[i+1]:
        a = s[i]
        s[i] = s[i+1]
        s[i+1] = a 
print(s)

s = n
for i in range(len(n)-2):  #Aqui hacemos el repaso a la lista dos veces
    for j in range(len(n)-1):
        if s[j] > s[j+1]:
            a = s[j]
            s[j] = s[j+1]
            s[j+1] = a
print(s)

s = n
for j in range(len(n)-2):
    for i in range(len(n)-1):
        if s[j] > sj+[1+j]:
            swap(j)
print(s)

