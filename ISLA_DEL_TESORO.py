#Isla del tesoro
print("Bienvenido a la isla del tesoro")


print ("en que dirección quisieras ir ¿Izquierda o derecha?" )

respuesta= input()

if respuesta == 'derecha':
    print("Caiste en un agujero, un esqueleto escucha el ruido y decide acercarse, decices esperar o salir")
    respuesta_2= input()
    if respuesta_2 == 'salir':
        print("al intentar salir jalas del pie al esqueleto y apoyandote en el sales del agujero")
        print("en que dirección quieres seguir, ¿izquierda o frente?")
        respuesta_3=input()
        if respuesta_3 == 'izquierda': 
            print("llegas a un lago, ¿decides nadar o esperar?")
            respuesta_4=input()
            if respuesta_4 == 'esperar':
                print("del suelo, aparecen dos puertas una roja y otra azul, ¿cual escoges?")
                respuesta_5=input()
                if respuesta_5 == 'roja':
                    print("has ganado, felicidades!! :D")
                else :
                    print("Eres deborado por bestias marinas Game over D:")
            
            else: 
                print("eres deborado por bestias marinas, game over D:")

        else: 
            print("entras a una cueva en el fondo hay un pasadizo, decides explorar o seguir directo al pasadizo")
            respuesta_6=input()
            if respuesta_6 == 'explorar':
                print("encuentras muchos objetos que te permiten derrotar los mounstros y ganas el juego, felicidades!! :D")

            else:
                print("eres atacado por un esqueleto y mueres, game over D:")



    else: 
        print("llevas mucho tiempo en el agujero, la tierra se suelta y te hundes, game over")

else :
    print("llegas a un lago, ¿decides nadar o esperar?")
    respuesta_7=input()
    if respuesta_7 == 'esperar':
        print("del suelo, aparecen dos puertas una roja y otra azul, ¿cual escoges?")
        respuesta_8=input()
        if respuesta_8 == 'roja':
            print("has ganado, felicidades!! :D")
        
    else: 
        print("Eres deborado por bestias marinas Game over D:")


    





    

