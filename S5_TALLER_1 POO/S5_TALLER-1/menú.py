from submenu import Sub_Men
import re
from usuario import Usua
from validar import Valid
import time
import os


sub = Sub_Men()
lista_SA = ["1).Usuario ","2).Administrador","3).Salir"]
alterna = ""  
while alterna != "3":
    os.system("cls")
    alterna = sub.menuprinci(lista_SA,"Módulo de Seguridad") 
    if alterna == "1":
        alterna1 = ""
        while alterna1 != "2":
            os.system("cls")
            alterna1 = sub.menu(["1) Verificación de Usuario","2) Salir"],"Opciones de Usuario")
            os.system("cls")
            print("*"*15,"Identifíquese","*"*15)
            if alterna1 == "1":
                while True:
                    correo = input("Ingrese un correo: ")
                    cor = Valid.Valid_correo(correo)
                    if cor == True:
                        print("Correo válido")
                        os.system("cls")
                        break
                    else:
                        print("Correo no válido")
                        os.system("cls")
                    
                
                while True:
                    cedul = input("Ingresar número de cédula: ")
                    ced = Valid.Valid_ced(cedul)
                    if  ced == True:
                        if len(cedul) == 10:
                            print("-"*2,"Cédula Correcta","-"*2)  
                            time.sleep(0.6) 
                            os.system("cls")
                            break

                while alterna1 != "5":
                
                    alterna1 = sub.menu(["1).Ingresar datos", "2).Mostrar datos", "3).Actualizar datos","4).Salir"],"Opciones de Usuario")
                            
                    if alterna1 == "1": 
                            os.system("cls")
                            nombre = input("Ingrese su nombre: ")
                            apellido = input("Ingrese su primer apellido: ")
                            dirección = input("Ingrese su dirección: ")
                                
                            metod = Usua(nombre, apellido, cedul, dirección)
                            usuario = metod.registro1()
                            Usua.usuario.append(usuario)
                            os.system("cls")

                            input("Presione una tecla para continuar...")
                            time.sleep(0.5)
                            os.system("cls")
        
                        

                    elif alterna1 == "2": 
                        os.system("cls")
                        print("*"*70)
                        print(" "*5,"Nombre"," "*8,"Apellido"," "*7,"Cédula"," "*9,"Dirección")
                        for metod in Usua.usuario:
                            nom = metod["Nombre"]
                            ape = metod ["Apellido"]
                            ced = metod ["Cédula"]
                            dir = metod["Dirección"]

                            print(" "*6,nom," "*10,ape," "*(11-len(nom)),ced," "*(19-len(ced)),dir)
                        
                        print("*"*70)
                        input("Presione una tecla para continuar...")
                        os.system("cls")
        
                       

                    elif alterna1 == "3": 
                        os.system("cls")
                        for metod in Usua.usuario:
                            metod["Nombre"] = "ROBIN"
                            print(metod)

                         
                    
                    elif alterna1 == "4":
                        pass
                    
                        

    if alterna == "2":
        alterna1 = ""
        while alterna1 != "2":
            os.system("cls")
            alterna1 = sub.menu(["1) Verificación de Administrador","2) Salir"],"Opciones de Administración")
            os.system("cls")
            print("*"*15,"Identifíquese","*"*15)
            if alterna1 == "1":
                while True:
                    correo = input("Ingrese un correo: ")
                    cor = Valid.Validarcorreo(correo)
                    if cor == True:
                        print("Correo válido")
                        os.system("cls")
                        break
                    else:
                        print("Correo no válido")
                        os.system("cls")
                    
                
                
                while True:
                    cedul = input("Ingresar clave: ")
                    ced = Valid.Validarced(cedul)
                    if  ced == True:
                        if len(cedul) == 10:
                            print("-"*2,"Clave Correcta","-"*2)  
                            time.sleep(0.6) 
                            os.system("cls")
                            break


                while alterna1 != "5":
                
                    alterna1 = sub.menu(["1).Ingresar datos", "2).Mostrar datos", "3).Actualizar datos", "4).Eliminar datos","5).Salir"],"Opciones de Administrador")
                            
                    if alterna1 == "1":
                            os.system("cls")
                            nombre = input("Ingrese su nombre: ")
                            apellido = input("Ingrese su primer apellido: ")
                            dirección = input("Ingrese su dirección: ")
                                
                            metod = Usua(nombre,apellido, cedul, dirección)
                            usuario = metod.registro1()
                            Usua.usuario.append(usuario)
                            os.system("cls")

                            input("Presione una tecla para continuar...")
                            time.sleep(0.5)
                            os.system("cls")
        


                    elif alterna1 == "2":
                        os.system("cls")
                        print("*"*70)
                        print(" "*5,"Nombre"," "*8,"Apellido"," "*7,"Cédula"," "*9,"Dirección")
                        for metod in Usua.usuario:
                            nom = metod["Nombre"]
                            ape = metod ["Apellido"]
                            ced = metod ["Cédula"]
                            dir = metod["Dirección"]

                            print(" "*6,nom," "*8,ape," "*(11-len(nom)),ced," "*(19-len(ced)),dir)
                        
                        
                        print("*"*70)
                        input("Presione una tecla para continuar...")
        
                       

                    elif alterna1 == "3":
                        pass
                        


                    elif alterna1 == "4":
                        pass
                    elif alterna1 == "5":
                        print("Salir del ")





    if alterna == "3":
        os.system("cls")
        print("Saliendo del módulo...")
        time.sleep(1)        
        os.system("cls")           
                        


