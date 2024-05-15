import random

class Superviviente:
    def __init__(self, nombre, vida, proteccion):
        self.nombre = nombre
        self.vida = vida
        self.proteccion = proteccion
        self.vivo = True

    def recibir_ataque_zombie(self):
        if self.vivo:
            ataque = random.randint(1, 10)
            if self.proteccion > 0:
                dano_proteccion = min(ataque, self.proteccion)
                self.proteccion -= dano_proteccion
                print(f"{self.nombre} ha recibido {dano_proteccion} de daño de un ataque zombie a su protección.")
                if self.proteccion == 0:
                    dano_vida = ataque - dano_proteccion
                    self.vida -= dano_vida
                    print(f"{self.nombre} ha recibido {dano_vida} de daño a su vida por el ataque zombie.")
                    if self.vida <= 0:
                        self.vivo = False
                        print(f"{self.nombre} ha muerto debido al ataque zombie.")
            else:
                self.vida -= ataque
                print(f"{self.nombre} ha recibido {ataque} de daño a su vida por el ataque zombie.")
                if self.vida <= 0:
                    self.vivo = False
                    print(f"{self.nombre} ha muerto debido al ataque zombie.")
        else:
            print(f"{self.nombre} ya está muerto.")

    def mejorar_proteccion(self):
        if self.vivo and self.proteccion < 8:  # Umbral de protección
            mejora = random.randint(1, 5)
            self.proteccion += mejora
            print(f"{self.nombre} ha mejorado su protección en {mejora} puntos.")
        else:
            print(f"{self.nombre} no mejora la protección esta vez.")

    def evento_desventajoso(self):
        if self.vivo and (self.vida < 40 or self.proteccion < 5):  # Umbrales para tomar decisiones
            perdida_recursos = random.randint(1, 3)
            if self.proteccion > 0:
                dano_proteccion = min(perdida_recursos, self.proteccion)
                self.proteccion -= dano_proteccion
                print(f"{self.nombre} ha perdido {dano_proteccion} de protección por un evento desventajoso.")
                if self.proteccion == 0:
                    dano_vida = perdida_recursos - dano_proteccion
                    self.vida -= dano_vida
                    print(f"{self.nombre} ha perdido {dano_vida} de vida por el evento desventajoso.")
                    if self.vida <= 0:
                        self.vivo = False
                        print(f"{self.nombre} ha muerto debido al evento desventajoso.")
            else:
                self.vida -= perdida_recursos
                print(f"{self.nombre} ha perdido {perdida_recursos} de vida por un evento desventajoso.")
                if self.vida <= 0:
                    self.vivo = False
                    print(f"{self.nombre} ha muerto debido al evento desventajoso.")
        else:
            print(f"{self.nombre} no enfrenta el evento desventajoso esta vez.")

    def mostrar_estado(self):
        if self.vivo:
            print(f"Estado de {self.nombre}: Vida - {self.vida}, Protección - {self.proteccion}")
        else:
            print(f"{self.nombre} está muerto.")


# Crear supervivientes
supervivientes = [
    Superviviente("Juan", 50, 5),
    Superviviente("María", 60, 3)
]

# Función para verificar si todos los supervivientes están muertos
def supervivientes_vivos():
    for superviviente in supervivientes:
        if superviviente.vivo:
            return True
    return False

# Función para ejecutar un día con eventos aleatorios
def ejecutar_dia():
    eventos = [superviviente.mejorar_proteccion for superviviente in supervivientes] + \
              [superviviente.evento_desventajoso for superviviente in supervivientes]
    eventos_del_dia = random.sample(eventos, random.randint(1, len(supervivientes) * 2))

    print("\n¡Comienza un nuevo día!")
    for evento in eventos_del_dia:
        evento()

    print("\n¡Ataque zombie!")
    for superviviente in supervivientes:
        superviviente.recibir_ataque_zombie()

    # Mostrar estado al final del día
    for superviviente in supervivientes:
        superviviente.mostrar_estado()


# Ejecutar el juego hasta que todos los supervivientes mueran
dia = 1
while supervivientes_vivos():
    print(f"\n---- Día {dia} ----")
    ejecutar_dia()
    dia += 1

print("\nEl juego ha terminado, todos los supervivientes han muerto.")
