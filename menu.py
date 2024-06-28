import comandos
import os
import time
while True:
    print("""
        *************************************
        *     bienvenido al mundo libro     *
        *************************************
        [1] - Mantenedor de categorias
        [2] - Reportes
        [3] - Salir
    """)
    opcion = int(input("Ingrese una opcion: "))
    time.sleep(1)
    #os.system(cls)
    while True:
        match opcion:
            case 1:
                print("""
            *************************************
            *      Mantenedor de categorias     *
            *************************************
            [1] - Agregar categorias
            [2] - Editar Categoria
            [3] - Eliminar categoria
            [4] - Buscar categoria
            [5] - Volver
        """)
                opcion = int(input("Ingrese una opcion: "))
                match opcion:
                    case 1:
                        comandos.agregar()
                        time.sleep(2)
                        os.system("cls")
                        break
                    case 2:
                        comandos.editar()
                        time.sleep(2)
                        os.system("cls")
                        break
                    case 3:
                        comandos.eliminar()
                        time.sleep(1)
                        os.system("cls")
                        break
                    case 4:
                        comandos.buscar()
                        time.sleep(1)
                        os.system("cls")
                        break
                    case 5:
                        break

            case 2:
                comandos.reporte()
                time.sleep(1)
                os.system("cls")
                break
            case 3:
                print("Gracias por usar el sistema")
                time.sleep(1)
                os.system("cls")
                break
    if opcion==3:
        break            
