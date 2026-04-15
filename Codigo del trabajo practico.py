import numpy as np
import matplotlib.pyplot as plt

# Función auxiliar para calcular el error aproximado
def calcular_ea(actual, anterior):
    if actual == 0:
        return 100.0
    return abs((actual - anterior) / actual) * 100.0

print("="*50)
print("TRABAJO PRÁCTICO N°1 - ANÁLISIS NUMÉRICO")
print("="*50)

# ---------------------------------------------------------
# EJERCICIO 1
# ---------------------------------------------------------
print("\n--- Ejercicio 1 ---")
# Función: f(x) = 5x^3 - 5x^2 + 6x - 2
def f1(x):
    return 5*x**3 - 5*x**2 + 6*x - 2

# a) Gráficamente
x_vals1 = np.linspace(-1, 2, 100)
y_vals1 = f1(x_vals1)

plt.figure(figsize=(8, 5))
plt.plot(x_vals1, y_vals1, label="f(x) = 5x^3 - 5x^2 + 6x - 2")
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.grid(True)
plt.title("Ejercicio 1: Método Gráfico")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()

# b) Método de bisección
# Analizando la gráfica/función, f(0) = -2 y f(1) = 4, hay un cambio de signo.
xl1, xu1 = 0.0, 1.0 
es1 = 10.0  # Tolerancia del 10%
ea1 = 100.0
xr1_ant = 0.0
iter1 = 0

print(f"Bisección (Valores iniciales: xl={xl1}, xu={xu1}):")
while ea1 > es1:
    xr1 = (xl1 + xu1) / 2.0
    if iter1 > 0:
        ea1 = calcular_ea(xr1, xr1_ant)
    
    print(f"Iteración {iter1+1}: xr = {xr1:.4f}, Error Aproximado = {ea1:.2f}%")
    
    test = f1(xl1) * f1(xr1)
    if test < 0:
        xu1 = xr1
    elif test > 0:
        xl1 = xr1
    else:
        ea1 = 0.0 # Se encontró la raíz exacta
        
    xr1_ant = xr1
    iter1 += 1

print(f"-> Raíz aproximada: {xr1:.4f} (con error {ea1:.2f}% < 10%)")

# ---------------------------------------------------------
# EJERCICIO 2
# ---------------------------------------------------------
print("\n--- Ejercicio 2 ---")
# Función: ln(x^2) = 0.7  =>  f(x) = ln(x^2) - 0.7
def f2(x):
    return np.log(x**2) - 0.7

# a) Gráficamente
x_vals2 = np.linspace(0.1, 3, 100)
y_vals2 = f2(x_vals2)

plt.figure(figsize=(8, 5))
plt.plot(x_vals2, y_vals2, label="f(x) = ln(x^2) - 0.7", color="green")
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.grid(True)
plt.title("Ejercicio 2: Método Gráfico")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()

# b) Bisección (3 iteraciones)
xl2, xu2 = 0.5, 2.0
print(f"Bisección (3 iteraciones, xl={xl2}, xu={xu2}):")
for i in range(3):
    xr2 = (xl2 + xu2) / 2.0
    print(f"Iteración {i+1}: xr = {xr2:.4f}")
    if f2(xl2) * f2(xr2) < 0:
        xu2 = xr2
    else:
        xl2 = xr2

# c) Falsa Posición (3 iteraciones)
xl2_fp, xu2_fp = 0.5, 2.0
print(f"\nFalsa Posición (3 iteraciones, xl={xl2_fp}, xu={xu2_fp}):")
for i in range(3):
    f_xl = f2(xl2_fp)
    f_xu = f2(xu2_fp)
    xr2_fp = xu2_fp - (f_xu * (xl2_fp - xu2_fp)) / (f_xl - f_xu)
    print(f"Iteración {i+1}: xr = {xr2_fp:.4f}")
    if f2(xl2_fp) * f2(xr2_fp) < 0:
        xu2_fp = xr2_fp
    else:
        xl2_fp = xr2_fp

# ---------------------------------------------------------
# EJERCICIO 3
# ---------------------------------------------------------
print("\n--- Ejercicio 3 ---")
# Función original: f(x) = 2*sen(sqrt(x)) - x = 0
# Despejando x para Punto Fijo: g(x) = 2*sen(sqrt(x))
def g3(x):
    return 2 * np.sin(np.sqrt(x))

x3 = 0.5
es3 = 0.001
ea3 = 100.0
iter3 = 0

print(f"Punto Fijo (Valor inicial: x={x3}, Tolerancia: {es3}%):")
print("Iteración | x | Error Aproximado (%)")
print("-" * 35)
while ea3 >= es3:
    x3_nuevo = g3(x3)
    ea3 = calcular_ea(x3_nuevo, x3)
    print(f"{iter3+1:>9} | {x3_nuevo:.6f} | {ea3:.6f}")
    x3 = x3_nuevo
    iter3 += 1

print(f"-> Raíz aproximada: {x3:.6f} lograda en {iter3} iteraciones (Error = {ea3:.5f}%)")
print(f"Verificación: f({x3:.6f}) = {2*np.sin(np.sqrt(x3)) - x3:.8f} (debe ser cercano a 0)")

# ---------------------------------------------------------
# EJERCICIO 4
# ---------------------------------------------------------
print("\n--- Ejercicio 4 ---")
# Función: f(x) = -x^2 + 1.8x + 2.5
def f4(x):
    return -x**2 + 1.8*x + 2.5

# Derivada para Newton-Raphson: f'(x) = -2x + 1.8
def df4(x):
    return -2*x + 1.8

# Despeje para Punto Fijo: x = sqrt(1.8x + 2.5) 
# (Se elige esta forma para asegurar la convergencia cerca de x=5)
def g4(x):
    return np.sqrt(1.8*x + 2.5)

x_inicial = 5.0
es4 = 0.05

# Método de Punto Fijo
x4_pf = x_inicial
ea4_pf = 100.0
iter4_pf = 0

print(f"1. Punto Fijo (Valor inicial: x={x_inicial}):")
print("Iteración | x | Error Aproximado (%)")
print("-" * 35)
while ea4_pf > es4:
    x4_nuevo = g4(x4_pf)
    ea4_pf = calcular_ea(x4_nuevo, x4_pf)
    print(f"{iter4_pf+1:>9} | {x4_nuevo:.6f} | {ea4_pf:.6f}")
    x4_pf = x4_nuevo
    iter4_pf += 1
print(f"-> Raíz (Punto Fijo): {x4_pf:.5f} en {iter4_pf} iteraciones (Error = {ea4_pf:.4f}%)")

# Método de Newton-Raphson
x4_nr = x_inicial
ea4_nr = 100.0
iter4_nr = 0

print(f"\n2. Newton-Raphson (Valor inicial: x={x_inicial}):")
print("Iteración | x | Error Aproximado (%)")
print("-" * 35)
while ea4_nr > es4:
    x4_nuevo = x4_nr - (f4(x4_nr) / df4(x4_nr))
    ea4_nr = calcular_ea(x4_nuevo, x4_nr)
    print(f"{iter4_nr+1:>9} | {x4_nuevo:.6f} | {ea4_nr:.6f}")
    x4_nr = x4_nuevo
    iter4_nr += 1
print(f"-> Raíz (Newton-Raphson): {x4_nr:.5f} en {iter4_nr} iteraciones (Error = {ea4_nr:.4f}%)")

# Comprobación final
print("\nComprobación de la respuesta obtenida (reemplazando en f(x)):")
print(f"f({x4_nr:.5f}) = {f4(x4_nr):.8f} (Cercano a 0)")