frutas = []

for i in range(10):
    print(f"Ingrese los datos de la fruta {i+1}:")
    nombre = input("Nombre de la fruta: ")
    
    
    while True:
        precio = input("Precio de la fruta: ")
        if precio.replace('.', '', 1).isdigit() and precio.count('.') <= 1:
            precio = float(precio)
            if precio > 0:
                break
            else:
                print("Por favor ingrese un precio válido mayor a 0.")
        else:
            print("Por favor ingrese un precio válido (número positivo).")

    # Almacenar la fruta en un diccionario
    fruta = {"nombre": nombre, "precio": precio}
    frutas.append(fruta)

for i in range(len(frutas)):
    for j in range(i + 1, len(frutas)):
        if frutas[i]['precio'] < frutas[j]['precio']:
            # Intercambiar los elementos si están en el orden incorrecto
            frutas[i], frutas[j] = frutas[j], frutas[i]

print("\nFrutas ordenadas por precio (de mayor a menor):")
for fruta in frutas:
    print(f"{fruta['nombre']} - {fruta['precio']:.2f}")