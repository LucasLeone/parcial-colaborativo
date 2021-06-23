
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

# Variables de ticket final
veces_que_se_uso = 0
veces_bloqueado = 0
importe_total_retirado = 0
importe_total_depositado = 0
importe_comisiones = 0
billetes_50_entregados = 0
billetes_100_entregados = 0
billetes_200_entregados = 0
billetes_500_entregados = 0
importe_mayor_retiro = 0
importe_mayor_deposito = 0

while True:
    #Entrada
    print('''
        ---- Bienvenido al banco BANMAS ----
        Inicie sesión para poder continuar:
    ''')

    user_name = input('Ingrese su nombre de usuario (cualquier nombre incorrecto finaliza el programa): ')
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
                        total_en_cajero += deposito
                        if cliente1[6] != 'BANMAS': 
                            cliente1[2] -= COMISION
                            importe_comisiones += COMISION
                        print('Deposito realizado!')
                    elif user_id == 2:
                        cliente2[2] += deposito
                        total_en_cajero += deposito
                        if cliente2[6] != 'BANMAS':
                            cliente2[2] -= COMISION
                            importe_comisiones += COMISION
                        print('Deposito realizado!')
                    elif user_id == 3:
                        cliente3[2] += deposito
                        total_en_cajero += deposito
                        if cliente3[6] != 'BANMAS':
                            cliente3[2] -= COMISION
                            importe_comisiones += COMISION
                        print('Deposito realizado!')
                    elif user_id == 4:
                        cliente4[2] += deposito
                        total_en_cajero += deposito
                        if cliente4[6] != 'BANMAS':
                            cliente4[2] -= COMISION
                            importe_comisiones += COMISION
                        print('Deposito realizado!')
                    elif user_id == 5:
                        cliente5[2] += deposito
                        total_en_cajero += deposito
                        if cliente5[6] != 'BANMAS':
                            cliente5[2] -= COMISION
                            importe_comisiones += COMISION
                        print('Deposito realizado!')
                    
                    importe_total_depositado += deposito

                    if importe_mayor_deposito < deposito:
                        importe_mayor_deposito = deposito

                    break
            # Si el usuario elige la opción 3, le pido que ingrese el saldo a retirar. Si el monto ingresado es
            # superior al que se encuentra en su cuenta, entonces no le permito retirar. También evalúo si el monto
            # a retirar es múltiplo de 50. Si no lo es, no le permito retirar.
            elif option == 3:
                while True:
                    retiro = int(input('Ingrese el monto a retiro: $'))

                    if user_id == 1:
                        if retiro > cliente1[2]:
                            print('El dinero requerido excede el monto de su cuenta!')
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
                    
                    if retiro > 5000:
                        print('No se puede retirar mas de $5000!')
                        break

                    if retiro % 50 != 0:
                        print('Solo se pueden retirar montos múltiplos de 50')
                        break

                    de500 = 0
                    de200 = 0
                    de100 = 0
                    de50 = 0

                    # Realizo la extracción de dinero de la cuenta del usuario que se encuentra logueado. Para entregar dicho dinero,
                    # tengo que tener en cuenta que debo hacerlo proporcionando la mínima cantidad de billetes posible.
                    
                    if user_id == 1:
                        while True:
                            retiro_while = retiro
                            if retiro_while <= total_en_cajero:
                                if retiro_while != 0:
                                    de500 = int(retiro_while/500)
                                    retiro_while = retiro_while % 500
                                    if de500 >= billetes_500:
                                        retiro_while = retiro_while + (de500 - billetes_500) * 500
                                        de500 = billetes_500
                                
                                if retiro_while != 0:
                                    de200 = int(retiro_while/200)
                                    retiro_while = retiro_while % 200
                                    if de200 >= billetes_200:
                                        retiro_while = retiro_while + (de200 - billetes_200) * 200
                                        de200 = billetes_200
                                
                                if retiro_while != 0:
                                    de100 = int(retiro_while/100)
                                    retiro_while = retiro_while % 100
                                    if de100 >= billetes_100:
                                        retiro_while = retiro_while + (de100 - billetes_100) * 100
                                        de100 = billetes_100

                                if retiro_while != 0:
                                    de50 = int(retiro_while/50)
                                    retiro_while = retiro_while % 50
                                    if de50 >= billetes_50:
                                        retiro_while = retiro_while + (de50 - billetes_50) * 50
                                        de50 = billetes_50

                                # Evalúo si la operación fue exitosa. Si es así, realizo el correspondiente análisis. Si no, 
                                # emito un mensaje expresando que el cajero no puede llevar a cabo esa operación.
                                
                                if retiro_while == 0:
                                    billetes_500 -= de500
                                    billetes_200 -= de200
                                    billetes_100 -= de100
                                    billetes_50 -= de50
                                    billetes_entregados = [de500, de200, de100, de50]
                                    print('RETIRO REALIZADO:')
                                    print('Billetes de 500', billetes_entregados[0])
                                    print('Billetes de 200:', billetes_entregados[1])
                                    print('Billetes de 100:', billetes_entregados[2])
                                    print('Billetes de 50:', billetes_entregados[3])
                                    
                                    billetes_50_entregados += billetes_entregados[3]
                                    billetes_100_entregados += billetes_entregados[2]
                                    billetes_200_entregados += billetes_entregados[1]
                                    billetes_500_entregados += billetes_entregados[0]
                                    
                                    cliente1[2] -= retiro
                                    importe_total_retirado += retiro
                                    
                                    # Busco si el importe retirado es mayor que otro importe retirado por otro cliente en
                                    # la misma jornada para después emitirlo en el ticket.
                                    if importe_mayor_retiro < retiro:
                                        importe_mayor_retiro = retiro

                                    if cliente1[6] != 'BANMAS':
                                        cliente1[2] -= COMISION
                                        importe_comisiones += COMISION

                                    break
                                else:
                                    print('El cajero no puede entregar el monto solicitado')
                                    break
                            else:
                                print('No hay suficiente dinero en el cajero')
                                break
                    elif user_id == 2:
                        while True:
                            retiro_while = retiro
                            if retiro_while <= total_en_cajero:
                                if retiro_while != 0:
                                    de500 = int(retiro_while/500)
                                    retiro_while = retiro_while % 500
                                    if de500 >= billetes_500:
                                        retiro_while = retiro_while + (de500 - billetes_500) * 500
                                        de500 = billetes_500
                                
                                if retiro_while != 0:
                                    de200 = int(retiro_while/200)
                                    retiro_while = retiro_while % 200
                                    if de200 >= billetes_200:
                                        retiro_while = retiro_while + (de200 - billetes_200) * 200
                                        de200 = billetes_200
                                
                                if retiro_while != 0:
                                    de100 = int(retiro_while/100)
                                    retiro_while = retiro_while % 100
                                    if de100 >= billetes_100:
                                        retiro_while = retiro_while + (de100 - billetes_100) * 100
                                        de100 = billetes_100

                                if retiro_while != 0:
                                    de50 = int(retiro_while/50)
                                    retiro_while = retiro_while % 50
                                    if de50 >= billetes_50:
                                        retiro_while = retiro_while + (de50 - billetes_50) * 50
                                        de50 = billetes_50

                                # Evalúo si la operación fue exitosa. Si es así, realizo el correspondiente análisis. Si no, 
                                # emito un mensaje expresando que el cajero no puede llevar a cabo esa operación.

                                if retiro_while == 0:
                                    billetes_500 -= de500
                                    billetes_200 -= de200
                                    billetes_100 -= de100
                                    billetes_50 -= de50
                                    billetes_entregados = [de500, de200, de100, de50]
                                    print('RETIRO REALIZADO:')
                                    print('Billetes de 500', billetes_entregados[0])
                                    print('Billetes de 200:', billetes_entregados[1])
                                    print('Billetes de 100:', billetes_entregados[2])
                                    print('Billetes de 50:', billetes_entregados[3])
                                    
                                    billetes_50_entregados += billetes_entregados[3]
                                    billetes_100_entregados += billetes_entregados[2]
                                    billetes_200_entregados += billetes_entregados[1]
                                    billetes_500_entregados += billetes_entregados[0]
                                    
                                    cliente2[2] -= retiro
                                    importe_total_retirado += retiro

                                    # Busco si el importe retirado es mayor que otro importe retirado por otro cliente en
                                    # la misma jornada para después emitirlo en el ticket.
                                    if importe_mayor_retiro < retiro:
                                        importe_mayor_retiro = retiro

                                    if cliente2[6] != 'BANMAS':
                                        cliente2[2] -= COMISION
                                        importe_comisiones += COMISION

                                    break
                                else:
                                    print('El cajero no puede entregar el monto solicitado')
                                    break
                            else:
                                print('No hay suficiente dinero en el cajero')
                                break
                    elif user_id == 3:
                        while True:
                            retiro_while = retiro
                            if retiro_while <= total_en_cajero:
                                if retiro_while != 0:
                                    de500 = int(retiro_while/500)
                                    retiro_while = retiro_while % 500
                                    if de500 >= billetes_500:
                                        retiro_while = retiro_while + (de500 - billetes_500) * 500
                                        de500 = billetes_500
                                
                                if retiro_while != 0:
                                    de200 = int(retiro_while/200)
                                    retiro_while = retiro_while % 200
                                    if de200 >= billetes_200:
                                        retiro_while = retiro_while + (de200 - billetes_200) * 200
                                        de200 = billetes_200
                                
                                if retiro_while != 0:
                                    de100 = int(retiro_while/100)
                                    retiro_while = retiro_while % 100
                                    if de100 >= billetes_100:
                                        retiro_while = retiro_while + (de100 - billetes_100) * 100
                                        de100 = billetes_100

                                if retiro_while != 0:
                                    de50 = int(retiro_while/50)
                                    retiro_while = retiro_while % 50
                                    if de50 >= billetes_50:
                                        retiro_while = retiro_while + (de50 - billetes_50) * 50
                                        de50 = billetes_50

                                # Evalúo si la operación fue exitosa. Si es así, realizo el correspondiente análisis. Si no, 
                                # emito un mensaje expresando que el cajero no puede llevar a cabo esa operación.

                                if retiro_while == 0:
                                    billetes_500 -= de500
                                    billetes_200 -= de200
                                    billetes_100 -= de100
                                    billetes_50 -= de50
                                    billetes_entregados = [de500, de200, de100, de50]
                                    print('RETIRO REALIZADO:')
                                    print('Billetes de 500', billetes_entregados[0])
                                    print('Billetes de 200:', billetes_entregados[1])
                                    print('Billetes de 100:', billetes_entregados[2])
                                    print('Billetes de 50:', billetes_entregados[3])
                                    
                                    billetes_50_entregados += billetes_entregados[3]
                                    billetes_100_entregados += billetes_entregados[2]
                                    billetes_200_entregados += billetes_entregados[1]
                                    billetes_500_entregados += billetes_entregados[0]
                                    
                                    cliente3[2] -= retiro
                                    importe_total_retirado += retiro

                                    # Busco si el importe retirado es mayor que otro importe retirado por otro cliente en
                                    # la misma jornada para después emitirlo en el ticket.
                                    if importe_mayor_retiro < retiro:
                                        importe_mayor_retiro = retiro

                                    if cliente3[6] != 'BANMAS':
                                        cliente3[2] -= COMISION
                                        importe_comisiones += COMISION

                                    break
                                else:
                                    print('El cajero no puede entregar el monto solicitado')
                                    break
                            else:
                                print('No hay suficiente dinero en el cajero')
                                break
                    elif user_id == 4:
                        while True:
                            retiro_while = retiro
                            if retiro_while <= total_en_cajero:
                                if retiro_while != 0:
                                    de500 = int(retiro_while/500)
                                    retiro_while = retiro_while % 500
                                    if de500 >= billetes_500:
                                        retiro_while = retiro_while + (de500 - billetes_500) * 500
                                        de500 = billetes_500
                                
                                if retiro_while != 0:
                                    de200 = int(retiro_while/200)
                                    retiro_while = retiro_while % 200
                                    if de200 >= billetes_200:
                                        retiro_while = retiro_while + (de200 - billetes_200) * 200
                                        de200 = billetes_200
                                
                                if retiro_while != 0:
                                    de100 = int(retiro_while/100)
                                    retiro_while = retiro_while % 100
                                    if de100 >= billetes_100:
                                        retiro_while = retiro_while + (de100 - billetes_100) * 100
                                        de100 = billetes_100

                                if retiro_while != 0:
                                    de50 = int(retiro_while/50)
                                    retiro_while = retiro_while % 50
                                    if de50 >= billetes_50:
                                        retiro_while = retiro_while + (de50 - billetes_50) * 50
                                        de50 = billetes_50

                                # Evalúo si la operación fue exitosa. Si es así, realizo el correspondiente análisis. Si no, 
                                # emito un mensaje expresando que el cajero no puede llevar a cabo esa operación.

                                if retiro_while == 0:
                                    billetes_500 -= de500
                                    billetes_200 -= de200
                                    billetes_100 -= de100
                                    billetes_50 -= de50
                                    billetes_entregados = [de500, de200, de100, de50]
                                    print('RETIRO REALIZADO:')
                                    print('Billetes de 500', billetes_entregados[0])
                                    print('Billetes de 200:', billetes_entregados[1])
                                    print('Billetes de 100:', billetes_entregados[2])
                                    print('Billetes de 50:', billetes_entregados[3])
                                    
                                    billetes_50_entregados += billetes_entregados[3]
                                    billetes_100_entregados += billetes_entregados[2]
                                    billetes_200_entregados += billetes_entregados[1]
                                    billetes_500_entregados += billetes_entregados[0]
                                    
                                    cliente4[2] -= retiro
                                    importe_total_retirado += retiro
                                    
                                    # Busco si el importe retirado es mayor que otro importe retirado por otro cliente en
                                    # la misma jornada para después emitirlo en el ticket.
                                    if importe_mayor_retiro < retiro:
                                        importe_mayor_retiro = retiro
                                    
                                    if cliente4[6] != 'BANMAS':
                                        cliente4[2] -= COMISION
                                        importe_comisiones += COMISION

                                    break
                                else:
                                    print('El cajero no puede entregar el monto solicitado')
                                    break
                            else:
                                print('No hay suficiente dinero en el cajero')
                                break
                    elif user_id == 5:
                        while True:
                            retiro_while = retiro
                            if retiro_while <= total_en_cajero:
                                if retiro_while != 0:
                                    de500 = int(retiro_while/500)
                                    retiro_while = retiro_while % 500
                                    if de500 >= billetes_500:
                                        retiro_while = retiro_while + (de500 - billetes_500) * 500
                                        de500 = billetes_500
                                
                                if retiro_while != 0:
                                    de200 = int(retiro_while/200)
                                    retiro_while = retiro_while % 200
                                    if de200 >= billetes_200:
                                        retiro_while = retiro_while + (de200 - billetes_200) * 200
                                        de200 = billetes_200
                                
                                if retiro_while != 0:
                                    de100 = int(retiro_while/100)
                                    retiro_while = retiro_while % 100
                                    if de100 >= billetes_100:
                                        retiro_while = retiro_while + (de100 - billetes_100) * 100
                                        de100 = billetes_100

                                if retiro_while != 0:
                                    de50 = int(retiro_while/50)
                                    retiro_while = retiro_while % 50
                                    if de50 >= billetes_50:
                                        retiro_while = retiro_while + (de50 - billetes_50) * 50
                                        de50 = billetes_50

                                # Evalúo si la operación fue exitosa. Si es así, realizo el correspondiente análisis. Si no, 
                                # emito un mensaje expresando que el cajero no puede llevar a cabo esa operación.

                                if retiro_while == 0:
                                    billetes_500 -= de500
                                    billetes_200 -= de200
                                    billetes_100 -= de100
                                    billetes_50 -= de50
                                    billetes_entregados = [de500, de200, de100, de50]
                                    print('RETIRO REALIZADO:')
                                    print('Billetes de 500', billetes_entregados[0])
                                    print('Billetes de 200:', billetes_entregados[1])
                                    print('Billetes de 100:', billetes_entregados[2])
                                    print('Billetes de 50:', billetes_entregados[3])
                                    
                                    billetes_50_entregados += billetes_entregados[3]
                                    billetes_100_entregados += billetes_entregados[2]
                                    billetes_200_entregados += billetes_entregados[1]
                                    billetes_500_entregados += billetes_entregados[0]
                                    
                                    cliente5[2] -= retiro
                                    importe_total_retirado += retiro
                                    
                                    # Busco si el importe retirado es mayor que otro importe retirado por otro cliente en
                                    # la misma jornada para después emitirlo en el ticket.
                                    if importe_mayor_retiro < retiro:
                                        importe_mayor_retiro = retiro

                                    if cliente5[6] != 'BANMAS':
                                        cliente5[2] -= COMISION
                                        importe_comisiones += COMISION

                                    break
                                else:
                                    print('El cajero no puede entregar el monto solicitado')
                                    break
                            else:
                                print('No hay suficiente dinero en el cajero')
                                break
                    break
            elif option == 4:
                print('Saludos!')
                veces_que_se_uso += 1
                break
            else:
                print('Opción incorrecta!')

