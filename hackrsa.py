# HACKRSA _ FUNCION ENCRIPTACION/DESENCRIPTACION
# Dilson Lazaro _ Computacion cientifica _ I semestre
# Marzo 18 2016 _ 14:57 hrs

# Se escogen dos numeros primos aleatorios (p y q); si se desea cambiar la llave publica hay que cambiar los numeros p y q por los primos deseados.
# Se recomienda que si quiere cambiar la llave publica, por otra distinta use el programa myrsa.py y genere con esta la nueva llave a usar
# Funcion modulo se emplea para llevar el proceso de los numeros primos a una variable llamada n utilizada mas adelante en la generacion del exponente de  # desencriptacion.
# La funcion de euler, se emplea en funcion algoritmica, es llamada nuevamente mas adelante y adaptada en una variable llamada f que servira para hallar # el exponente privado, para asi, continuar con el debido proceso de descifrado de los datos cifrados, el resultado que este programa muestra que retorna # la funcion en cuestion sale de hacer el despeje total de la ecuacion (p-1)*(q-1); es decir, phi_n == (p-1)*(q-1).

def modulo(p,q):
    return (p*q)
                              # Funciones modulo(multiplicaion de los numeros aleatorios) y funcion de Euler(p-1)*(q-1), respectivamente.
def phi_n(p,q): 
    return (p*q-p-q+1)
  
p = 5                         # Primero numero aleatorio 
q = 11                        # Segundo numero aleatorio
n = modulo(p,q)               # Producto de los numeros aleatorios, su proceso es: primero, se ejecuta la funcion modulo(p,q), luego n es igual al valor                                                     			      # que retorna la funcion.
f = phi_n(p,q)                # Funcion de euler
e = 39                        # Entero positivo coprimo menor que f
      
# Ciclo que comienza con un valor en la variable d de 1 y mientras la condicion que se le pide que halle se cumpla, el resultado sera la vaiable inicial # mas uno. condicion      
                              # Calcular d
d = 1                         # d = e^-1 (mod f)        d * e = 1 (mod f)
while ( d * e % f  != 1):     
    d = d + 1
     
# imprime el valor del modulo y lo muestra por pantalla, igualmente el exponente publico

print "\nN:(",n,")"
print "\ne:(",e,")"

# Mensaje del proceso a ejecutarse, sera impreso en pantalla.

print ("\nDatos a proceso de encriptacion..")

# Datos que seran encriptados, estos los pedira Seran ingresados por el usuario teniendo presente que los numeros van en una lista del (0,9), pues lo    # exige el ejercicio.

m1=(input ("\nDato 1: ")) 
m2=(input ("Dato 2: "))
m3=(input ("Dato 3: "))
m4=(input ("Dato 4: "))

#Mensaje que mostrara que datos van a ser cifrados.

print "\nCifrar", m1, m2, m3, m4

# para cada uno de los datos que se ingresan se realiza el mismo proceso, donde cada dato encriptado sera igual a, el dato elevado a la potencia del      # exponente publico y esto a la operacion modulo del modulo del programa (multiplicaion de los numeros aleatorios)

n1 =  m1 ** e % n
n2 =  m2 ** e % n
n3 =  m3 ** e % n
n4 =  m4 ** e % n

# imprime en fila por pantalla el mensaje encriptado, es decir, los cuatro datos ingresados, mostrando el valor que toman despues de pasar por la        # encriptacion, este mensaje sera el que vera el intruso. 

print "\nMensaje Cifrado", n1, n2, n3, n4

# invirtiendo el proceso de la exponenciacion modular, esta linea del codigo imprime los datos ya desencriptados aplicando el proceso siguiente: (cada   # uno de los datos cifrados elevedos al exponente privado y esto a su vez a la operacion modulo del modulo del programa(multiplicaion de los numeros     # aleatorios))

print "\nDatos descifrados:(",n1 ** d % n, ",",n2 ** d % n,",",n3 ** d % n,",",n4 ** d % n,")"

print "\nEnd"