import random


def adivina_el_numero_de_la_computadora(x):
    print("******************************************************************")
    print('========================Bienvenido================================')
    print("******************************************************************")
    print(f"Selecciona un numero entre 1 y {x} para que la computadora intente adivinarlo")

    limite_inferior = 1
    limite_superior = x

    respuesta = ""
    while respuesta != "A":
        #Generar prediccion
        if limite_inferior != limite_superior:
            prediccion = random.randint(limite_inferior, limite_superior)
        else:
            prediccion = limite_inferior #Tambien podria ser el limite_superior
        
        # Obtener respuesta del usuario
        respuesta = input(f"Mi prediccion es {prediccion}.Si es muy alta, ingresa (A). Si es muy baja, ingresa (B). Si es correcta, ingresa (C): ").lower()

        if respuesta == "a":
            limite_superior = prediccion -1

        elif respuesta == "b":
            limite_inferior = prediccion +1

    print(f"La computadora adivino su numero correctamente: {prediccion}")
        


adivina_el_numero_de_la_computadora(10)