# Evalúo cuántos intentos realizaron entre todos los clientes para emitirlo en el ticket.
if tries_cliente1 != 0:
    veces_bloqueado += 1

if tries_cliente2 != 0:
    veces_bloqueado += 1

if tries_cliente3 != 0:
    veces_bloqueado += 1

if tries_cliente4 != 0:
    veces_bloqueado += 1

if tries_cliente5 != 0:
    veces_bloqueado += 1


print('----------------------------------')
print('TICKET FINAL DEL CAJERO:')
print(f'Cantidad de veces que se usó el cajero: {veces_que_se_uso}')
print(f'Cantidad de veces que se ingresaron 3 veces de forma errónea la clave: {veces_bloqueado}')
print(f'El importe total entregado fue de: ${importe_total_retirado}')
print(f'El importe total depositado fue de: ${importe_total_depositado}')
print(f'El total cobrado por comisiones fue: ${importe_comisiones}')
print(f'La cantidad entregada de billetes de 50 fue: {billetes_50_entregados}')
print(f'La cantidad entregada de billetes de 100 fue: {billetes_100_entregados}')
print(f'La cantidad entregada de billetes de 200 fue: {billetes_200_entregados}')
print(f'La cantidad entregada de billetes de 500 fue: {billetes_500_entregados}')
print(f'El retiro mayor fue de: ${importe_mayor_retiro}')
print(f'El depósito mayor fue de: ${importe_total_depositado}')
print('----------------------------------')
