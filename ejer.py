def buscval (list,target):
    for item in list:
        if item == target:
            return item
    return None
def quick_sort_Nombre(lista):
    if len(lista) <= 1:
        return lista

    pivote = lista[0]
    menores = [x for x in lista[1:] if x[1]["Nombre"] < pivote[1]["Nombre"]]
    iguales = [x for x in lista if x[1]["Nombre"] == pivote[1]["Nombre"]]
    mayores = [x for x in lista[1:] if x[1]["Nombre"] > pivote[1]["Nombre"]]

    return quick_sort_Nombre(menores) + iguales + quick_sort_Nombre(mayores)
def ingresar_Participante(lista={}):
        dorsnum=int(input("ingrese numero de ID para el participante: "))
        name=input("ingrese nombre del participante: ")
        age=int(input("ingrese la edad del participante: "))
        if age > 10 and age < 101:
            if age >=10 and age <20:
                categ="Juvenil"
            elif age >=20 and age <50:
                categ="Adulto"
            elif age >=50:
                categ="Master"

            lista [dorsnum] = {
                "Nombre": name,
                "Edad": age,
                "Categ": categ
            }
        else:
            print("Ingreso invalido, intente nuevamente")
participantes={}
ingresar_Participante(participantes)
ingresar_Participante(participantes)
ingresar_Participante(participantes)
list= list(participantes.items())
result= quick_sort_Nombre(list)
for name, value in result:
    print(f"{value['Nombre']}, {value['Edad']}, {value['Categ']}")