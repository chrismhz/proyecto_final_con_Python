import os
os.system('cls')
print("")
print(" _________________________________________________________________")
print("| 🏥 Bienvenidos al sistema de historias clinicas del hospital 🏥 |")
print("|_________________________________________________________________|")
print("")

######################
# VARIABLES GLOBALES #
######################

running = True
#database = list()
database = [{'nombre':'Juan', 'historia':'resfrio'},{'nombre':'Pedro', 'historia':'Dolor de muela'}]

######################
#      FUNCIONES     #
######################

def show_menu():
    print("")
    print("")
    print("\t\t🔴        1 - Cargar paciente")
    print("\t\t🔴        2 - Buscar paciente")
    print("\t\t🔴        3 - Listar pacientes")
    print("\t\t🔴        4 - Salir")
    print("")
    res = input("INGRESE UNA OPCION > ")
    os.system('cls')
    return res

def response_validate(response):
    validated = False
    num_res = 0


    if response.isdigit():
        num_res = int(response)
        if num_res >= 1 and num_res <= 4:
            msg = "esta en rango"
            validated = True
        else:
            msg = "fuera de rango"
    else:
        msg = "Entrada incorrecta"

    return validated,num_res,msg

######################
#   LOOP PRINCIPAL   #
######################

while running:
    response = show_menu()
    validated,num_res,msg =  response_validate(response)
    if validated:
        if num_res == 1:
            name = input("Ingrese el nombre del paciente > ")
            history = input("Ingrese la historia clinca del paciente > ")
            paciente = {"nombre":name , "historia":history}
            database.append(paciente)
            print(database)

        elif num_res == 2:
            name = input("Ingrese el nombre del paciente > ")

            finded = False
            for x in range(len(database)):
                if database[x]["nombre"].lower() == name.lower():
                    print("")
                    print("Paciente encontrado!")
                    print("PACIENTE ENCONTRADO | H. CLINICA > ", database[x]["historia"])
                    print("")
                else:
                    finded = True

            if not finded: 
                print("Paciente no encontrado :( ")

        elif num_res == 3:
            print("")
            print(" ________________________________________")
            print("| Listado de Pacientes                   |")
            print("|________________________________________|")
            print("")
            for x in range(len(database)):
                print("Nombre >  ".ljust(10), database[x]["nombre"],"\tHistoria C > ".ljust(10),database[x]["historia"])

            print ("FIN DE LISTA")

        else:
            running=False
    else:
        print(msg)
    
print("")
print("Aplicacion Finalizada")
print("")

