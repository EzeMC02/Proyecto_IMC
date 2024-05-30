Calculadora de IMC 

Para realizar el proyecto primero se definió una función la cual nos iba a ayudar con la obtención de datos por parte del usuario y al mismo tiempo verificar que estos datos no quedaran en blanco. 

Siendo la función: 

def informacion(mensaje, mensaje_while): 

    dato = input(mensaje).strip() 

    while dato == '':  

        dato = input (mensaje_while).strip() 

    return dato  

Una vez definida la función se procede a obtener los datos por parte del usuario preguntando por nombre, apellidos, edad, estatura y peso. 

En el caso donde necesitamos obtener valores numéricos se hace un ajuste indicando el tipo de variable que requerimos (int o float) por ejemplo:  

edad = int(informacion. 

Con los datos ya ingresados por parte del usuario definimos nuestra formula:     

imc = peso / altura**2 

En este punto empezamos a mostrar al usuario un resumen de la información obtenida y el resultado del IMC, para mostrar el nombre completo del usuario se concatenan tres de las variables introducidas por el mismo, al tratar de un nombre propio también indicamos que la primera letra de cada una de estos sea mayúscula mediante .capitalize: 

print('Tu nombre es',nombre.capitalize(),  apellido.capitalize(),  apellido_2.capitalize()) 

A continuación, se muestra el resto de la información concatenada para que se muestre en una sola línea: 

print('Tienes ', edad, 'años, pesas ', peso, 'kg y mides ', altura, 'metros') 

Se muestra el IMC obtenido y abajo un significado de este para lo cual es necesario hacer un tabulador según sea el resultado la leyenda que se mostrara: 

if imc < 18.5: 

   print('Peso inferior al normal') 

elif imc >= 18.5 and imc <=24.5: 

   print('Peso normal') 

elif imc >= 24.5 and imc <= 29.9: 

    print ('Peso superior al normal') 

if imc >=30: 

   print ('obesidad'). 

  

  

Reflexiones: 

Al ser un programa muy versátil, Python está actualmente entre los programas más usado a nivel mundial para la programación. 

El hacer uso de esta herramienta tal versátil te puede servir para las tareas más pequeñas como para proyectos gigantes 

El mundo de la programación está en su auge y el meternos en él es difícil pero definitivamente valdrá la pena cada segundo invertido y cada avance que tengamos en este es un logro pequeño que a largo o mediano plazo nos dará una recompensa ya sea económica, laboral y/o satisfacción personal. 

Esto es solo el principio de las cosas que podemos llegar a hacer y he quedado emocionado y con ganas de aprender más. 
