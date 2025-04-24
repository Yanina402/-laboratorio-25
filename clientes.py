class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = 0.0

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}, Cuenta: {self.numero_cuenta}, Balance: ${self.balance:.2f}"

    def depositar(self, cantidad):
        self.balance += cantidad
        print(f"Depósito de ${cantidad:.2f} realizado. Nuevo balance: ${self.balance:.2f}")

    def retirar(self, cantidad):
        if cantidad <= self.balance:
            self.balance -= cantidad
            print(f"Retiro de ${cantidad:.2f} realizado. Nuevo balance: ${self.balance:.2f}")
        else:
            print("No se puede retirar más de lo que tiene en la cuenta.")

def crear_cliente():
    nombre = input("Ingrese el nombre del cliente: ")
    apellido = input("Ingrese el apellido del cliente: ")
    numero_cuenta = input("Ingrese el número de cuenta: ")
    return Cliente(nombre, apellido, numero_cuenta)

def inicio():
    cliente = crear_cliente()
    print(cliente)

    while True:
        print("\n¿Qué desea hacer?")
        print("1. Depositar")
        print("2. Retirar")
        print("3. Mostrar balance")
        print("4. Salir")
        opcion = input("Ingrese una opción: ")

        if opcion == '1':
            cantidad = float(input("Ingrese la cantidad a depositar: "))
            cliente.depositar(cantidad)
        elif opcion == '2':
            cantidad = float(input("Ingrese la cantidad a retirar: "))
            cliente.retirar(cantidad)
        elif opcion == '3':
            print(cliente)
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    inicio()