class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False

class ListaTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion):
        tarea_nueva = Tarea(descripcion)
        self.tareas.append(tarea_nueva)

    def marcar_completada(self, posicion):
        try:
            tarea = self.tareas[posicion]
            tarea.completada = True
        except IndexError:
            print("La posición especificada no existe en la lista.")

    def mostrar_tareas(self):
        for i, tarea in enumerate(self.tareas):
            estado = "Completada" if tarea.completada else "Pendiente"
            print(f"{i + 1}. {tarea.descripcion} ({estado})")

    def eliminar_tarea(self, posicion):
        try:
            del self.tareas[posicion]
        except IndexError:
            print("La posición especificada no existe en la lista.")

if __name__ == "__main__":
    lista = ListaTareas()

    while True:
        print("\n--- Gestor de Tareas ---")
        print("1. Agregar tarea")
        print("2. Marcar tarea como completada")
        print("3. Mostrar todas las tareas")
        print("4. Eliminar tarea")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            descripcion = input("Introduce la descripción de la tarea: ")
            lista.agregar_tarea(descripcion)
        elif opcion == "2":
            try:
                posicion = int(input("Introduce la posición de la tarea a marcar como completada: ")) - 1
                lista.marcar_completada(posicion)
            except ValueError:
                print("Por favor, introduce un número válido.")
        elif opcion == "3":
            lista.mostrar_tareas()
        elif opcion == "4":
            try:
                posicion = int(input("Introduce la posición de la tarea a eliminar: ")) - 1
                lista.eliminar_tarea(posicion)
            except ValueError:
                print("Por favor, introduce un número válido.")
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
