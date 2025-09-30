"""diagrama de flujo del juego"""
import random
from enum import Enum, auto
from random import Random

# Inicia app
# Game manage

class Mano(Enum):
    PIEDRA  = auto()
    PAPEL = auto()
    TIJERAS = auto()
    EMPATE = auto()

class Ganador(Enum):
    JUGADOR = auto()
    ORDENADOR = auto()


# lista_jugadas[0], [1] tijeras, [2] papel
LISTA_JUGADAS = [((Mano.PIEDRA, Mano.TIJERAS),  Mano.PIEDRA),  # piedra gana
                 ((Mano.PIEDRA, Mano.PAPEL),    Mano.PAPEL),  # piedra pierde
                 ((Mano.PIEDRA, Mano.PIEDRA),   Mano.EMPATE), # empate
                 ((Mano.TIJERAS, Mano.TIJERAS), Mano.EMPATE),  # empate
                 ((Mano.TIJERAS, Mano.PAPEL),   Mano.TIJERAS ),  # tijeras gana
                 ((Mano.TIJERAS, Mano.PIEDRA),  Mano.PIEDRA), # tijeras pierde
                 ((Mano.PAPEL, Mano.TIJERAS),   Mano.TIJERAS),  # papel pierde
                 ((Mano.PAPEL, Mano.PAPEL),     Mano.EMPATE),  # empate
                 ((Mano.PAPEL, Mano.PIEDRA),    Mano.TIJERAS)  # tijeras gana
                 ]


def ordenador_escoge() -> Mano | None:
    """la clase random decide el Enum a devolver"""
    azar = Random().randint(0, 2)
    if azar == 0:
        return Mano.PIEDRA
    elif azar == 1:
        return Mano.PAPEL
    elif azar == 2:
        return Mano.TIJERAS

    return None

def jugador_escoje(indice: str) ->Mano | None:
    """segun el indice devuelve el enum correspondiente"""
    if indice == '0':
        return Mano.PIEDRA
    elif indice == '1':
        return Mano.PAPEL
    elif indice == '2':
        return Mano.TIJERAS

    return None

def mano_a_mano(mano_jug: Mano, mano_ord: Mano, lista_j: list)-> Mano  | None:
    """comprueba la mano ganadora en la lista de jugadas y devuelve el Enum
    correspondiente"""
    jugada = (mano_jug, mano_ord)

    for manos, ganadora in lista_j:
        if jugada == manos:
            return ganadora

    return None


def input_jugador():
    indice = ''
    print("[0]: PIEDRA, [1]: PAPEL, [2]: TIJERAS")
    while not indice.isdigit() or not indice == '0' and not indice =='1' and not indice == '2':
        indice = input("Introduce una de las opciones: ")

    return indice

def game():
    contador_jugador = 0
    contador_ordenador = 0
    # flag de control bucle principal
    game_over = False


    # mensaje, al mejor de tres
    print("*" * 30)
    print("*" * 30)
    print("""\tPIEDRAS PAPEL O TIJERAS""")
    print("*" * 30)
    print("*" * 30)
    print("Vamos a jugar al mejor de tres")

    while not game_over and contador_jugador < 3 and contador_ordenador < 3:
        #inptu de usuario
        indice = input_jugador()
        mano_jug = jugador_escoje(indice)
        # juego elije un random
        mano_ord = ordenador_escoge()
        # mensaje jugador: seleccion ; ordenador: seleccion
        print(f"Jugador: {mano_jug} - Ordenador: {mano_ord}")
        # Comprobamos la mano ganadora con la lista de Jugada
        mano_ganadora = mano_a_mano(mano_jug, mano_ord, LISTA_JUGADAS)

        if mano_jug == mano_ord:
            print("Empatamos!")

        else:
            if mano_ganadora == mano_jug:
                contador_jugador += 1
                print("Estupendo, tú ganas!")
            elif mano_ganadora == mano_ord:
                contador_ordenador += 1
                print("Lástima, esta la gano yo.")

        print(f"Score. Juador: {contador_jugador}/3 -  Ordenador: {contador_ordenador}/3")

    print("GAME OVER")
    if contador_jugador == 3:
        print("JUGADOR GANA")
    else:
        print("ORDENADOR GANA")

game()

