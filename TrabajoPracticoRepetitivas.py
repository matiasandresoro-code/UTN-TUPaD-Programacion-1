""" Ejercicio 1 ------- Caja de Kiosco"""

nombre = input("Cliente: ")

while not nombre.isalpha():
    nombre = input("Vuelva a ingresar su nombre. Solo utilice letras, por favor:")

cantidad_productos = input("Cantidad de Productos: ")

while not cantidad_productos.isdigit() or int(cantidad_productos)<=0:
    cantidad_productos = input("Vuelva a ingresar la cantidad. Solo ingrese numeros mayor que cero: ")

total = 0
ahorro = 0
total_con_descuento = 0
for i in range(1, int(cantidad_productos)+1):
    print(f"Producto {i} - ",end=" ")
    precio = input("Precio: ")
    while not precio.isdigit():
        precio = input("Ingrese solo numeros enteros:")
    descuento = input("Descuento S/N: " ).lower()
    while not descuento in "sn":
        descuento = input("Ingrese solo S o N:").lower()
    
    total = total + int(precio)
    if descuento == "s":
        ahorro = ahorro + int(precio)*0.1
        total_con_descuento = total_con_descuento + int(precio)*0.9
    else: 
        total_con_descuento = total_con_descuento + int(precio)

promedio = total_con_descuento / int(cantidad_productos)
print("********************************")
print(f"Total sin descuentos: ${total}")
print(f"Total con descuentos: ${total_con_descuento}")
print(f"Ahorro: ${ahorro}")
print(f"Promedio por producto: ${promedio:.2f}")



""" Ejercicio 2 — “Acceso al Campus y Menú Seguro”"""

usuario = "alumno"
password = "python123"

usuario_correcto = False
for i in range(3):
    print(f"Intento {i+1}/3")
    usuario_ingresado = input("Usuario: ")
    password_ingresado = input("Contraseña: ")

    if usuario_ingresado == usuario and password_ingresado == password:
        print("Ingreso correctamente.\n")
        usuario_correcto = True
        break
    elif i ==2:
        print("Cuenta Bloqueada.")

    else:
        print("Error: credenciales invalidas.\n")
        

while usuario_correcto:
    eleccion = input("\nIngrese el numero de la accion a realizar.\n1. Ver estado de inscripcion.\n2. Cambiar clave.\n3. Mostrar mensaje motivacional.\n4. Salir.\n") 
    if not eleccion.isdigit():
        print("Error: ingrese un numero valido.")
    elif int(eleccion)<1 or int(eleccion)>4:
        print("Error: opcion fuera de rango.")
    elif eleccion=="1":
        print("Inscripto.")
    elif eleccion=="2":
        flag2=True
        while flag2:
            clave_nueva = input("Ingrese su clave nueva: ")
            if len(clave_nueva)<6:
                print("Error: minimo 6 caracteres.")
                continue
            else:
                confirmacion_clave= input("Repita la clave nueva: ")
        
            if clave_nueva == confirmacion_clave:
                password = confirmacion_clave
                print("Clave cambiada exitosamente.\n")
                break
            else: 
                print("Las claves no coinciden.")
        
    elif eleccion == "3":
        print("El éxito es la suma de pequeños esfuerzos, repetidos día tras día.")
    elif eleccion == "4":
        print("Hasta luego!")
        usuario_correcto = False

    


""" Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)”"""

"""Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)”"""


lunes1 = ""
lunes2 =""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = "" 
martes3 = ""

