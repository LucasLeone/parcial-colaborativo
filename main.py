
# Vector de clientes: id (int), permite_entrar (boolean), saldo (float), nombre (str), user (str), clave (str), tarjeta_banco (str)
cliente1 = [1, True, 30000, 'Pepe', 'pepito', 'pepe123', 'BANMAS']
cliente2 = [2, True, 10000, 'Juan', 'juancito', 'juancito123', 'BBVA']
cliente3 = [3, True, 40000, 'Manolo', 'manolito', 'manolito00', 'BANMAS']
cliente4 = [4, True, 25000, 'Julia', 'julia01','juli432', 'HIPOTECARIO']
cliente5 = [5, True, 15000, 'Mario', 'marito','mario123', 'BANMAS']

# Intentos por cliente
tries_cliente1 = 0
tries_cliente2 = 0
tries_cliente3 = 0
tries_cliente4 = 0
tries_cliente5 = 0

# Constante de comisión
COMISION = 9.5

# Variables de billetes
billetes_50 = int(input('Cuantos billetes de $50 se cargarán? '))
billetes_100 = int(input('Cuantos billetes de $100 se cargarán? '))
billetes_200 = int(input('Cuantos billetes de $200 se cargarán? '))
billetes_500 = int(input('Cuantos billetes de $500 se cargarán? '))
total_en_cajero = (billetes_50 * 50) + (billetes_100 * 100) + (billetes_200 * 200) + (billetes_500 * 500)

