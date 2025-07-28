def registrar_visitas():
    visitas = []

    for i in range(3):
        print(f"\nRegistro #{i+1}")
        nombre = input("Nombre del estudiante: ")
        curso = input("Curso: ")
        motivo = input("Motivo por el que entra a la MakerSpace: ")

        visita = {
            "nombre": nombre,
            "curso": curso,
            "motivo": motivo
        }
        visitas.append(visita)

    return visitas

def mostrar_datos(visitas):
    print("\n--- Lista de estudiantes que ingresaron a la MakerSpace ---")
    for visita in visitas:
        print(f"{visita['nombre']} - {visita['curso']} - Motivo: {visita['motivo']}")

    cursos = {}
    for visita in visitas:
        curso = visita["curso"]
        if curso in cursos:
            cursos[curso] += 1
        else:
            cursos[curso] = 1

    print("\n--- Cantidad de visitas por curso ---")
    for curso, cantidad in cursos.items():
        print(f"{curso}: {cantidad} estudiante(s) ingresaron")

    print("\nPrimer estudiante que ingresó a la MakerSpace:")
    print(visitas[0]["nombre"])

def main():
    visitas = registrar_visitas()
    mostrar_datos(visitas)

if __name__ == "__main__":
    main()
