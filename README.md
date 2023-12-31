<div align="center">
  <h1>Video Games Dataset Analysis</h1>
</div>
<div align="center">
  <img src="images/controles.png" width="600" alt="Controles">
</div>

## Descripción General
Este repositorio contiene un dataset y scripts para producirlo. A su vez, analiza información sobre videojuegos, utilizando datos de la API de RAWG. El análisis se centra en identificar tendencias y patrones en la popularidad de diferentes géneros de videojuegos a lo largo del tiempo.

## Estructura del Dataset
El dataset incluye los siguientes atributos:

- `genre` (STRING): Categoría o tipo del videojuego (ej. Acción, RPG, Aventura, etc.).
- `year` (NUMERIC): Año en que el juego fue lanzado.
- `average_rating` (NUMERIC): Calificación media otorgada a los juegos de un género específico en un año determinado.
- `game_count` (NUMERIC): Número total de juegos lanzados en un género particular durante un año específico.
- `genre_successful` (NUMERIC): Indicador binario (1 o 0) que muestra si un género es considerado exitoso en un año basado en el umbral de calificación promedio.

## Proceso de Análisis
El proceso de análisis consta de los siguientes pasos:

1. **Extracción de Datos:** Utilizando la API de RAWG, se recopilan diferentes datos de videojuegos como el nombre, género, fecha de lanzamiento y calificaciones.
2. **Procesamiento de Datos:** Los datos se procesan para calcular el rating promedio y la cantidad de juegos lanzados por género y año. También se determina si un género es exitoso en un año específico basándose en un umbral de calificación promedio, con esto se etiqueta o clasifica la instancia.
3. **Almacenamiento de Datos:** Los datos procesados se almacenan en un archivo en formato ARFF, con objeto de poder ser analizado fácilmente.

## Uso del Dataset
Puede ser utilizado para realizar análisis en aplicaciones machine learning; puede servir para explorar tendencias en la industria de los videojuegos y entender cómo han ido evolucionado los géneros y la recepción de los juegos durante su historia.

## Requisitos
- Python 3
- Bibliotecas de Python: `pandas`, `requests`

## Cómo Ejecutar
1. Clonar el repositorio.
2. Ejecutar el script `GameDataAnalyzer` para recopilar y procesar los datos.
3. Listo, en el nuevo directorio data/arff se dispondrá del dataset actualizado y listo para ser analizado.

## Autores
Aingeru García
