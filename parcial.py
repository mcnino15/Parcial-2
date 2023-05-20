from datetime import datetime
from collections import defaultdict
class PuntoGeografico:
    def __init__(self, latitud: float, longitud: float):
        self.latitud = latitud
        self.longitud = longitud

class Carga:
    def __init__(self, id_carga: int, vidrio: float, papel: float, plastico: float, metal: float, material_organico: float):
        self.id_carga = id_carga
        self.vidrio = vidrio
        self.papel = papel
        self.plastico = plastico
        self.metal = metal
        self.material_organico = material_organico
class Ruta:
    def __init__(self, info_ruta: int, puntos: list[PuntoGeografico]):
        self.info_ruta = info_ruta #una variable de instancia que almacena el valor del argumento info_ruta pasado al constructor.
        self.puntos = puntos # una variable de instancia que almacena el valor del argumento puntos pasado al constructor, que debe ser una lista de objetos de la clase PuntoGeografico.
    
class Turno:
    def __init__(self, info_turno: int, camion: str, conductor: str, asistente1: str, asistente2: str, ruta: Ruta, fecha_inicio: datetime, fecha_fin: datetime, tiempo: int):
        self.info_turno = info_turno
        self.camion = camion
        self.conductor = conductor
        self.asistente1 = asistente1
        self.asistente2 = asistente2
        self.ruta = ruta
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.tiempo = tiempo
        self.carga = None

    def set_carga(self, carga: Carga): #es un método que acepta un argumento carga del tipo Carga y establece el valor de la variable de instancia self.carga con el valor de carga
        self.carga = carga

    def get_carga(self): #get_carga es un método que no acepta argumentos y simplemente devuelve el valor de la variable de instancia self.carga. 
    #Es decir, retorna el valor de la variable carga dentro del objeto (instancia) de la clase.
        return self.carga
class TrashCity: 
    def __init__(self):
     self.registro_turnos = []

    def recibir_turno(self, turno):
        self.registro_turnos.append(turno)

    def obtener_total_residuos(self):
        total_carga = defaultdict(float)

        for turno in self.registro_turnos:
            for ruta, carga in turno.carga_por_ruta.items():
                for tipo_residuo, cantidad in carga.items():
                    total_carga[tipo_residuo] += cantidad

        return total_carga

    def obtener_residuos_por_ruta(self):
        residuos_por_ruta = defaultdict(lambda: defaultdict(float))

        for turno in self.registro_turnos:
            ruta = turno.camion.ruta
            carga_por_ruta = turno.carga_por_ruta

            for ruta, carga in carga_por_ruta.items():
                residuos = residuos_por_ruta[ruta]

                for tipo_residuo, cantidad in carga.items():
                    residuos[tipo_residuo] += cantidad

        return residuos_por_ruta
from datetime import datetime


punto1 = PuntoGeografico(9.123603, -75.581242)
punto2 = PuntoGeografico(9.157315, -75.574897)
punto3 = PuntoGeografico(9.179732, -75.586095)

ruta1 = Ruta(1, [punto1, punto2, punto3])
carga_vidrio1 = Carga(1, 1.5, 2.5, 1.0, 2.5, 2.0) # valores de la carga del vidrio
carga1p = Carga(2, 0.5, 1.5, 1.2, 0.8, 1)  # valores de la carga del papel
carga1pl = Carga(0.5, 0.2, 0.1, 0.4, 0.3, 0.2) # valores de la carga del plastico
carga1m = Carga(2, 1.2, 1.0, 2.0, 1.1, 0.2)
carga1_material = Carga(0.2, 0.4, 0.5, 0.5,1,0.6)
turno1 = Turno(1, "Camión 1", "Brian lopez", "Nicolas Rodriguez", None, ruta1, datetime(2023, 5, 19, 7, 0, 0), datetime(2023, 4, 1, 11, 0, 0), 4*60)
#Es el noveno argumento que se pasa al constructor de la clase Turno y representa la duración máxima en minutos del turno. En este caso se establece como 4 horas multiplicadas por 60 minutos, lo que resulta en 240 minutos, es decir, 4 horas de duración para el turno.
turno1.set_carga(carga_vidrio1)
turno1.set_carga(carga1p)
turno1.set_carga(carga1pl)
turno1.set_carga(carga1m)
turno1.set_carga(carga1_material)

punto3 = PuntoGeografico(9.123603, -75.581242)
punto4 = PuntoGeografico(9.157315, -75.574897)
punto5 = PuntoGeografico(9.179732, -75.586095)
ruta2 = Ruta(2, [punto3, punto4, punto5])
carga_vidrio2 = Carga(2, 1.0, 2.0, 2.5, 1.5, 3.0)
carga2p = Carga(3, 1, 2.3, 0.1, 1, 0.2)
carga2pl = Carga(0.1, 1, 0.3, 0.2, 1, 0.5)
carga2m = Carga(3, 1.0, 2.0, 2.5, 0.5, 3.0)
carga2_material = Carga (0.9, 0.5, 0.1, 0.8, 0.6, 0.4)
turno2 = Turno(2, "Camión 2", "Pedro", "Santana", "Martin", ruta2, datetime(2023, 5, 19, 12, 0, 0), datetime(2023, 4, 1, 17, 0, 0), 4*60)
turno2.set_carga(carga_vidrio2)
turno2.set_carga(carga2p)
turno2.set_carga(carga2pl)
turno2.set_carga(carga2m)
turno2.set_carga(carga2_material)
trash_city = TrashCity()
trash_city.turnos.append(turno1)
trash_city.turnos.append(turno2)

fecha = datetime(2023, 5, 19)
vidrio_recolectado = trash_city.calcular_vidrio_recolectado(fecha)
papel_recolectado = trash_city.calcular_papel_recolectado(fecha)
plastico_recolectado = trash_city.calcular_plastico_recolectado(fecha)
metal_recolectado = trash_city.calcular_metal_recolectado(fecha)
material_recolectado = trash_city.calcular_material_recolectado(fecha)
print (f"﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏")
print("Bienvenido a TrashCity")
while True:
    print ("¿Que desea hacer?")
    print("1. Ver total de vidrio recolectado")
    print("2. Ver total de papel recolectado")
    print ("3. Ver total de plastico recolectado")
    print ("4. Ver total de metal recolectado")
    print ("5. Ver total de material recolectado")
    print ("6. Salir")
    option =  input("Ingresa tu opción (1, 2, 3 , 4, 5, 6): ")
    print (f"﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏")
    if option == "1":
        print(f"El total de vidrio recolectado el {fecha.date()} fue de {vidrio_recolectado} toneladas")
        print (f"﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏")
    elif option == "2":
         print(f"El total de papel recolectado el {fecha.date()} fue de {papel_recolectado} toneladas")
         print (f"﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏")
    elif option == "3":
         print(f"El total de plastico recolectado el {fecha.date()} fue de {plastico_recolectado} toneladas")
         print (f"﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏")
    elif option == "4":
         print(f"El total de metal recolectado el {fecha.date()} fue de {metal_recolectado} toneladas")
         print(f"﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏")
    elif option == "5":
         print(f"El total de material organico recolectado el {fecha.date()} fue de {material_recolectado} toneladas")
         print (f"﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏")
    elif option == "6":
         print("Gracias por usar nuestro servicios ¡Chauuuuuu!")
         print (f"﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏")
         break 
    else:
        print("Opción no válida, por favor intenta de nuevo.")
        print (f"﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏")