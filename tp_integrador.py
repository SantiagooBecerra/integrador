def registrar_visitas():
    visitas = []  # Crea una lista vacía para guardar los datos de cada visita

    for i in range(3):  # Repite el bloque 3 veces (para registrar 3 estudiantes)
        print(f"\nRegistro #{i+1}")  # Muestra el número de registro actual
        nombre = input("Nombre del estudiante: ")  # Pide el nombre del estudiante
        curso = input("Curso: ")  # Pide el curso del estudiante
        motivo = input("Motivo por el que entra a la MakerSpace: ")  # Pide el motivo de la visita

        visita = {  # Crea un diccionario con los datos ingresados
            "nombre": nombre,
            "curso": curso,
            "motivo": motivo
        }
        visitas.append(visita)  # Agrega el diccionario a la lista de visitas

    return visitas  # Devuelve la lista de visitas


def mostrar_datos(visitas):
    print("\n--- Lista de estudiantes que ingresaron a la MakerSpace ---")
    for visita in visitas:  # Recorre cada visita en la lista
        print(f"{visita['nombre']} - {visita['curso']} - Motivo: {visita['motivo']}")  # Muestra los datos

    cursos = {}  # Crea un diccionario vacío para contar visitas por curso
    for visita in visitas:  # Recorre cada visita
        curso = visita["curso"]  # Obtiene el curso
        if curso in cursos:  # Si el curso ya está en el diccionario
            cursos[curso] += 1  # Suma 1 al contador
        else:
            cursos[curso] = 1  # Si no existe, lo agrega con valor 1

    print("\n--- Cantidad de visitas por curso ---")
    for curso, cantidad in cursos.items():  # Recorre cada curso y su cantidad
        print(f"{curso}: {cantidad} estudiante(s) ingresaron")  # Muestra el resultado

    print("\nPrimer estudiante que ingresó a la MakerSpace:")
    print(visitas[0]["nombre"])  # Muestra el nombre del primer estudiante


def main():
    visitas = registrar_visitas()  # Llama a la función para registrar visitas y guarda el resultado
    mostrar_datos(visitas)  # Llama a la función para mostrar los datos


if __name__ == "__main__":
    main()  # Ejecuta la función principal si el archivo se ejecuta directamente
