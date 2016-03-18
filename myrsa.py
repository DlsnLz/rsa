				  ######################################################################################
				  ##      ALGORTITMO RSA _ COMPUTACION CIENTIFICA _ Universidad de Medellin.          ##  
				  ##                                Marzo - 2016                                      ##
				  ##                                   DlsnLz                                         ##
				  ##                                                                                  ##
				  ######################################################################################


#                                               +++++++++++++++++++++++ CODIGO RSA +++++++++++++++++++++++++++

# REALIZADO: Basando todo el proceso en las distintas funciones que se han visto en clase y muchas otras demas cosas con ayudas de la internet y con     # mucho del ingenio logico personal.

# Ayudas textos y Explicaciones: logica para programacion de computadores _ Gabriel Vasquez L _ Biblioteca udem _ cap 4 - pag 62,96 ; Fundamentos de     # programacion (algoritmos y estructura de datos)_ Luis joyanes Aguilar _ Biblioteca udem _ cap 4 y 5; http://es.slideshare.net/jpadillaa/criptografia-  # asimetrica-rsa _ Diapositiva 22; http://serdis.dis.ulpgc.es/~ii-cript/RSA.pdf; http://www.lawebdelprogramador.com/codigo/Python/2413-Determinar-si-un- # numero-es-primo-o-no.html.

# Algoritmo RSA, generador de las claves publicas y privadas dados dos numeros primos, validando en medio de su proceso condiciones que de una u otra    # manera van a ser dependientes consecutivos de cada una de las funciones y los arreglos tratados.

# la funcion myrsa, fue definida en este codigo como algoritmo_rsa; debido a que hubieron algunos problemas de confusion.

# Dados dos numeros, esta funcion se encargara de identificar cual es el menor, necesaria en el algoritmo para que cuando se ejecute el proceso de la    # busqueda del maximo comun divisor los numeros ingresados sean ordenados de tal manera que el mas grande sea mayor que el menor (es obvio pero por       # claridad,se menciona)  

def menornumero (x,y):
	if x < y:
		return x
	else:
		return y

# Funcion que identificara el maximo comun divisor, teniendo presente la funcion anterior, pues, al ser dados los numeros esta los ordenara de manera que # aunque se obvie el mayor sea mas grande que el menor.

def maxcomdiv (x,y):
	m = menornumero(x,y)
	for i in range (m,0,-1):
		if x % i == 0 and y % i == 0:
			return i

# Esta funcion define la segunda condicion que debe cumplir el numero "e", me dice que 1 < e < funcioneuler; y ademas que el numero "e" debe ser coprimo # con el modulo (linea 41,42)

def coprimos (a,b):
	m = maxcomdiv (a,b)
	if m==1:
		return 1
	else:
		return 0

# Funcion que identifica si al ingresar un numero cumple con las condiciones que pide, las cuales dicen literalmente que en una lista de numeros del     # dos al x-1 (pues esta dentro del ciclo for), divida a x entre todos los numeros antes del numero en cuestion y busque los numeros que cumplan que     # x mod i == 1, estos seran primos; de ese modo, si, al ingresar un numero cumple la condicion entonces este sera primo.           

def fprim (t):
	for i in range (2, t): 
		if t % i == 0:
			return 0
	return 1

# Funcion que multiplicara los numeros que seran ingresados por el usuario y nuevamente seran utilizados como resultados al final del codigo donde se    # muestra como; modulo, parte de la llave publica y privada.

def modulo(p,q):
    return (p*q)

# Funcion de Euler, necesaria en el algoritmo para hallar "e" y "d", pues, con "e" necesita que sea coprimo y con "d" es necesario que la multiplicacion # de e por d mod funcioneuler ==1; es decir (en este algoritmo) e * d % phi_n(p,q) == 1, si esto se cumple entonces sera "d". 

def phi_n(p,q): 
    return (p*q-p-q+1)
   
# Se imprime en pantalla el texto, dando instrucciones del tipo de numeros que se requieren y el por que el proceso se demorara un poco, en dado caso.
# Las instruciones aparecen debido a que si se ingresan numeros no primos el proceso se parara y tocara iniciar nuevamente(el programa se para).

print ("\nPara generar sus claves siga las instrucciones que se le piden a continuacion...")

print 				("\n++++++++++++++++++++++++++++++++++INSTRUCCIONES+++++++++++++++++++++++++++++++++++++++")
print ("\n++ Tenga en cuenta que los numeros a ingresar tienen que ser primos, si no, sus llaves no seran generadas.")
print ("\n++ Aqui algunos de ellos: 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89.")
print ("\n++ Si al ingresar dos numeros grandes observa que el proceso se demora, no se altere, solo espere que pronto sus llaves seran generadas.")

# input palabra reservada del diccionario de python la cual pide que se ingrese un dato(numeros en este caso); estos numeros son aleatorios y primos,    # ademas, son estos datos son los que validaran el proceso de la funcion modulo.

p=(input ("\nPrimer numero aleatorio:"))
q=(input ("\nSegundo numero aleatorio:"))



def algoritmo_rsa (p,q):
	
	if fprim(p)==0 or fprim(q)==0:
		return '\nEstas seguro que los numeros aleatorios que acabas de ingresar son correctos'
 
	else:

# Hallar "e" tal que 1< e <phi_n(p,q) y mcd(e, phi_n(p,q)) = 1
# "e" Debe ser un entero positivo coprimo con phi_n(p,q) y menor que este.
# Este ciclo buscara en la lista desde el numero 2 hasta el valor de phi_n(p,q)-1 un numero que sea coprimo con "e", y, este numero sera el valor que   # quedara valiendo "e".

		for e in range(2,phi_n(p,q)):
			if coprimos (phi_n(p,q), e) == 1:
				e

# Este ciclo cumplira la condicion mencionada en el apartado de la funcioneuler que dice que "d" sera igual a la multiplicacion de e por d mod          # phi_n(p,q) ==1,teniendo presente que es un ciclo y su rango esta comprendido en (phi_n(p,q),2) 

		for d in range(phi_n(p,q)*2):
			if e * d % phi_n(p,q) == 1:
				d

# lineas que imprimiran en pantalla respectivamente; modulo, llave publica y llave privada.

		print "\nphi_n es : (",phi_n(p,q),")"

		print "\nEl modulo es:(",modulo(p,q),")"

		print "\nLa llave publica es: (",modulo(p,q),",",e,")"

		print "\nLa llave privada es: (",modulo(p,q),",",d,")"

print algoritmo_rsa(p,q)