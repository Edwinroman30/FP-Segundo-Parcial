class Libreta_contacto:
    
    def __init__(self):
        #self.__nombre
        #self.__telefono
        #self.__mail
        #self.direccion
        
        self.__list_contact = []
    
    #!
    def Anadir_contacto(self):
        print(' ')        
        p_nombre = input('Ingrese el nombre del contacto que desea ingresar: ')
        p__telefono = input('Ingrese el telefono del contacto que desea ingresar: ')
        p__mail = input('Ingrese el e-mail del contacto que desea ingresar: ')
        p_direccion = input('Ingrese la direccion del contacto que desea ingresar: ')

        self.__list_contact.append({'Nombre': p_nombre,'Telefono':p__telefono,'Mail':p__mail,'Direccion':p_direccion})
        print('\n')
        
    #! 
    def Mostrar_contacto(self):
        print(' ')
        print('Lista de Contacto:')
        for indice,contacto in enumerate(self.__list_contact):
            print('{}) {}, de telefono: {} y e-mail: {}, reside en: {}'.format(indice,contacto['Nombre'],contacto['Telefono'],contacto['Mail'],contacto['Direccion']))
        print('\n')    
    #!
    def Buscar_contacto(self):
        #print(' ')
        tosearch = input('Por favor, ingrese nombre del contacto que desea buscar: ')
        tosearch = tosearch.lower()
        print('\n')
        print('Coinsidencias en la BD: ')
        
        for contacto in self.__list_contact:
            
            if (contacto.get('Nombre').lower().find(tosearch)) > -1:
                print('{}, de telefono: {} y e-mail: {}, residen en: {}'.format(contacto['Nombre'],contacto['Telefono'],contacto['Mail'],contacto['Direccion']))
        print('\n')        
    
    #!
    def Modificar_data(self):
        print(' ')
        id_telefono = input('Ingrese el telefono del contacto que desea modificar:')
        
        opcion = int(input('Seleccione lo que desea modificar: \n(1)Telefono (2)Mail (3)Direccion: '))
        print('\n')
        
        if(opcion == 1):
            for contacto in self.__list_contact:
                
                if (contacto.get('Telefono') == id_telefono):
                    contacto['Telefono'] = input('Introduzca el nuevo valor de telefono: ')
                    print('Cambio registrado sactisfactoriamente :) !')
                    break
                else:
                    print('Lo sentimos pero el numero que busca, no se encuentra en el registro.')
                    break
                
        elif(opcion == 2):
           for contacto in self.__list_contact:
                
                if (contacto.get('Telefono') == id_telefono):
                    contacto['Mail'] = input('Introduzca el nuevo valor del e-Mail: ')
                    print('Cambio registrado sactisfactoriamente :) !')
                    break
                else:
                    print('Lo sentimos pero el numero que busca, no se encuentra en el registro.')
                    break
                
                  
        elif(opcion == 3):
              for contacto in self.__list_contact:
                    
                if (contacto.get('Telefono') == id_telefono):
                    contacto['Direccion'] = input('Introduzca el nuevo valor de la Direccion: ')
                    print('Cambio registrado sactisfactoriamente :) !')
                    break
                else:
                    print('Lo sentimos pero el numero que busca, no se encuentra en el registro.')
                    break
                
       
        else:
            print('Lo sentimos pero usted se ha salido del rango establecido en el MENU.')
        print('\n')    
            

import os

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
             
                     
Libreta = Libreta_contacto()
menu_op = 0

try:
    #!Remember WHILE LOOP
    while menu_op != 6:
       
        #Añadir un menu.
        
        print('Bienvenido a tu Agenda de Contacto:'.title())
        print('1) Agregar contacto a la agenda.'.title())
        print('2) Lista de contacto.'.title())
        print('3) Buscar contacto por nombre.'.title())
        print('4) Modificar de telefono, e-mail o direccion.'.title())
        print('5) Limpiar consola.'.title())
        print('6) Fin de programa.'.title())
        print('\n')
        
        menu_op = int(input('Ingrese su opcion: '))
       
        if(menu_op == 1):
            Libreta.Anadir_contacto()
        elif(menu_op == 2):
            Libreta.Mostrar_contacto()
        elif (menu_op == 3):
            Libreta.Buscar_contacto()
        elif (menu_op == 4):
            Libreta.Modificar_data()
        elif((menu_op == 5)):
            clear()
        elif((menu_op == 6)):
            break
         
except:
    print('Usted a ingresado un valor fuera de rango o NO numerico.')


#Edwin Alberto Roman Seberino
#2020-10233