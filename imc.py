print('Hola, te voy a ayudar a calcular tu indice de masa corporal, para eso te voy a pedir la siguiente información')
def informacion(mensaje, mensaje_while):
    dato = input(mensaje).strip()
    while dato == '': 
        dato = input (mensaje_while).strip()
    return dato    

nombre = informacion('Introduce tu nombre(s): ', 'Informacion erronea, intentalo de nuevo: ')
apellido = informacion('Introduce tu apellido paterno: ', 'Informacion erronea, intentalo de nuevo: ')
apellido_2 = informacion('Introduce tu apellido materno: ', 'Informacion erronea, intentalo de nuevo: ')
edad = int(informacion('Introduce tu edad: ', 'Informacion erronea, intentalo de nuevo: '))
altura = float(informacion('Introduce tu altura en metros, (ej.- 1.75): ', 'Informacion erronea, intentalo de nuevo: '))
peso = float(informacion('Introduce tu peso en kilogramos (ej.- 65.4): ', 'Informacion erronea, intentalo de nuevo: ' ))
print(type(altura))
print(type(edad))
print(type(peso))
imc = peso / altura**2

print('A continuacion te voy dar tu indice de masa corporal segun los datos que me proporcionaste:')
print('Tu nombre es',nombre.capitalize(),  apellido.capitalize(),  apellido_2.capitalize())
print('Tienes ', edad, 'años, pesas ', peso, 'kg y mides ', altura, 'metros')
print('Tu indice de masa corporal es ', imc) 
if imc < 18.5:
   print('Peso inferior al normal')
elif imc >= 18.5 and imc <=24.5:
   print('Peso normal')
elif imc >= 24.5 and imc <= 29.9:
    print ('Peso superior al normal')
if imc >=30:
   print ('obesidad')

      