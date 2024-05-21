import datetime

# Definimos las zonas y sus temperaturas iniciales
zonas = {
    "Sala": 22.0,
    "Cocina": 22.0,
    "Dormitorio 1": 22.0,
    "Dormitorio 2": 22.0,
    "Baño": 22.0,
    "Garage": 22.0
}

# Definimos los horarios programados
horarios = {}

def agregar_zona():
    nombre_zona = input("Ingresa el nombre de la nueva zona: ")
    if nombre_zona in zonas:
        print(f"La zona '{nombre_zona}' ya existe.")
    else:
        temp_inicial = float(input(f"Ingresa la temperatura inicial para la zona '{nombre_zona}': "))
        zonas[nombre_zona] = temp_inicial
        print(f"La zona '{nombre_zona}' ha sido agregada con temperatura inicial de {temp_inicial}°C.")

def eliminar_zona():
    print("Zonas actuales:")
    for zona in zonas:
        print(f"- {zona}")

    zona_eliminar = input("Ingresa el nombre de la zona que deseas eliminar: ")
    if zona_eliminar in zonas:
        del zonas[zona_eliminar]
        print(f"La zona '{zona_eliminar}' ha sido eliminada.")

        # Eliminar los horarios programados para la zona eliminada
        horarios_eliminar = [(zona, inicio, fin) for (zona, inicio, fin) in horarios if zona == zona_eliminar]
        for horario in horarios_eliminar:
            del horarios[horario]
            print(f"Horario {horario[1]} - {horario[2]} eliminado para la zona '{zona_eliminar}'.")
    else:
        print(f"La zona '{zona_eliminar}' no existe.")

def ajustar_temperatura():
    print("Zonas actuales:")
    for zona, temp in zonas.items():
        print(f"{zona}: {temp}°C")

    zona_seleccionada = input("Ingresa el nombre de la zona que quieres ajustar: ")
    if zona_seleccionada in zonas:
        nueva_temp = float(input(f"Ingresa la nueva temperatura para la zona '{zona_seleccionada}': "))
        zonas[zona_seleccionada] = nueva_temp
        print(f"La temperatura fue actualizada para la zona '{zona_seleccionada}': {nueva_temp}°C")
    else:
        print("La zona ingresada no existe.")


def programar_horario():
    hora_actual = datetime.datetime.now().strftime("%H:%M")
    print(f"La hora actual del sistema es: {hora_actual}")

    print("Zonas actuales:")
    for zona in zonas:
        print(f"- {zona}")

    zona_seleccionada = input("Ingresa el nombre de la zona que deseas programar: ")
    if zona_seleccionada in zonas:
        horario_inicio = input("Ingresa la hora de inicio del horario (HH:MM): ")
        horario_fin = input("Ingresa la hora de finalización del horario (HH:MM): ")
        temp_deseada = float(input(f"Ingresa la temperatura deseada para la zona '{zona_seleccionada}' durante ese horario: "))
        horarios[(zona_seleccionada, horario_inicio, horario_fin)] = temp_deseada
        print("Horario programado correctamente.")
    else:
        print("La zona ingresada no existe.")

def mostrar_sensores():
    hora_actual = datetime.datetime.now().strftime("%H:%M")
    print(f"La hora actual del sistema es: {hora_actual}")

    print("Temperaturas actuales:")
    for zona, temp_deseada in zonas.items():
        temp_actual = temp_deseada  
        # Simulación de temperatura actual

        # Verificar horarios programados
        for horario, temp_programada in horarios.items():
            zona_horario, inicio, fin = horario
            if zona_horario == zona and inicio <= hora_actual < fin:
                temp_actual = temp_programada
                print(f"{zona}: {temp_actual}°C (Programado)")
                break
        else:
            print(f"{zona}: {temp_actual}°C")

def menu_principal():
    while True:
        print("\nMenú Principal")
        print("1. Agregar zona")
        print("2. Eliminar zona")
        print("3. Ajustar temperatura")
        print("4. Programar horario")
        print("5. Mostrar sensores de temperatura")
        print("6. Salir")

        opcion = input("Ingresa una opción: ")

        if opcion == "1":
            agregar_zona()
        elif opcion == "2":
            eliminar_zona()
        elif opcion == "3":
            ajustar_temperatura()
        elif opcion == "4":
            programar_horario()
        elif opcion == "5":
            mostrar_sensores()
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Iniciar el programa
menu_principal() 
