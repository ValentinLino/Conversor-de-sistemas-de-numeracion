'''

el objetivo de este programa es realizar el pasaje entre los sistemas de numeracion binario, octal, decimal y hexadecimal
recibe una entrada del usuario e interpreta a que sistema de numeracion corresponde, luego realiza la conversion a los otros sistemas de numeracion

'''

import msvcrt

#funcion para obtener el numero ingresado por el usuario
def get_user_input():
    print("para numeros binarios por favor usar el prefijo 0b, para octales el prefijo 0o y para hexadecimales el prefijo 0x")
    input_string_var=input("Ingrese un número: ")
    input_string_var=input_string_var.strip()
    return input_string_var
    
#funcion para detectar el sistema de numeracion del numero ingresado por el usuario y transformar al tipo de dato correspondiente 
def detect_numeral_system(input_string_var):
    #binary check
    if input_string_var.startswith("0b") or input_string_var.startswith("0B"):
        input_string_var=input_string_var[2:]  
        output_var=int(input_string_var, 2)  
        return output_var
    
    #octal check
    elif input_string_var.startswith("0o") or input_string_var.startswith("0O"):
        input_string_var=input_string_var[2:]  
        output_var=int(input_string_var, 8)  
        return output_var
    
    #hexadecimal check
    elif input_string_var.startswith("0x") or input_string_var.startswith("0X"):
        input_string_var=input_string_var[2:]  
        output_var=int(input_string_var, 16)  
        return output_var
    
    #decimal check
    elif input_string_var[0] != 0:
        output_var=int(input_string_var)  
        return output_var

def convert_to_other_systems(output_var):
    binary_var=bin(output_var)
    octal_var=oct(output_var)
    hexadecimal_var=hex(output_var)
    print(f"El número ingresado es del sistema de numeración: {type(output_var)}")
    print(f"En binario: {binary_var}")
    print(f"En octal: {octal_var}")
    print(f"En hexadecimal: {hexadecimal_var}")        
    
loop=True

    

while loop == True:
    print("Presione ESC en cualquier momento para salir...")
    get_user_input_var=get_user_input()
    numeral_system_var=detect_numeral_system(get_user_input_var)
    convert_to_other_systems(numeral_system_var)
    print("\npresione cualquier tecla para continuar...")
    if msvcrt.getch().lower() == b'\x1b':  # ESC key
        loop=False
        break


    
    