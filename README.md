# Optimización del Problema del Viajante de Comercio (TSP) con PuLP

Este repositorio contiene la implementación y resolución del **Problema del Viajante** (*Travelling Salesperson Problem - TSP*) utilizando **Programación Entera Mixta (MILP)** en Python.

---

## Descripción del Problema
El TSP es un problema clásico de optimización cuyo objetivo es encontrar la ruta mas corta posible para recorrer un conjunto de ciudades determinado. Se incluyen las premisas de que se pase por cada ciudad exactamente una vez y al terminar se regrese al origen. Se trata de un programa muy útil para minimizar costes de transporte en empresas de logística.

## Formulación del Modelo (MILP)
El modelo matemático se ha formulado utilizando:
* **Variables de decisión binarias ($x_{i,j}$):** Indican si la ruta pasa directamente de la ciudad $i$ a la ciudad $j$.
* **Función Objetivo:** Minimizar la distancia total del recorrido.
* **Restricciones de Grado:** Cada ciudad debe tener exactamente un arco de entrada y uno de salida.
* **Eliminación de Sub-tours:** Implementación de las restricciones de **Miller-Tucker-Zemlin (MTZ)** para garantizar una única ruta conectada.

---

## Tecnologías Utilizadas
* **Lenguaje:** Python
* **Modelado de Optimización:** `PuLP`(configurado con el *solver* por defecto CBC, aunque compatible con *solvers* comerciales como **Gurobi** o CPLEX si se dispone de licencia).

---

## Archivos en el Repositorio
* `TPS_Solver.py`: Script principal de Python con el modelo de optimización y la resolución con PuLP.
* `problemaviajante.ipynb`: Cuaderno Jupyter con el código diseccionado.

---

## Cómo Ejecutar el Proyecto
1. Clonar este repositorio o descargar los archivos.
2. Instalar la librería necesaria:
   ```bash
   pip install pulp
3. Ejecutar el programa:
    ```bash
   python TPS_Solver.py
   
---

## 🔮 Próximos Pasos
*  **Visualización gráfica:** Implementar `Matplotlib` para trazar la ruta óptima sobre un plano.
*  **Escalabilidad:** Probar el modelo con un mayor número de ciudades.
