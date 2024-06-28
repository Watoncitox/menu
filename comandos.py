import json
import os

def buscar():
    with open("biblioteca.json",mode="r") as lecturajson:
        leerjson=json.load(lecturajson)
    """print ("CategoriaID")
    id=input("ingrese el id de la categoria:")"""
    print("ID / Nombre")
    for i in leerjson["Categoria"]:
        #if i["CategoriaID"]==id:
        print(i["CategoriaID"],i["Nombre"])

def agregar():
    with open("biblioteca.json",mode="r") as lecturajson:
        leerjson=json.load(lecturajson)
    nombre=input("Ingrese el nombre de la nueva categoria: ")
    nuevacategoria= {
        "CategoriaID":len(leerjson["Categoria"])+1,
        "Nombre": nombre
    }
    leerjson["Categoria"].append(nuevacategoria)
    print("Se a agregado correctamente")
    with open("biblioteca.json",mode="w") as escriturajson:
        json.dump(leerjson, escriturajson, indent=4)

def editar():
    with open("biblioteca.json",mode="r") as lecturajson:
        leerjson=json.load(lecturajson)
    id=input("ingrese el id de la categoria:")
    for i in leerjson["Categoria"],:
        if i["CategoriaID"]==id:
            print(i["Nombre"])
            nombre=input("ingrese el nuevo Nombre:")
            i["Nombre"]=nombre
    with open("biblioteca.json",mode="w") as escriturajson:
        json.dump(leerjson, escriturajson, indent=4)

def eliminar():
    with open("biblioteca.json",mode="r") as lecturajson:
        leerjson=json.load(lecturajson)
    print ("id")
    id=input("ingrese el id de la categoria:")
    for i in leerjson["Categoria"]:
        if i["CategoriaID"]==id:
            print(i["Nombre"])
            leerjson.remove(i)
    with open("biblioteca.json",mode="w") as escriturajson:
        json.dump(leerjson, escriturajson, indent=4)

def reporte():
    with open("Reportes_biblioteca_mundo_libro.json", mode="r") as lecturajson:
        leerjson=json.load(lecturajson)
        print("""
    *****************************************************
    *  Libro                Cantidad de veces prestado  *
    *****************************************************
""")
    for i in leerjson["Reportes"]:
        print(i["Nombre"],i["vecesprestado"])
        

#buscar()
#agregar()
        
#eliminar()
#editar()
        
#reporte()