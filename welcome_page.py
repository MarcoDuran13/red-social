#Hola, para empezar con nuestro proyecto de red social, vamos a utilizar
#las herramientas que conocemos para ejecutar algunas acciones.
#
#Primero, mostraremos un mensaje en pantalla dando la bienvenida al usuario
#y escribiendo el nombre de la red.

#A continuaciÃ³n preguntaremos algunos datos al usuario para poder construir su perfil,
#y guardaremos esta informaciÃ³n en variables.

#Finalmente, escribiremos en pantalla todos los datos que hemos recolectado, y permitiremos
#al usuario escribir un mensaje de estado.

#Te invito a examinar el cÃ³digo, leer los comentarios y comprender los tipos de datos
#que estamos utilizando en cada caso.


#Para conocer un poco mÃ¡s del usuario, vamos a preguntarle algunos datos.
#Por ejemplo, su aÃ±o de nacimiento, y aprovecharemos este dato descubrir la edad del usuario.
#Â¿CÃ³mo lo haremos?, usaremos una variable para guardar el resultado del cÃ¡lculo de
#la edad del usuario. Este es un dato de tipo entero.

#A continuaciÃ³n le preguntaremos al usuario su estatura en metros. Este es un dato de tipo float,
#y usaremos esta informaciÃ³n para calcular los centimetros

#Finalmente escribiremos en pantalla los datos que hemos recordado del usuario usando print y le solicitaremos
#que escriba un mensaje para desplegar en pantalla.

############################################################
# Lo primero que haremos serÃ¡ escribir un mensaje de bienvenida al usuario
# con el nombre de la red. Puedes modificar este mensajes para que represente el nombre de tu propia red
# Considera que al escribir """ tambiÃ©n estamos delimitado un string, pero al hacerlo de esta manera,
# cambios de lÃ­nea que ocurran en el cÃ³digo se considerarÃ¡n como parte del string.
# Si no estÃ¡s convencido, prueba el funcionamiento reemplazando los delimitadores por "

print("Bienvenido a ... ")
print("""                                                        .___
  _____ _____ _______   ____  ____   _______   ____   __| _/
 /     \\\__  \\\_  __ \_/ ___\/  _ \  \_  __ \_/ __ \ / __ | 
|  Y Y  \/ __ \|  | \/\  \__(  <_> )  |  | \/\  ___// /_/ | 
|__|_|  (____  /__|    \___  >____/   |__|    \___  >____ | 
      \/     \/            \/                     \/     \/ 
""")

#Primera interacciÃ³n. Solicitamos al usuario que ingrese su nombre,
#y lo guardamos en una variable de tipo str
nombre = input("Para empezar, dime como te llamas. ")
print()
print("Hola ", nombre, ", bienvenido a Marco Red")
print()

#Segunda interacciÃ³n. Solicitamos el ingreso del aÃ±o, y utilizamos este
#dato para estimar la edad de la persona. Â¿Por quÃ© decimos que solo estamos "estimando" su edad?
#Â¿QuÃ© ocurre si eliminamos la conversiÃ³n a tipo de dato 'int' de la siguiente lÃ­nea?
agno = int(input("Para preparar tu perfil, dime en quÃ© aÃ±o naciste. "))
edad = 2020-agno-1
print()

#Tercera interacciÃ³n. Solicitamos la estatura, medida en metros.
#Utilizamos la conversiÃ³n a 'int', y una expresiÃ³n para convertir esto
#a una medida en metros y centÃ­metros
estatura = float(input("CuÃ©ntame mÃ¡s de ti, para agregarlo a tu perfil. Â¿CuÃ¡nto mides? DÃ­melo en metros. "))
estatura_m = int(estatura)
estatura_cm = int( (estatura - estatura_m)*100 )

#Cuarta interacciÃ³n. Consultamos cuÃ¡ntos amigos tiene el usuario.
num_amigos = int(input("Muy bien. Finalmente, cuÃ©ntame cuantos amigos tienes. "))

#Quinta InteracciÃ³n. Se pedira direccion del usuario.
print("Es necesario tener tu direcciÃ¡n de domicilio para darte recomendaciones cercanas a tu casa. ")
direccion = input("Ingresa direcciÃ¡n.")
ciudad = input("Ingresa en quÃ© ciudad vives. ")
departamento = input("Ingresa el departamento. ")

#Sexta InteracciÃ³n. Se pedira el sexo de la persona.
telefono=input("Para terminar, indÃ­canos tu numero telefÃ¡nico. ")

#Con los datos recolectados escribimos en pantalla un texto que resuma los datos que hemos obtenido
print()
print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
print("--------------------------------------------------")
print("Nombre:  ", nombre)
print("Edad:    ", edad, "aÃ±os")
print("Estatura:", estatura_m, "metros y", estatura_cm, "centÃ­metros")
print("Amigos:  ", num_amigos)
print("DirecciÃ¡n:  ", direccion, ",", ciudad, ",", departamento + ".")
print("TelÃ©fono:  ", telefono)
print("--------------------------------------------------")
print("Gracias por la informaciÃ³n. Esperamos que disfrutes con Marco Red")
print()

#Usaremos una variable bool para indicar si el usuario desea continuar
#utilizando el programa o no
continuar = True

#Este ciclo se mantiene en ejecuciÃ³n hasta que el usuario desee salir
while continuar:

    #Solicitamos opciÃ³n al usuario
    print("Ahora puedes interactuar en Marco Red")
    print("Te ofrecemos las siguientes opciones:")
    print("1. Â¿Deseas escribir un mensaje?")
    print("2. Â¿Deseas cambiar tu nombre?")
    print("3. Salir")
    operacion = str(input("Â¿QuÃ© deseas hacer? (Marca el nÃºmero de la opciÃ³n)"))

    #Vamos a aceptar que el usuario ingrese un mensaje cuando escriban "S", "s", o nada
    if operacion == "1" or operacion == "":
        mensaje = input("Vamos a publicar un mensaje. Â¿QuÃ© piensas hoy? ")
        print()
        print("--------------------------------------------------")
        print(nombre, "dice:", mensaje)
        print("--------------------------------------------------")
    #En caso que sea otra respuesta, vamos a decidir salir.
    #AsÃ­, en la siguiente iteraciÃ³n el ciclo terminarÃ¡
    if operacion == "2":
        nombre = input("Digita tu nuevo nombre ")
        print()
        print("--------------------------------------------------")
        print("Tu nuevo nombre es: ", nombre)
        print("--------------------------------------------------")
    if operacion == "3":
        continuar = False

#Mensaje de salida, una vez que el ciclo ha terminado.
print("Gracias por usar Marco Red. Â¡Hasta pronto!")

#Ahora puedes escribir mensajes todas las veces que quieras.
#Observa que hemos utilizado un ciclo while que permite repetir la acciÃ³n de preguntar por un mensajes
#hasta que el usuario escribe algo distino de "S".

#Pero las redes sociales pueden ejecutar mÃ¡s acciones que solamente enviar mensajes.

#Te proponemos los siguientes desafÃ­os:
#1. Este programa termina cada vez que el valor de 'escribir_mensaje' es distinto a "S" o a "s".
#   Modifique el programa para que el programa termine UNICAMENTE cuando se ingresa "N" o "n".
#   En caso que se ingrese algo distinto, debe volver a solicitar una opciÃ³n al usuario.
#
#2. Modifica este menÃº para que le permita el usuario realizar mÃ¡s de una acciÃ³n.
#   Por ejemplo, puedes agregar una acciÃ³n que permita al usuario modificar su nombre.