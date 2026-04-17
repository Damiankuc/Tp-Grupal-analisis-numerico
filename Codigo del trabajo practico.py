import math

# 1. Definimos la función y su derivada
def f(x):
    return math.exp(x) - 3 * x**2

def df(x):
    return math.exp(x) - 6 * x
#2. Definimos el criterio de error esperado
#  (4 cifras significativas)
# es: Tolerancia de error relativo esperado en porcentaje (%).
#     Para n cifras significativas: es = 0.5 * 10^(2 - n) %
#     Aquí n=4 => es = 0.005 %
es = 0.5 * 10**(2-4)

# --- a) Método de la Falsa Posición ---
def falsa_posicion(f, xl, xu, es, max_iter=100):
    
   #Método de la Falsa Posición (Regula Falsi).
   # Encuentra raíz de f(x)=0 en intervalo inicial [xl, xu] donde f(xl)*f(xu) <= 0.
    #xd
   # Parámetros:
    #- f: función a evaluar
    #- xl: límite INFERIOR inicial del intervalo de búsqueda
    #- xu: límite SUPERIOR inicial del intervalo de búsqueda
    #- es: tolerancia de error relativo aproximado (%)
    #- max_iter: número MÁXIMO de iteraciones permitidas (default: 100)
    
    #Retorna: (raíz aproximada, iteraciones usadas, error último %)

    if f(xl) * f(xu) > 0:
        return None, 0, 100 # No hay cambio de signo
    
    xr_old = xl
    for i in range(1, max_iter + 1):
        # Fórmula del método de Falsa Posición:
        # xr = xu - [f(xu) * (xl - xu)] / [f(xl) - f(xu)]
        # Donde:
        # - xr: nueva aproximación a la raíz
        # - (xl - xu): ancho del intervalo actual
        # - f(xl), f(xu): evaluaciones en límites
        xr = xu - (f(xu) * (xl - xu)) / (f(xl) - f(xu))
        
        # Error aproximado relativo porcentual:
        # ea = | (xr - xr_old) / xr | * 100 %
        # Donde xr_old: aproximación anterior
        if xr != 0:
            ea = abs((xr - xr_old) / xr) * 100
        else:
            ea = 100
            
        # Actualizar intervalo según signo de f(xl)*f(xr)
        test = f(xl) * f(xr)
        if test < 0:
            xu = xr
        elif test > 0:
            xl = xr
        else:
            ea = 0 # Raíz exacta encontrada
            
        if ea < es and i > 1: # Verificar después de 1ra iteración
            return xr, i, ea
            
        xr_old = xr
    return xr, max_iter, ea

# --- c) Método de Newton-Raphson ---
def newton_raphson(f, df, x0, es, max_iter=100):

#Método de Newton-Raphson.
#Aproximación iterativa usando derivada.
    
    # - f: función
   # - x0: valor INICIAL de aproximación (equivalente a xl o xu medio)
   # - es: tolerancia de error relativo (%)
   # - max_iter: máx iteraciones (default: 100)
    
    xr_old = x0
    for i in range(1, max_iter + 1):
        # Fórmula de Newton-Raphson:
        # xr = xr_old - f(xr_old) / df(xr_old)
        # Donde:
        # - xr: nueva aproximación
        # - f(xr_old)/df(xr_old): corrección basada en tangente
        xr = xr_old - f(xr_old) / df(xr_old)
        
        # ea = | (xr - xr_old) / xr | * 100 %
        if xr != 0:
            ea = abs((xr - xr_old) / xr) * 100
        else:
            ea = 100
            
        if ea < es:
            return xr, i, ea
            
        xr_old = xr
    return xr, max_iter, ea

# --- d) Método de la Secante ---
def secante(f, x0, x1, es, max_iter=100):

    #Método de la Secante (similar a falsa posición pero sin derivada).
    
    #Parámetros
    #- f: función
    #- x0: primera aproximación inicial (equivalente a xl)
    #- x1: segunda aproximación inicial (equivalente a xu)
    #- es: tolerancia (%)
    #- max_iter: máx iteraciones (100)
    # Retorna: (raíz aproximada, iteraciones usadas, error último %)
    for i in range(1, max_iter + 1):
        # Fórmula de la Secante:
        # xr = x1 - [f(x1) * (x0 - x1)] / [f(x0) - f(x1)]
        # Similar a falsa posición, pero x0/x1 se actualizan como aproximaciones
        xr = x1 - (f(x1) * (x0 - x1)) / (f(x0) - f(x1))
        
        # ea = | (xr - x1) / xr | * 100 %
        if xr != 0:
            ea = abs((xr - x1) / xr) * 100
        else:
            ea = 100
            
        if ea < es:
            return xr, i, ea
            
        x0 = x1
        x1 = xr
    return xr, max_iter, ea

# ==========================================
# Ejecución y resultados
# ==========================================

intervalos = [(0, 1), (3, 5)]

print(f"Criterio de error (es): {es}%\\n")

#Resultados para cada método en cada intervalo
for (a, b) in intervalos:
    print("-" * 50)
    print(f"Buscando raíz en el intervalo [{a}, {b}]")
    print("-" * 50)
    
    # a) Falsa Posición
    raiz_fp, iter_fp, ea_fp = falsa_posicion(f, a, b, es)
    if raiz_fp is not None:
        print(f"Falsa Posición : Raíz = {raiz_fp:.6f} | Iteraciones = {iter_fp:2} | Error = {ea_fp:.6f}%")
    else:
        print("Falsa Posición : No aplicable (f(xl)*f(xu) > 0)")
        
    # c) Newton-Raphson (Usamos el límite superior 'b' como valor inicial x0)
    raiz_nr, iter_nr, ea_nr = newton_raphson(f, df, b, es)
    print(f"Newton-Raphson : Raíz = {raiz_nr:.6f} | Iteraciones = {iter_nr:2} | Error = {ea_nr:.6f}%")
    
    # d) Secante (Usamos 'a' y 'b' como valores iniciales x0 y x1)
    raiz_sec, iter_sec, ea_sec = secante(f, a, b, es)
    print(f"Secante        : Raíz = {raiz_sec:.6f} | Iteraciones = {iter_sec:2} | Error = {ea_sec:.6f}%")
    print()

