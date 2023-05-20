from collections import defaultdict #Proporciona un valor predeterminado cuando se 
#accede a una clave inexistente en el diccionario, evitando errores KeyError
# Almacena carga y residuos por ruta en las clases Turno y CentroAcopio..

class Ruta:
    def __init__(self, puntos):
        self.puntos = puntos # Lista de puntos geográficos que componen la ruta


class Camion:
    def __init__(self, conductor, asistente1, asistente2, ruta):
        self.conductor = conductor # Objeto que representa al conductor
        self.asistente1 = asistente1
        self.asistente2 = asistente2
        self.ruta = ruta     #Indica la ruta asignada al camión


class Persona:
    def __init__(self, nombre, identificacion):
        self.nombre = nombre
        self.identificacion = identificacion


class Turno:
    def __init__(self, camion, inicio, fin):
        self.camion = camion # Representa el camión asignado al turno
        self.inicio = inicio  # Fecha y hora de inicio del turno
        self.fin = fin  # Fecha y hora de finalización del turno
        self.localizaciones = []  # Lista de localizaciones del camión durante el turno
        self.carga_por_ruta = defaultdict(lambda: defaultdict(float))  # Diccionario para almacenar la carga de residuos por ruta

    def agregar_localizacion(self, latitud, longitud, tiempo):
        self.localizaciones.append((latitud, longitud, tiempo)) # Agrega una localización a la lista de localizaciones del turno

    def clasificar_carga(self, ruta_actual, vidrio, papel, plastico, metal, organicos):
        ruta_actual += 1 # Incrementa el número de la ruta actual en 1 para que no comience en 0
        self.carga_por_ruta[ruta_actual]['vidrio'] += vidrio
        self.carga_por_ruta[ruta_actual]['papel'] += papel
        self.carga_por_ruta[ruta_actual]['plastico'] += plastico
        self.carga_por_ruta[ruta_actual]['metal'] += metal
        self.carga_por_ruta[ruta_actual]['organicos'] += organicos
         # Agrega la cantidad de residuo a la carga de residuos de la ruta actual

class CentroAcopio:
    def __init__(self):
        self.registro_turnos = [] # Lista para almacenar los turnos registrados en el centro de acopio

    def recibir_turno(self, turno):
        self.registro_turnos.append(turno)  # Agrega un turno al registro de turnos del centro de acopio

    def obtener_total_residuos(self):
        total_carga = defaultdict(float)  # Diccionario para almacenar la cantidad total de cada tipo de residuo

        for turno in self.registro_turnos:
            for ruta, carga in turno.carga_por_ruta.items():
                for tipo_residuo, cantidad in carga.items():
                    total_carga[tipo_residuo] += cantidad  # Acumula la cantidad de residuos por tipo en el diccionario total_carga


        return total_carga  # Devuelve el diccionario con la cantidad total de residuos por tipo

    def obtener_residuos_por_ruta(self):
        residuos_por_ruta = defaultdict(lambda: defaultdict(float))  # Diccionario anidado para almacenar la cantidad de residuos por ruta

        for turno in self.registro_turnos:
            ruta = turno.camion.ruta # Obtiene la ruta asignada al camión del turno actual
            carga_por_ruta = turno.carga_por_ruta # Obtiene la carga de residuos por ruta del turno actual

            for ruta, carga in carga_por_ruta.items(): # Obtiene el diccionario de residuos correspondiente a la ruta actual
                residuos = residuos_por_ruta[ruta]  

                for tipo_residuo, cantidad in carga.items(): # Acumula la cantidad de residuos por tipo en el diccionario de residuos de la ruta actual
                    residuos[tipo_residuo] += cantidad

        return residuos_por_ruta


# <Implementación
conductor1 = Persona("Sebastian Rullo", "973164503")
asistente11 = Persona("Marina Guerrero", "730102456")
asistente12 = Persona("Nicolas Miranda", "103279450")
ruta1 = Ruta([(40.7128, -74.0060), (40.7394, -73.9881), (40.7580, -73.9855)])

camion1 = Camion(conductor1, asistente11, asistente12, ruta1)

inicio_turno1 = "2023-05-19 08:00:00"  # Ejemplo de fecha y hora de inicio del turno
fin_turno1 = "2023-05-19 12:00:00"  # Ejemplo de fecha y hora de finalización del turno

turno1 = Turno(camion1, inicio_turno1, fin_turno1)
turno1.agregar_localizacion(40.7128, -74.0060, "2023-05-19 08:30:00")
turno1.agregar_localizacion(40.7394, -73.9881, "2023-05-19 10:15:00")
turno1.clasificar_carga(0, 10, 20, 15, 5, 8)
turno1.clasificar_carga(1, 8, 15, 12, 3, 6)

centro_acopio = CentroAcopio()
centro_acopio.recibir_turno(turno1)

# Cálculo y visualización de los resultados
total_residuos = centro_acopio.obtener_total_residuos()
residuos_por_ruta = centro_acopio.obtener_residuos_por_ruta()

# Menú
print("Bienvenido a TrashCity")
while True:
    print ("¿Que desea hacer?")
    print("1. Ver total de residuos recolectados")
    print("2. Ver los residuos por ruta")
    print ("3. Ver los detalles de las rutas")
    print ("4. Salir")
    print(f"‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵")
    option =  input("Ingresa tu opción (1, 2, 3, 4) : ")
    print(f"‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵")
    if option == "1":
      print("Total de residuos recolectados:")
      for tipo_residuo, cantidad in total_residuos.items(): # Recorre el diccionario de residuos totales
        print(f"{tipo_residuo}: {cantidad} toneladas")
      print(f"‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵")
    elif option == "2":
      print("\nResiduos recolectados por ruta:")
      for ruta, residuos in residuos_por_ruta.items(): # Recorre el diccionario de residuos por ruta
       print(f"Ruta {ruta}:")
       for tipo_residuo, cantidad in residuos.items(): # Recorre el diccionario de residuos por tipo en la ruta actual
        print(f"{tipo_residuo}: {cantidad} toneladas")  # Imprime el tipo de residuo y su cantidad correspondiente
      print(f"‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵")
    elif option == "3":
      print("\nInformación de las rutas:")
      for turno in centro_acopio.registro_turnos: # Recorre la lista de turnos registrados en el centro de acopio
        camion = turno.camion
        ruta = camion.ruta
        print(f"\nRuta: {ruta}")
        print(f"Conductor: {camion.conductor.nombre}")
        print(f"Asistente 1: {camion.asistente1.nombre}")
        print(f"Asistente 2: {camion.asistente2.nombre}")
        print("Puntos geográficos:")
        for punto in ruta.puntos: # Recorre los puntos geográficos de la ruta actual
         latitud, longitud = punto
         print(f"Latitud: {latitud}, Longitud: {longitud}")
      print(f"‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵")
    elif option == "4":     
     print("Gracias por usar nuestro servicios ¡Chauuuuuu!")
     print(f"‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵")
     break 
    else:
        print("Opción no válida, por favor intenta de nuevo.")
        print(f"‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵")