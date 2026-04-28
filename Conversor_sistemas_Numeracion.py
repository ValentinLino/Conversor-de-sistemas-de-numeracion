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
        input_string_var=input_string_var[2:]  # Remove the "0b" prefix
        output_var=int(input_string_var, 2)  # Convert binary string to integer
        return output_var
    
    #octal check
    elif input_string_var.startswith("0o") or input_string_var.startswith("0O"):
        input_string_var=input_string_var[2:]  # Remove the "0o" prefix
        output_var=int(input_string_var, 8)  # Convert octal string to integer
        return output_var
    
    #hexadecimal check
    elif input_string_var.startswith("0x") or input_string_var.startswith("0X"):
        input_string_var=input_string_var[2:]  # Remove the "0x" prefix
        output_var=int(input_string_var, 16)  # Convert hexadecimal string to integer
        return output_var
    
    #decimal check
    elif input_string_var[0] != 0:
        output_var=int(input_string_var)  # Convert decimal string to integer
        return "decimal"
        
loop=0

    

while loop<5:
    print("Presione ESC en cualquier momento para salir...")
    if msvcrt.getch().lower() == b'\x1b':  # ESC key
        break
    get_user_input_var=get_user_input()
    numeral_system_var=detect_numeral_system(get_user_input_var)
    #print(f"El número ingresado es del sistema de numeración: {numeral_system_var}")
    loop+=1
    