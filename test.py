#######################Ejercicio 1####################################################################
def primeros_pares_1_1(n): #funcion que evalua los primero n pares
	c = 0     #contador para cortar el ciclo
	par = 0		#variable para numeros pares
	while c != n: 	#ciclo que repite el proceso mientras que el contador sea distinto de parametro entregado en la funcion
		print(par)	#muestra valor par
		c += 1		#aumento contador
		par += 2	#aumento variable en 2 para que sea par

def sincero_1_2(n): #funcion que evalua los primero n pares sin el 0
	c = 0 		#contador para cortar el ciclo
	par = 1		#variable para numeros pares inicia en 1 para no mostrar el 0
	while c != n: 	#ciclo que repite el proceso mientras que el contador sea distinto de parametro entregado en la funcion
		if par%2==0:	#evalua que el valor sea par (se inicio con valor impar)
			print(par)	#muestra valor par
			c += 1		#aumento contador
		par += 1	#aumento variable

#ambas funciones anteriores las realicé con ciclos while, debido a que puedo detener el ciclo al alcanzar la cantidad indicada por el usuario.


#######################Ejercicio 2####################################################################
def suma_impares_2_1(n):  #funcion para sumar impares
	sum = 0				#variable que guarda el valor de la suma
	for i in range (0,n+1):	#ciclo desde 0 hasta n para sumar numeros impares
		if (i%2==1):		#condicion. evalua que el valor sea impar (compara el resto de la division)
			sum += i		#a la variable le sumo el valor impar
	print(sum)			#muestra el resultado de la suma

def suma_impares_con_limites_2_2(min,max): #funcion para sumar impares con limites
	sum = 0		#variable que guarda el valor de la suma
	if (min<max):	#evalua que los limites esten en el orden correcto
		for i in range (min, max+1): #ciclo desde min hasta max para sumar numeros impares
			if (i%2==1):	#condicion. evalua que el valor sea impar (compara el resto de la division)
				sum += i	#a la variable le sumo el valor impar
		print(sum)		#muestra el resultado de la suma
	else:			#si no estan en el orden correcto ...
		print("el limite inferior no es menor que el limite superior") 	#imprime alerta

## desarrollé ambas funciones con ciclos for, debido a que, puedo limitar los rangos que se entregan en ellos.


#######################Ejercicio 3####################################################################

def fibonacci_3(n):		#funcion para calcular la secuencia de fibonacci (retorna solo 1 valor)
	if n < 2:			#si n es menor que 2 entonces retorna el mismo valor (los valores inicales de la secuencia son 0,1)
		return n
	else:				#sino, entonces retorna
		return fibonacci_3(n-1) + fibonacci_3(n-2) #valor entregado al llamar a la función de nuevo (recursividad) disminuido en 1, mas (+),
									#valor entregado al llamar a la funcion disminuido en 2.

## La secuencia de fibonacci es un ejemplo claro de recursividad, al hacerlo con una funcion, simplifico de manera drastica la logica para llegar al resultado.
## la funcion retorna solo un valor y se ejecuta cada vez que se requiere, esta entrega el valor de la funcion en el parametro entregado.
## ejemplo: al ingresar el valor 7 la funcion retorna el valor 13 (f7 = f6+ f5 => fn = fn-1 +fn-2)



#### decidi realizar el desarrollo de todas las actividades en forma de funcion, debido a que es mucho mas facil de ejecutar y además de realizar validaciones,
#### como las que realizo mas abajo para llamar a las funciones de cada item

print ("Prueba Desarrollo:")
print ("1. Solo Pares")
print ("2. Suma Impares")
print ("3. Secuencia de Fibonacci")
opcion = int (input("Escoga alguna de las opciones anteriores :"))
############## ejercicio 1 ###################
if (opcion == 1):
	print ("1.1 Parte 1, ingrese 1")
	print ("1.2 Parte 2, ingrese 2")
	op = int (input("Escoga alguna de las opciones anteriores :"))
	############# parte 1#######################
	if(op == 1):
		n = int(input("ingrese parametro: ") )

		if (n>=0):
			primeros_pares_1_1(n)

		else:
			print("El Valor ingresado no es valido")
	################## parte 2 ################
	elif (op == 2):
		n = int(input("ingrese parametro: ") )

		if (n>=0):
			sincero_1_2(n)

		else:
			print("El Valor ingresado no es valido")

	else:
		print("el valor ingresado no es valido")

############## ejercicio 2 ###################
elif (opcion ==2):

	print ("2.1 Parte 1, ingrese 1")
	print ("2.2 Parte 2, ingrese 2")
	op = int (input("Escoga alguna de las opciones anteriores :"))
	############# parte 1#######################
	if(op == 1):
		n = int(input("ingrese parametro: ") )

		if (n>=0):
			suma_impares_2_1(n)

		else:
			print("El Valor ingresado no es valido")
	################## parte 2 ################
	elif (op == 2):
		min = int(input("ingrese limite inferior: ") )
		max = int(input("ingrese limite superior: ") )

		if (min>=0 and max>=0):
			suma_impares_con_limites_2_2(min,max)

		else:
			print("Los valores ingresados no son validos")

	else:
		print("el valor ingresado no es valido")

elif (opcion == 3):

	n = int(input("ingrese parametro: ") )

	if (n>=0):
		for i in range (n+1):
				print (fibonacci_3(i))
	else:
		print("El Valor ingresado no es valido")

else:
	print ("ingrese una opcion valida")







