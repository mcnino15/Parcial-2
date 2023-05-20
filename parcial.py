from datetime import datetime
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
        self.turnos = []

    def calcular_vidrio_recolectado(self, fecha: datetime) -> float: #Se crea una variable total_vidrio_recolectado
        total_vidrio_recolectado = 0.0 # se inicializa con el valor 0.0. 
        #Esta variable será utilizada para almacenar la cantidad total de vidrio recolectado en la fecha especificada
        carga_dia = {} #Se crea un diccionario vacío llamado carga_dia que se utilizará para almacenar la carga de vidrio recolectado para cada día.

        for turno in self.turnos:
            if turno.fecha_inicio.date() == fecha.date():
                carga_turno = turno.get_carga()
                #Para cada objeto Turno en la lista self.turnos, se verifica si la fecha de inicio del turno (turno.fecha_inicio) es igual a la fecha especificada (fecha). 
                #Esto se hace comparando solo las fechas sin tener en cuenta la hora, utilizando el método date() de los objetos datetime.
                if fecha.date() not in carga_dia:
                    carga_dia[fecha.date()] = carga_turno.vidrio
                    #Si la fecha de inicio del turno coincide con la fecha especificada, 
                    #se obtiene la carga de vidrio recolectado para ese turno utilizando el método get_carga() del objeto Turno. 
                    #La cantidad de vidrio recolectado se obtiene accediendo al atributo vidrio del objeto de carga.
                else:
                    carga_dia[fecha.date()] += carga_turno.vidrio
                    #Se actualiza el diccionario carga_dia con la cantidad de vidrio recolectado para ese día. 
                    #Si el día aún no existe en el diccionario, se crea una nueva entrada con la fecha como clave y la cantidad de vidrio recolectado como valor. 
                    #Si el día ya existe en el diccionario, se suma la cantidad de vidrio recolectado al valor existente.

        if fecha.date() in carga_dia: #Después de iterar a través de todos los turnos, se verifica si la fecha especificada está presente en el diccionario carga_dia.
            total_vidrio_recolectado = carga_dia[fecha.date()]
            #Si la fecha está presente en el diccionario, se actualiza la variable total_vidrio_recolectado con el valor de la cantidad de vidrio recolectado para esa fecha.
        return total_vidrio_recolectado
    
    def calcular_papel_recolectado(self, fecha: datetime) -> float: 
        total_papel_recolectado = 0.0  
        carga_dia = {} 

        for turno in self.turnos:
            if turno.fecha_inicio.date() == fecha.date():
                carga_turno = turno.get_carga()
                #Para cada objeto Turno en la lista self.turnos, se verifica si la fecha de inicio del turno (turno.fecha_inicio) es igual a la fecha especificada (fecha). 
                #Esto se hace comparando solo las fechas sin tener en cuenta la hora, utilizando el método date() de los objetos datetime.
                if fecha.date() not in carga_dia:
                    carga_dia[fecha.date()] = carga_turno.papel
                    #Si la fecha de inicio del turno coincide con la fecha especificada, 
                    #se obtiene la carga de papel recolectado para ese turno utilizando el método get_carga() del objeto Turno. 
                    #La cantidad de papel recolectado se obtiene accediendo al atributo vidrio del objeto de carga.
                else:
                    carga_dia[fecha.date()] += carga_turno.papel
                    #Se actualiza el diccionario carga_dia con la cantidad de papel recolectado para ese día. 
                    #Si el día aún no existe en el diccionario, se crea una nueva entrada con la fecha como clave y la cantidad de vidrio recolectado como valor. 
                    #Si el día ya existe en el diccionario, se suma la cantidad de papel recolectado al valor existente.

        if fecha.date() in carga_dia: #Después de iterar a través de todos los turnos, se verifica si la fecha especificada está presente en el diccionario carga_dia.
            total_papel_recolectado = carga_dia[fecha.date()]
            #Si la fecha está presente en el diccionario, se actualiza la variable total_vidrio_recolectado con el valor de la cantidad de vidrio recolectado para esa fecha.
        return total_papel_recolectado
    #se utiliza datetime para crear objetos datetime que representan fechas y horas específicas, como la fecha y hora de inicio y fin de los turnos de recolección de basura.

    def calcular_plastico_recolectado(self, fecha: datetime) -> float: 
        total_plastico_recolectado = 0.0  
        carga_dia = {} 
        for turno in self.turnos:
            if turno.fecha_inicio.date() == fecha.date():
                carga_turno = turno.get_carga()  
                if fecha.date() not in carga_dia:
                    carga_dia[fecha.date()] = carga_turno.plastico  
                else:
                    carga_dia[fecha.date()] += carga_turno.plastico
             
        if fecha.date() in carga_dia:
            total_plastico_recolectado = carga_dia[fecha.date()] 
        return total_plastico_recolectado
    
    def calcular_metal_recolectado(self, fecha: datetime) -> float: 
        total_metal_recolectado = 0.0  
        carga_dia = {} 
        for turno in self.turnos:
            if turno.fecha_inicio.date() == fecha.date():
                carga_turno = turno.get_carga()  
                if fecha.date() not in carga_dia:
                    carga_dia[fecha.date()] = carga_turno.metal 
                else:
                    carga_dia[fecha.date()] += carga_turno.metal
             
        if fecha.date() in carga_dia:
            total_metal_recolectado = carga_dia[fecha.date()] 
        return total_metal_recolectado
    
    def calcular_material_recolectado(self, fecha: datetime) -> float: #material organico
        total_material_recolectado = 0.0  
        carga_dia = {} 
        for turno in self.turnos:
            if turno.fecha_inicio.date() == fecha.date():
                carga_turno = turno.get_carga()  
                if fecha.date() not in carga_dia:
                    carga_dia[fecha.date()] = carga_turno.material_organico
                else:
                    carga_dia[fecha.date()] += carga_turno.material_organico
             
        if fecha.date() in carga_dia:
            total_material_recolectado = carga_dia[fecha.date()] 
        return total_material_recolectado
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
         print(f"El total de material organico recolectado el {fecha.date()} fue de {material_recolectado} toneladas")
         print (f"﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏")
    elif option == "6":
         print("Gracias por usar nuestro servicios ¡Chauuuuuu!")
         print (f"﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏")
         break 
    else:
        print("Opción no válida, por favor intenta de nuevo.")
        print (f"﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏")