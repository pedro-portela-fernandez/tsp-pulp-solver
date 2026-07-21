import pulp
#--------------------------------------------------------------------------
# Datos de entrada (son datos de ejemplo, aquí irían los datos reales de cada caso particular)
#Número de ciudades
N = 5
# Definimos las distancias entre cada par de ciudades (i, j)
distancias = {
    (0, 1): 10, (0, 2): 15, (0, 3): 20, (0, 4): 25,
    (1, 0): 10, (1, 2): 35, (1, 3): 25, (1, 4): 12,
    (2, 0): 15, (2, 1): 35, (2, 3): 30, (2, 4): 20,
    (3, 0): 20, (3, 1): 25, (3, 2): 30, (3, 4): 15,
    (4, 0): 25, (4, 1): 12, (4, 2): 20, (4, 3): 15
}
#--------------------------------------------------------------------------
# Problema del viajante (TPS)
# Definimos el problema de minimización y lo llamamos Optimizacion1
problema = pulp.LpProblem("Optimizacion1", pulp.LpMinimize)
# Creamos la variable de decisión x(i,j)
x = {}
for i in range(N):
    for j in range(N):
        if i != j:
            nombre_var = f"x_{i}_{j}"
            x[i, j] = pulp.LpVariable(nombre_var, cat ="Binary")
# Función objetivo
funcion_objetivo = 0
for i in range(N) :
    for j in range(N) :
        if i != j:
            funcion_objetivo += distancias[i,j] * x[i,j]
# Le asignamos la función objetivo al problema
problema += funcion_objetivo, "Distancia_Total_Recorrida"
#--------------------------------------------------------------------------
# Restricciones de grado
# Restricción 1, salir de cada ciudad exactamente una vez
for i in range(N):
    suma_salidas = 0
    for j in range(N):
        if i != j:
         suma_salidas += x[i,j]
    # Le asignamos la restricción de la ciudad "i" al problema
    problema += (suma_salidas == 1), f"Restriccion_Salida_Ciudad_{i}"
# Restricción 2, entrar en cada ciudad exactamente una vez
for j in range(N):
    suma_entradas = 0
    for i in range(N):
        if i != j:
         suma_entradas += x[i,j]
    # Le asignamos la restricción de la ciudad "i" al problema
    problema += suma_entradas == 1, f"Restriccion_Entrada_Ciudad_{j}"
#--------------------------------------------------------------------------
# Variables auxiliares continuas
u = {}
for i in range(1,N):
    nombre_var_u = f"u_{i}"
    u[i] = pulp.LpVariable(nombre_var_u, lowBound = 1, upBound = N-1, cat = "Continuous")
# Restricción de Subtours
sum2 = N-1
for i in range(1,N):
    for j in range(1,N):
        if i != j:
            # Restricción: u[i] - u[j] + N * x[i,j] <= N - 1
            sum1 = u[i] - u[j] + N * x[i,j]
            # Le asignamos la restricción del trayecto "i -> j" al problema
            problema += sum1 <= sum2, f"Restriccion_Subtours_{i}_{j}"
#--------------------------------------------------------------------------
# Obtener la ruta más eficiente (resolver el problema de minimización)
problema.solve()
#Estado de la solución
print("Estado:", pulp.LpStatus[problema.status])
#Caminos elegidos
print("\nRuta óptima:")
ciudad_actual = 0
ruta = [ciudad_actual]
for _ in range(N):
    for j in range(N):
        if ciudad_actual != j and x[ciudad_actual,j].varValue == 1:
                print(f"De la ciudad {ciudad_actual} a la {j}")
                ciudad_actual = j
                ruta.append(ciudad_actual)
                break
print("\nRuta completa:","->".join(map(str,ruta)))
# Distancia total del viaje (coste)
print(f"\nDistancia total mínima: {pulp.value(problema.objective)}")
