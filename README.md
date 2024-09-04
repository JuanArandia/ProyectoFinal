# Proyecto de Parqués

## Descripción
Este proyecto es una implementación en Python del juego de parqués. El juego permite a los jugadores mover fichas en un tablero y compete para ser el primero en llevar todas sus fichas a la meta.

## Estructura del Código

### Paquetes Importados
- `random`: Para generar números aleatorios que simulan el lanzamiento de dados.
- `matplotlib.pyplot`: Para visualizar el tablero del juego mediante gráficos.

### Clases
- **Ficha**: Representa una ficha del juego. Controla el color, la posición y el estado de la ficha (si está en juego o no).
  - `__init__(color)`: Inicializa una ficha con un color específico.
  - `mover(cantidad, tablero)`: Mueve la ficha según el resultado de los dados.

- **Jugador**: Representa un jugador en el juego. Maneja las fichas del jugador y sus movimientos.
  - `__init__(color)`: Inicializa un jugador con fichas de un color.
  - `sacar_ficha(dado1, dado2, tablero)`: Saca una ficha de la cárcel si el resultado de los dados permite hacerlo.
  - `escoger_movimiento(dado1, dado2, tablero)`: Elige y mueve una ficha en base al resultado de los dados.

- **Tablero**: Representa el tablero del juego. Maneja las casillas, las posiciones seguras y las fichas de todos los jugadores.
  - `__init__()`: Inicializa el tablero con casillas y posiciones.
  - `inicializar_fichas(jugadores)`: Crea y asigna fichas a los jugadores.

## Instalación

Para ejecutar este proyecto, asegúrate de tener Python 3.x instalado en tu sistema, también necesitarás instalar el paquete `matplotlib` para la visualización del tablero. Puedes hacerlo utilizando `pip`, el gestor de paquetes de Python.

1. **Instalar Python 3.x**: Descárgalo e instálalo desde [python.org](https://www.python.org/).

2. **Instalar Dependencias**: Abre una terminal o línea de comandos y ejecuta el siguiente comando para instalar `matplotlib`:
   ```bash
   pip install matplotlib

## Ejecución

Una vez que hayas instalado las dependencias, puedes ejecutar el juego siguiendo estos pasos:

1. Descargar el Código: Asegúrate de tener el archivo Python del proyecto (main.py).
2. Ejecutar el Script: En la terminal o línea de comandos, navega hasta el directorio donde se encuentra el archivo del proyecto y ejecuta:
```bash
python parques.py

