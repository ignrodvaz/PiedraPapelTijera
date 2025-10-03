import random

def ordenador_decide_jugada():
    ''' 
    Elige aleatoriamente entre piedra, papel o tijeras y devuelve la elección.     
    '''
    opciones = ["piedra", "papel", "tijeras"]
    res = random.choice(opciones)
    return res

def usuario_decide_jugada():
    ''' 
    Pide al usuario que elija entre piedra, papel o tijeras y devuelve la elección.     
    '''
    eleccion_usuario = input("Elige piedra, papel o tijeras: ")
    while eleccion_usuario not in ["piedra", "papel", "tijeras"]:
        eleccion_usuario = input("Opción no válida, por favor elige piedra, papel o tijeras: ")
    return eleccion_usuario

def determina_ganador(jugada_usuario, jugada_ordenador):
    if jugada_usuario == jugada_ordenador:
        return "Empate"
    elif jugada_usuario == "piedra" and jugada_ordenador == "tijeras":
        return "Ganaste"
    elif jugada_usuario == "tijeras" and jugada_ordenador == "papel":
        return "Ganaste"
    elif  jugada_usuario == "papel" and jugada_ordenador == "piedra":
        return "Ganaste"
    else:
        return "Perdiste"
    
def jugar_torneo():
    puntos_usuario = 0
    puntos_ordenador = 0
    while puntos_usuario < 3 and puntos_ordenador < 3:
        res_ordenador = ordenador_decide_jugada()
        res_usuario = usuario_decide_jugada()
        ganador_ronda = determina_ganador(res_usuario, res_ordenador)
        if ganador_ronda == "Ganaste":
            print("Punto para el usuario")
            puntos_usuario +=1
        elif ganador_ronda == "Perdiste":
            print("Punto para el ordenador")
            puntos_ordenador +=1
        else:
            print("Empate")
        print("Puntos ordenador: ", puntos_ordenador)
        print("Puntos usuario: ", puntos_usuario)
        
    if puntos_usuario == 3:
        print("Ganó el usuario")
    else:
        print("Ganó el ordenador")
    
def jugar():
    print("Bienvenido al piedra papel tijeras.")
    res_ordenador = ordenador_decide_jugada()
    res_usuario = usuario_decide_jugada()
    print(f"El ordendor eligió: {res_ordenador}")
    resultado = determina_ganador(res_usuario, res_ordenador)
    print(resultado)
    
if __name__ == "__main__":
    jugar_torneo()