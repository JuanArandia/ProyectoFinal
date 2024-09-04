import random
import matplotlib.pyplot as plt

class Ficha:
    def __init__(self, color):
        self.color = color
        self.posicion = None  # comienza en None porque la ficha está en casa
        self.en_juego = False

    def mover(self, cantidad, tablero):
        if self.en_juego and self.posicion is not None:
            nueva_posicion = (self.posicion + cantidad) % len(tablero.casillas_externas)
            self.posicion = nueva_posicion
            print(f"Moviendo ficha {self.color} a la posición {self.posicion}")
        elif cantidad == 5:  # Regla para sacar de casa
            self.en_juego = True
            self.posicion = tablero.posicion_salida[self.color]
            print(f"Ficha {self.color} sale de casa a la posición {self.posicion}")

class Jugador:
    def __init__(self, color):
        self.color = color
        self.fichas = [Ficha(color) for _ in range(4)]
        self.en_carcel = self.fichas.copy()  # toda ficha comienza en la carcel

    def sacar_ficha(self, dado1, dado2, tablero):
        if dado1 == 5 or dado2 == 5 or (dado1 + dado2 == 5):
            if self.en_carcel:
                ficha = self.en_carcel.pop(0)  # sacar la primera ficha de la carcel
                ficha.en_juego = True
                ficha.posicion = tablero.posicion_salida[self.color]
                print(f"Sacando ficha de {self.color} a la posición {ficha.posicion}")

    def escoger_movimiento(self, dado1, dado2, tablero):
        self.sacar_ficha(dado1, dado2, tablero)
        movimientos_posibles = [ficha for ficha in self.fichas if ficha.en_juego]

        if movimientos_posibles:
            ficha_elegida = movimientos_posibles[0]
            ficha_elegida.mover(dado1 + dado2, tablero)

class Tablero:
    def __init__(self):
        self.casillas_externas = [i for i in range(68)]
        self.casillas_internas = {
            "rojo": [f"rojo_{i}" for i in range(8)],
            "azul": [f"azul_{i}" for i in range(8)],
            "verde": [f"verde_{i}" for i in range(8)],
            "amarillo": [f"amarillo_{i}" for i in range(8)]
        }
        self.posiciones_seguras = [5, 12, 17, 22, 27, 34, 39, 44, 51, 56, 61, 66]
        self.posicion_salida = {"rojo": 0, "azul": 17, "verde": 34, "amarillo": 51}
        self.fichas = {"rojo": [], "azul": [], "verde": [], "amarillo": []}

    def inicializar_fichas(self):
        for color in ["rojo", "azul", "verde", "amarillo"]:
            for _ in range(4):
                self.fichas[color].append(Ficha(color))

    def mostrar_tablero(self):
        print("\nEstado actual del tablero:")
        for i in range(len(self.casillas_externas)):
            print(f"Casilla {i+1}: {self.casillas_externas[i]}")
        # mostrar el estado de las fichas
        for color, fichas in self.fichas.items():
            for ficha in fichas:
                print(f"Ficha {color} en posicion {ficha.posicion}")

def lanzar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1, dado2

def iniciar_juego():
    tablero = Tablero()
    tablero.inicializar_fichas()

    jugadores = [Jugador("rojo"), Jugador("azul"), Jugador("verde"), Jugador("amarillo")]
    turno = 0

    while True:
        jugador_actual = jugadores[turno]
        dado1, dado2 = lanzar_dados()
        print(f"\nTurno del jugador {jugador_actual.color}: Dado 1: {dado1}, Dado 2: {dado2}")

        jugador_actual.escoger_movimiento(dado1, dado2, tablero)
        tablero.mostrar_tablero()

        if verificar_ganador(jugadores):
            print(f"¡El jugador {jugador_actual.color} ha ganado el juego!")
            break

        turno = (turno + 1) % len(jugadores)

def verificar_ganador(jugadores):
    for jugador in jugadores:
        if all(ficha.posicion == "llegada" for ficha in jugador.fichas):
            return True
    return False

def graficar_tablero(tablero):
    plt.figure(figsize=(8, 8))
    for i, casilla in enumerate(tablero.casillas_externas):
        plt.text(i, 0, str(i+1), ha='center')
    plt.show()

if __name__ == "__main__":
    iniciar_juego()