flag31 = True
while flag31:
    nombre_operador = input("Ingrese nombre del operador: ")
    if nombre_operador.isalpha():
        flag32 = True
        while flag32:
            print("Ingrese el numero de la accion que desea realizar:\n1. Reservar turno.\n2. Cancelar turno (por nombre).\n3. Ver agenda del dia.\n4. Ver resumen general.\n5. Cerrar sistema ")
            eleccion3 = input("")
            match eleccion3:
                case "1":
                    flag34 = True
                    while flag34:
                        print("Elige el dia (escriba el numero correspondiente):\n1. Lunes\n2. Martes")
                        dia = input("")
                        if dia == "1" or dia =="2":
                            break
                        print("Error: ingrese una opcion valida.")
                    flag33 = True
                    while flag33:
                        print("Ingrese el nombre del paciente: ")
                        paciente = input("")
                        if paciente.isalpha():
                            break
                        
                        print("Error: ingrese solo letras.")

                    if dia == "1":
                        if lunes1 == paciente or lunes2 == paciente or lunes3 == paciente or lunes4 == paciente:
                            print("Ya hay un turno para ese paciente.")
                        elif lunes1 == "":
                            lunes1 = paciente
                            print(f"Turno asignado en el horario 1 al paciente {paciente}")
                        elif lunes2 == "":
                            lunes2 = paciente
                            print(f"Turno asignado en el horario 2 al paciente {paciente}")
                        elif lunes3 == "":
                            lunes3 = paciente
                            print(f"Turno asignado en el horario 3 al paciente {paciente}")
                        elif lunes4 == "":
                            lunes4 = paciente
                            print(f"Turno asignado en el horario 4 al paciente {paciente}")
                        else:
                            print("No hay turnos disponibles para el lunes.")
                    elif dia == "2":
                        if martes1 == paciente or martes2 == paciente or martes3 == paciente:
                            print("Ya hay un turno para ese paciente.")
                        elif martes1 == "":
                            martes1 = paciente
                            print(f"Turno asignado en el horario 1 al paciente {paciente}")
                        elif martes2 == "":
                            martes2 = paciente
                            print(f"Turno asignado en el horario 2 al paciente {paciente}")
                        elif martes3 == "":
                            martes3 = paciente
                            print(f"Turno asignado en el horario 3 al paciente {paciente}")
                       

                case "2":
                    flag35 = True
                    while flag35:
                        print("Elige el dia (escriba el numero correspondiente):\n1. Lunes\n2. Martes")
                        dia2 = input("")
                        if dia2 == "1" or dia2 == "2":
                            break
                        print("Error: ingrese solo un numero.")
                    flag36 = True
                    while flag36:
                        print("Ingrese el nombre del paciente: ")
                        paciente_a_cancelar = input("")
                        if paciente_a_cancelar.isalpha():
                            break
                        print("Error: ingrese solo letras.")
                    if dia2 == "1":
                        if lunes1 == paciente_a_cancelar or lunes2 == paciente_a_cancelar or lunes3 == paciente_a_cancelar or lunes4 == paciente_a_cancelar:
                            if lunes1 == paciente_a_cancelar:
                                lunes1 = ""
                                print(f"El turno para el paciente {paciente_a_cancelar} en el horario 1 ha sido cancelado.")
                            elif lunes2 == paciente_a_cancelar:
                                lunes2 = ""
                                print(f"El turno para el paciente {paciente_a_cancelar} en el horario 2 ha sido cancelado.")
                            elif lunes3 == paciente_a_cancelar:
                                lunes3 = ""
                                print(f"El turno para el paciente {paciente_a_cancelar} en el horario 3 ha sido cancelado.")
                            elif lunes4 == paciente_a_cancelar:
                                lunes4 = ""
                                print(f"El turno para el paciente {paciente_a_cancelar} en el horario 4 ha sido cancelado.")
                        else:
                            print("No hay turnos agendados para este paciente.")
                    if dia2 == "2":
                        if martes1 == paciente_a_cancelar or martes2 == paciente_a_cancelar or martes3 == paciente_a_cancelar:
                            if martes1 == paciente_a_cancelar:
                                martes1 = ""
                                print(f"El turno para el paciente {paciente_a_cancelar} en el horario 1 ha sido cancelado.")
                            elif martes2 == paciente_a_cancelar:
                                martes2 = ""
                                print(f"El turno para el paciente {paciente_a_cancelar} en el horario 2 ha sido cancelado.")
                            elif martes3 == paciente_a_cancelar:
                                martes3 = ""
                                print(f"El turno para el paciente {paciente_a_cancelar} en el horario 3 ha sido cancelado.")
                        else:
                            print("No hay turnos agendados para este paciente")
                    
                case "3":
                    
                    flag37 = True
                    while flag37:
                        print("Elige el dia (escriba el numero correspondiente):\n1. Lunes\n2. Martes")
                        dia3 = input("")
                        if dia3 == "1" or dia3 =="2":
                            break
                        print("Error: ingrese una opcion valida.")
                    
                    if dia3 == "1":
                            if lunes1 == "":
                                agenda_lunes1 = "(libre)"
                            else:
                                agenda_lunes1 = lunes1
                            if lunes2 == "":
                                agenda_lunes2 = "(libre)"
                            else:
                                agenda_lunes2 = lunes2
                            if lunes3 == "":
                                agenda_lunes3 = "(libre)"
                            else:
                                agenda_lunes3 = lunes3
                            if lunes4 == "":
                                agenda_lunes4 = "(libre)"
                            else:
                                agenda_lunes4 = lunes4
                            print("Agenda dia Lunes:")
                            print(f"- Turno 1: {agenda_lunes1}.\n- Turno 2: {agenda_lunes2}.\n- Turno 3: {agenda_lunes3}.\n- Turno 4: {agenda_lunes4}.")

                    else:
                        if martes1 == "":
                            agenda_martes1 = "(libre)"
                        else:
                            agenda_martes1 = martes1
                        if martes2 == "":
                            agenda_martes2 = "(libre)"
                        else: 
                            agenda_martes2 = martes2
                        if martes3 =="":
                            agenda_martes3="(libre)"
                        else:
                            agenda_martes3 = martes3
                        print("\nAgenda dia Martes:")
                        print(f"- Turno 1: {agenda_martes1}.\n- Turno 2: {agenda_martes2}.\n- Turno 3: {agenda_martes3}.\n")

                    

                case "4":
                    turnos_ocupados_lunes = 0
                    turnos_libres_lunes = 0
                    turnos_ocupados_martes = 0
                    turnos_libres_martes = 0
                    if lunes1 == "":
                        turnos_libres_lunes +=1
                    else:
                        turnos_ocupados_lunes +=1
                    if lunes2 == "":
                        turnos_libres_lunes +=1
                    else:
                        turnos_ocupados_lunes +=1
                    if lunes3 == "":
                        turnos_libres_lunes +=1
                    else:
                        turnos_ocupados_lunes +=1
                    if lunes4 == "":
                        turnos_libres_lunes +=1
                    else:
                        turnos_ocupados_lunes +=1
                    
                    if martes1 == "":
                        turnos_libres_martes +=1
                    else:
                        turnos_ocupados_martes +=1
                    if martes2 == "":
                        turnos_libres_martes +=1
                    else:
                        turnos_ocupados_martes +=1
                    if martes3 == "":
                        turnos_libres_martes +=1
                    else:
                        turnos_ocupados_martes +=1

                    if turnos_ocupados_lunes == turnos_ocupados_martes:
                        dia_con_mas_turnos = "Empate"
                    elif turnos_ocupados_lunes > turnos_ocupados_martes:
                        dia_con_mas_turnos = "Lunes"
                    else:
                        dia_con_mas_turnos = "Martes"

                    print("\nResumen general:")
                    print(f" --- Dia Lunes --- \n. Turnos ocupados: {turnos_ocupados_lunes}. \n. Turnos libres: {turnos_libres_lunes}.")
                    print(f"\n --- Dia Martes --- \n. Turnos ocupados: {turnos_ocupados_martes}. \n. Turnos libres: {turnos_libres_martes}.")
                    print(f"\n Dia con mas turnos: {dia_con_mas_turnos}")
                        
                    
                    
                    
                    

                case "5":
                    print(f"Hasta luego {nombre_operador}")
                    flag31 = False
                    break
    else:
        print("Error: ingrese solo letras.")

