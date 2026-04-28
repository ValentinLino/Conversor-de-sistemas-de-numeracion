'''

el objetivo de este programa es realizar el pasaje entre los sistemas de numeracion binario, octal, decimal y hexadecimal
recibe una entrada del usuario e interpreta a que sistema de numeracion corresponde, luego realiza la conversion a los otros sistemas de numeracion

'''

import msvcrt

#funcion para obtener el numero ingresado por el usuario
def get_user_input():
    input_string_var=input("Ingrese un número: ")
    input_string_var=input_string_var.strip().upper()
    return input_string_var

#funcion para detectar el sistema de numeracion del numero ingresado por el usuario
def detect_numeral_system(input_string_var):
    #binary check
    if input_string_var.startswith("0b") or input_string_var.startswith("0B"):
        return print(f"binario:{type(input_string_var)}")
    elif all(c in '01' for c in input_string_var):
        return print(f"binario:{type(input_string_var)}")
    #octal check
    elif input_string_var.startswith("0o") or input_string_var.startswith("0O"):
        return "octal"
    elif all(c in '01234567' for c in input_string_var):
        return "octal"
    #hexadecimal check
    elif input_string_var.startswith("0x") or input_string_var.startswith("0X"):
        return "hexadecimal"
    elif all(c in '0123456789ABCDEF' for c in input_string_var):
        return print(f"hexadecimal:{type(input_string_var)}")
    #decimal check
def convert_string_to_correct_type(input_string_var):
        
        return int(input_string_var)
        
loop=0

    

while loop<5:
    print("Presione ESC en cualquier momento para salir...")
    if msvcrt.getch().lower() == b'\x1b':  # ESC key
        break
    get_user_input_var=get_user_input()
    numeral_system_var=detect_numeral_system(get_user_input_var)
    #print(f"El número ingresado es del sistema de numeración: {numeral_system_var}")
    loop+=1
    