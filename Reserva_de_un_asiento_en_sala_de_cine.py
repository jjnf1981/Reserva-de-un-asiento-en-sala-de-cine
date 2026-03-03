#Se establece la matriz y se la encera
matrix = [[0 for col in range(4)] for fil in range(3)]

# Menú de presentación
print("-" * 50)
print()
print("=== PROGRAMA DE RESERVA DE ASIENTOS ===")
print("\n=== ASIENTOS DISPONIBLES ===\n")
for fil in range(3):
    for col in range(4):
        # Presentación de cada asiento disponible
        print(f"[{matrix[fil][col]:2}", end="] ")
    print()
print()
print("-" * 50)
print()
print("Ingrese solo números enteros")
print()
fil=int(input("Ingrese el número de fila del asiento a reservar: " ))
col=int(input("Ingrese el número de columna del asiento a reservar: " ))
matrix[fil-1][col-1] = 1
print()
print("-" * 50)
print("\n=== ASIENTOS RESERVADOS Y DISPONIBLES ===\n")
for fil in range(3):
    for col in range(4):
        # Presentación de cada asiento disponible
        print(f"[{matrix[fil][col]:3}", end="] ")
    print()
print()