"""Ejercicio 4 — “Escape Room: La Bóveda”"""

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
contador_forzar_cerradura = 0
bloqueo_por_alarma = False
turnos=0
estado_alarma = "Desactivado"
while True:
    nombre_agente = input("Ingrese el nombre del agente: ")
    if nombre_agente.isalpha():
        print(f"Bienvenido {nombre_agente} a Escape Room: La Boveda.")
        break
    print("Ingrese solo letras por favor.")


while energia>0 and tiempo>0 and cerraduras_abiertas<3 and not bloqueo_por_alarma:
    turnos += 1
    if alarma:
        estado_alarma="Activado"
    else:
        estado_alarma="Desactivado"
    print(f"\n **** ESTADO TURNO {turnos} ****")
    print(f"\n     Energia: {energia}\n     Tiempo: {tiempo}\n     Cerraduras abiertas: {cerraduras_abiertas}\n     Estado alarma: {estado_alarma}")
    while True:
        print("\nMenu de opciones (ingrese la accion a realizar): ")
        print("\n1- Forzar cerradura (costo: -20 energía, -2 tiempo).\n2- Hackear panel (costo: -10 energía, -3 tiempo).\n3- Descansar (costo: +15 energía (máx 100), -1 tiempo; si alarma ON: -10 energía extra)")
        eleccion3 = input("")
        if eleccion3.isdigit() and int(eleccion3) in range(1,4):
            break
        print("Error: ingrese una opcion correcta.")
        
    if eleccion3 == "1":
        contador_forzar_cerradura +=1
        if contador_forzar_cerradura == 3:
            alarma = True
            print("Ha intentado forzar 3 veces seguidas la cerradura. Se activo la alarma.")

        if energia < 40:
            while True:
                opcion_alarma = input("\nLa energia es menor a 40. Hay riesgo de alarma. Ingrese un numero del 1 al 3: \n")
                if opcion_alarma.isdigit() and int(opcion_alarma) in range(1,4):
                    break
                print("Error: ingrese una opcion valida.")

            if opcion_alarma=="3":
                alarma = True
                print("Se activo la alarma! ")
        
        if not alarma:
            cerraduras_abiertas +=1
            energia -= 20
            tiempo -= 2
            print("Logro abrir 1 cerradura.")
        
    elif eleccion3 == "2":
        contador_forzar_cerradura = 0
        energia -=10
        tiempo -=3

        for i in range(4):
            letra_aniadida = input("Ingrese una letra para añadir al codigo:\n")
            if letra_aniadida.isalpha() and len(letra_aniadida) ==1:
                codigo_parcial+=letra_aniadida
                print(f"Codigo: {codigo_parcial}")
            else:
                print("Error: ingrese solo UNA letra.")
        
        if len(codigo_parcial) >= 8:
            cerraduras_abiertas+=1
            print("Ha logrado abrir una cerradura!")
    
    elif eleccion3 == "3":
        contador_forzar_cerradura = 0
        if energia <100:
            if 100 - energia>15 and not alarma:
                energia+=15
                tiempo -= 1
            elif 100-energia< 15 and not alarma:
                energia +=100-energia
                tiempo -=1
            elif 100-energia>5 and alarma:
                energia +=5
                tiempo -=1
            elif 100-energia<5 and alarma:
                energia+=100-energia
                tiempo -=1
            
        else:
            print("La energia esta al maximo!")
            tiempo -=1

    if alarma == True and tiempo <=0:
        bloqueo_por_alarma = True
        print("\nSe activo el bloqueo por alarma. Fin del juego.")
    elif energia <=0:
        print("\nSe acabo la energia. Fin del juego.")
    elif tiempo<=0:
        print("\nSe acabo el tiempo. Fin del juego.")
    elif cerraduras_abiertas >=3:
        print("Felicitaciones! Gano el juego!")

