# este ecript pone ip a las maquias y el ultimo ip k puso lo guarda en un archivo
import os
def cls():
    os.system('cls')
def menu(mensaje):
    print(f"•÷±‡±( {mensaje} )±‡±÷ ")

    
print( os.listdir('.'))
os.system('color a')
while 1:
    # cls()
    menu("Administra tus puertos")
    print("1. Ver puertos abiertos (netstat)")
    print("S. salir ")
    opcion = input()
    if opcion=="1":
        # cls()
        print( os.system('NETSTAT -ANO'))
        menu("inserte el numero PID para poder eliminar proceso")
        menu("0 para salir")
        numeroProceso = input()
        if numeroProceso=="0":
            break
            print("saliendo del programa...")
        else:
            print(os.system('TASKKILL /PID '+numeroProceso+' /F'))
            print("Se cerro con exito...")
    else:
        print("opcion 0")
        break




# os.system('echo hola desde el cmd')
# os.system('NETSTAT -ANO')
# os.system('TASKKILL /PID '+)

# archivoIp = open("ip.txt") 
# archivoIp.write('hola')