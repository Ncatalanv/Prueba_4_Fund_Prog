datos = {
    "fortificados": [
                        {
                            "nombre": "nicolas",
                            "tipo_entrada": "G",
                            "codigo": "Ent123"
                        }
                    ],

    "iluminados": [
                        {
                            "nombre": "ignacio",
                            "tipo_entrada": "CV",
                            "codigo": "ENT1"
                        },
                        {
                            "nombre": "sofia",
                            "tipo_entrada": "PALCO",
                            "codigo": "ent222"
                        }
                    ]
            }



def validar_texto(mensaje:str):
    while True:
        texto = input(mensaje)

        if len(texto) == 0:
            print("No puede estar vacío.")
            continue
        return texto

def validar_numero_entero_positivo(mensaje:str):
    while True:
        try:
            numero = int(input(mensaje))

            if numero < 0:
                print("Número debe ser mayor a 0.")
                continue
            return numero
        except ValueError:
            print("Error, debe ser un número entero.")
            continue

def validar_texto_letra(codigo:str):
    letras = "abcdefghijklmnñopqrstuvwxyz"

    for i in codigo:
        for j in letras:
            if i == j:
                return True
    return False
    
def validar_texto_numero(codigo:str):
    numeros = "0123456789"

    for i in codigo:
        for j in numeros:
            if i == j:
                return True
    return False


def entrada_fortificados():
    while True:
        entrada = input("Ingrese tipo de entrada General o Vip (G / V) ")
        if entrada.lower() == "g" or entrada.lower() == "v":
            return entrada.upper()
        print("No existe este tipo de entrada.")
        continue

def entrada_iluminados():
    while True:
        entrada = input("Ingrese tipo de entrada (CV o Palco): ")
        if entrada.lower() == "cv" or entrada.lower() == "palco":
            return entrada.upper()
        print("No existe este tipo de entrada.")
        continue    

def validar_codigo_fortificados(codigo:str):
    """Válida que tenga 1 letra mayúscula"""
    letras = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

    for i in codigo:
        for j in letras:
            if i == j:
                return True
    return False

def validar_codigo_iluminados(codigo:str):
    """Válida que tenga 3 letras mayúsculas"""
    
    conteo = 0
    letras = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

    for i in codigo:
        for j in letras:
            if i == j:
                conteo += 1
    
    if conteo >= 3:
        return True
    else:
        return False



def validar_repetido_iluminados(nombre:str):
    for i in datos["iluminados"]:
        if i['nombre'] == nombre:
            print("Este nombre ya está en uso.")
            return False
    return nombre


def menu():
    stock_fortificados = 499
    stock_iluminados = 498
    while True:
        print("TOTEM AUTOSERVICIO CONCIERTOS ROCK AND CHILE")
        print("1.- Comprar entrada a 'los Fortificados'.")
        print("2.- Comprar entrada a 'los Iluminados'.")
        print("3.- Stock de entradas para ambos conciertos.")
        print("4.- Salir.")
        opc = validar_numero_entero_positivo("Ingrese una opción 1 - 4: ")

        if opc == 1:
            print(" --- Comprar entrada para 'Los Fortificados'")
            nombre_agregar = validar_texto("Ingrese nombre del comprador: ")

            tipo_entrada_agregar = entrada_fortificados()

            while True:
                codigo_agregar = validar_texto("Ingrese código de confirmación: ")

                if validar_texto_letra(codigo_agregar.lower()) == False:
                    print("El código debe contener una letra.")
                    continue
                elif validar_texto_numero(codigo_agregar) == False:
                    print("El código debe contener un número.")
                    continue
                elif validar_codigo_fortificados(codigo_agregar) == False:
                    print("Debe contener al menos una letra mayúscula.")
                    continue
                elif len(codigo_agregar) < 6:
                    print("Debe ser mayor o igual a 6 carácteres.")
                    continue
                break


            agregar_entrada_fortificados =      {
                                                    "nombre": nombre_agregar,
                                                    "tipo_entrada": tipo_entrada_agregar,
                                                    "codigo": codigo_agregar
                                                }

            
            datos["fortificados"].append(agregar_entrada_fortificados)
            stock_fortificados -= 1
            print("Entrada registrada con éxito para 'Los Fortificados'.")

        elif opc == 2:
            print("Comprar entrada para 'Los Iluminados'.")
            while True:
                nombre_validar = validar_texto("Ingrese nombre del comprador: ")
                nombre_agregar = validar_repetido_iluminados(nombre_validar)

                if nombre_agregar == False:
                    continue
                break
            
            tipo_entrada_agregar = entrada_iluminados()

            while True:
                codigo_agregar = validar_texto("Ingrese código de confirmación: ")

                if validar_texto_letra(codigo_agregar.lower()) == False:
                    print("Debe contener al menos una letra.")
                    continue
                elif validar_codigo_iluminados(codigo_agregar) == False:
                    print("Debe contener al menos 3 letras mayúsculas.")
                    continue
                elif validar_texto_numero(codigo_agregar) == False:
                    print("Debe contener al menos un número.")
                    continue
                elif len(codigo_agregar) < 5:
                    print("El código debe ser mayor a 5 carácteres.")
                    continue
                break

            agregar_entrada_iluminados =        {
                                                    "nombre": nombre_agregar,
                                                    "tipo_entrada": tipo_entrada_agregar,
                                                    "codigo": codigo_agregar
                                                }

            datos["iluminados"].append(agregar_entrada_iluminados)
            stock_iluminados -= 1
            print("Entrada registrada con éxito para 'Los Iluminados'.")
        elif opc == 3:
            print("--- Stock de entradas ---")
            print(f"Entradas disponibles para 'Los Fortificados': {stock_fortificados} ")
            print(f"Entradas disponibles para 'Los Iluminados': {stock_iluminados}")
        
        elif opc == 4:
            print("Saliendo del Totem Autoservicio...")
            break
        else:
            print("Opción no válida.")
            continue



menu()

#print(validar_repetido_iluminados("ignacio5"))
#print(validar_codigo_iluminados("3432D432"))

#print(entrada_fortificados())
#print(validar_texto_numero("fewqew4qe"))
#menu()
#print(validar_texto("Ingrese nombre: "))
#print(validar_numero_entero_positivo("hola"))