while True:
    #Entrada
    print('''
        ---- Bienvenido al banco BANMAS ----
        Inicie sesión para poder continuar:
    ''')
    
    user_name = input('Ingrese su nombre de usuario: ')
    #Proceso
    if user_name == cliente1[4]:
        if cliente1[1] == False:
            print('No puede usar el cajero')
            break
    elif user_name == cliente2[4]:
        if cliente2[1] == False:
            print('No puede usar el cajero')
            break
    elif user_name == cliente3[4]:
        if cliente3[1] == False:
            print('No puede usar el cajero')
            break
    elif user_name == cliente4[4]:
        if cliente4[1] == False:
            print('No puede usar el cajero')
            break
    elif user_name == cliente5[4]:
        if cliente5[1] == False:
            print('No puede usar el cajero')
            break
    else:
        print('Usuario incorrecto!')
        break

    user_id = 0
    
    while True:
        if user_id != 0:
            break

        passwd = input('Ingrese su clave: ')

        # Evalúo si la pass es correcta
        if passwd == cliente1[5]:
            user_id = 1
            print(f'Bienvenido {cliente1[3]}')
        elif passwd == cliente2[5]:
            user_id = 2
            print(f'Bienvenido {cliente2[3]}')
        elif passwd == cliente3[5]:
            user_id = 3
            print(f'Bienvenido {cliente3[3]}')
        elif passwd == cliente4[5]:
            user_id = 4
            print(f'Bienvenido {cliente4[3]}')
        elif passwd == cliente5[5]:
            user_id = 5
            print(f'Bienvenido {cliente5[3]}')
        else:
            # Si la pass no es correcta, sumo la cantidad de intentos realizados
            print('Clave incorrecta!')
            if user_name == cliente1[4]:
                tries_cliente1 += 1
            elif user_name == cliente2[4]:
                tries_cliente2 += 1
            elif user_name == cliente3[4]:
                tries_cliente3 += 1
            elif user_name == cliente4[4]:
                tries_cliente4 += 1
            elif user_name == cliente5[4]:
                tries_cliente5 += 1

        
        # Si la cantidad de intentos es igual o mayor a 3, deshabilito al cliente cambiando la flag de True a False
        if user_name == cliente1[4]:
            if tries_cliente1 >= 3:
                cliente1[1] = False
                break
        elif user_name == cliente2[4]:
            if tries_cliente3 >= 3:
                cliente3[1] = False
                break
        elif user_name == cliente3[4]:
            if tries_cliente3 >= 3:
                cliente3[1] = False
                break
        elif user_name == cliente4[4]:
            if tries_cliente4 >= 3:
                cliente4[1] = False
                break
        elif user_name == cliente5[4]:
            if tries_cliente5 >= 3:
                cliente5[1] = False
                break
            
    if user_id != 0:
        while True:
            print('''
                MENU DE OPCIONES:
                [1] Ver saldo
                [2] Deposito
                [3] Retiro
                [4] Salir  
            ''')
            option = int(input('Ingrese la opción: '))
            
            # Si el usuario ingresa la opción 1, muestro el saldo respectivo. En el caso de que su tarjeta no sea
            # del banco BANMAS, le descuento $9.50 de comisión.
            if option == 1:
                if user_id == 1:
                    if cliente1[6] != 'BANMAS': 
                        cliente1[2] -= COMISION
                    print(f'Su saldo es: ${cliente1[2]}')
                elif user_id == 2:
                    if cliente2[6] != 'BANMAS':
                        cliente2[2] -= COMISION
                    print(f'Su saldo es: ${cliente2[2]}')
                elif user_id == 3:
                    if cliente3[6] != 'BANMAS':
                        cliente3[2] -= COMISION
                    print(f'Su saldo es: ${cliente3[2]}')
                elif user_id == 4:
                    if cliente4[6] != 'BANMAS':
                        cliente4[2] -= COMISION
                    print(f'Su saldo es: ${cliente4[2]}')
                elif user_id == 5:
                    if cliente5[6] != 'BANMAS':
                        cliente5[2] -= COMISION
                    print(f'Su saldo es: ${cliente5[2]}')
            # Si el usuario ingresa la opción 2, le solicito que ingrese el saldo a depositar. Este saldo solamente podrá 
            # depositarse si es múltiplo de 50. En el caso de que su tarjeta no sea del banco BANMAS, le descuento $9.50 de comisión.
            elif option == 2:
                while True:
                    deposito = int(input('Ingrese el monto a depositar: $'))
                    if deposito % 50 != 0:
                        print('Solo se pueden depositar montos múltiplos de 50')
                        break
                    if user_id == 1:
                        cliente1[2] += deposito
                        if cliente1[6] != 'BANMAS': 
                            cliente1[2] -= COMISION
                        print('Deposito realizado!')
                    elif user_id == 2:
                        cliente2[2] += deposito
                        if cliente2[6] != 'BANMAS':
                            cliente2[2] -= COMISION
                        print('Deposito realizado!')
                    elif user_id == 3:
                        cliente3[2] += deposito
                        if cliente3[6] != 'BANMAS':
                            cliente3[2] -= COMISION
                        print('Deposito realizado!')
                    elif user_id == 4:
                        cliente4[2] += deposito
                        if cliente4[6] != 'BANMAS':
                            cliente4[2] -= COMISION
                        print('Deposito realizado!')
                    elif user_id == 5:
                        cliente5[2] += deposito
                        if cliente5[6] != 'BANMAS':
                            cliente5[2] -= COMISION
                        print('Deposito realizado!')
                    break
            elif option == 3:
                while True:
                    retiro = int(input('Ingrese el monto a retiro: $'))

                    if user_id == 1:
                        if retiro > cliente1[2]:
                            print('El dinero requerido excede lo que tiene en su cuenta!')
                            break
                    elif user_id == 2:
                        if retiro > cliente2[2]:
                            print('El dinero requerido excede el monto de su cuenta!')
                            break
                    elif user_id == 3:
                        if retiro > cliente3[2]:
                            print('El dinero requerido excede el monto de su cuenta!')
                            break
                    elif user_id == 4:
                        if retiro > cliente4[2]:
                            print('El dinero requerido excede el monto de su cuenta!')
                            break
                    elif user_id == 5:
                        if retiro > cliente5[2]:
                            print('El dinero requerido excede el monto de su cuenta!')
                            break
                    if retiro > total_en_cajero:
                        print('No hay tanto dinero disponible en el cajero!')
                    if retiro > 5000:
                        print('No se puede retirar mas de $5000!')
                        break
                    if retiro % 50 != 0:
                        print('Solo se pueden retirar montos múltiplos de 50')
                        break
                    if user_id == 1:
                        cliente1[2] -= deposito
                        if cliente1[6] != 'BANMAS': 
                            cliente1[2] -= COMISION
                        print('Deposito realizado!')
                    elif user_id == 2:
                        cliente2[2] -= deposito
                        if cliente2[6] != 'BANMAS':
                            cliente2[2] -= COMISION
                        print('Deposito realizado!')
                    elif user_id == 3:
                        cliente3[2] -= deposito
                        if cliente3[6] != 'BANMAS':
                            cliente3[2] -= COMISION
                        print('Deposito realizado!')
                    elif user_id == 4:
                        cliente4[2] -= deposito
                        if cliente4[6] != 'BANMAS':
                            cliente4[2] -= COMISION
                        print('Deposito realizado!')
                    elif user_id == 5:
                        cliente5[2] -= deposito
                        if cliente5[6] != 'BANMAS':
                            cliente5[2] -= COMISION
                        print('Deposito realizado!')
                    break
            elif option == 4:
                print('Saludos!')
                break
            else:
                print('Opción incorrecta!')