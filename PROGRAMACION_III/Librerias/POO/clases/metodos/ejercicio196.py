class Contacto:
    def __init__(self, nombre, telefono, mail):
        self.nombre = nombre
        self.telefono = telefono
        self.mail = mail

    def __str__(self):
        return f"Nombre: {self.nombre} | Teléfono: {self.telefono} | Email: {self.mail}"

class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self):
        nombre = input("Ingrese el nombre: ")
        telefono = input("Ingrese el teléfono: ")
        mail = input("Ingrese el mail: ")
        self.contactos.append(Contacto(nombre, telefono, mail))
        print("Contacto agregado correctamente.\n")

    def mostrar_agenda(self):
        if not self.contactos:
            print("La agenda está vacía.\n")
            return
        print("Listado completo de la agenda:")
        for contacto in self.contactos:
            print(contacto)
        print()

    def buscar_contacto(self):
        nombre = input("Ingrese el nombre a buscar: ")
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                print("Contacto encontrado:")
                print(contacto, "\n")
                return
        print("Contacto no encontrado.\n")

    def modificar_contacto(self):
        nombre = input("Ingrese el nombre del contacto a modificar: ")
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                nuevo_telefono = input("Ingrese el nuevo teléfono: ")
                nuevo_mail = input("Ingrese el nuevo mail: ")
                contacto.telefono = nuevo_telefono
                contacto.mail = nuevo_mail
                print("Datos actualizados correctamente.\n")
                return
        print("Contacto no encontrado.\n")

    def ejecutar(self):
        while True:
            print("Agenda Personal - Menú de opciones:")
            print("1 - Cargar un contacto")
            print("2 - Listado completo de la agenda")
            print("3 - Consulta por nombre")
            print("4 - Modificar teléfono y mail")
            print("5 - Finalizar programa")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.agregar_contacto()
            elif opcion == "2":
                self.mostrar_agenda()
            elif opcion == "3":
                self.buscar_contacto()
            elif opcion == "4":
                self.modificar_contacto()
            elif opcion == "5":
                print("Finalizando programa...")
                break
            else:
                print("Opción inválida. Intente nuevamente.\n")


# Ejecutar el programa
agenda = Agenda()
agenda.ejecutar()
