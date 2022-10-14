
print("¡Bienvenido!")
while True:
    archivo=open("Inventario.txt","r")
    inv=archivo.readlines()
    

    invent=[]
    for v in inv:
        reg=v.split(",")
        invent.append(reg)

    inventari=invent[0]
    
    #Función para crear el inventario total
    def crear_inventario(x):
        s=[]
        for i in range (0,len(inventari),4):
            s.append(inventari[i:i+4])
        return(s)
    iniciar=0
    inventario=crear_inventario(iniciar)
    archivo.close()
    
    #Lista de artículos por departamento
    departamento1=[inventario[0:5]]
    departamento2=[inventario[5:10]]
    departamento3=[inventario[10:15]]
    departamento4=[inventario[15:20]]
    
    ventas=open("Ventas.txt","r")
    v=ventas.readlines()

    ven=[]
    for v in v:
        reg=v.split(",")
        ven.append(reg)

    venta=ven[0]

    #Función para lista de ventas totales por Vendedor, Artículo y Cantidad.
    def crear_ventas(x):
        h=[]
        for i in range (0,len(venta),3):
            h.append(venta[i:i+3])
        return(h)
    comenzar=0
    lista_ventas=crear_ventas(comenzar)
    ventas.close()

    #Lista de artículos por departamento
    ventas_vendedor1=lista_ventas[0:5]
    ventas_vendedor2=lista_ventas[5:10]
    ventas_vendedor3=lista_ventas[10:15]
    ventas_vendedor4=lista_ventas[15:20]
    
    #Variables de Cantidad de cada Artículo
    cant_nueva_producto1=int(departamento1[0][0][3])
    cant_nueva_producto2=int(departamento1[0][1][3])
    cant_nueva_producto3=int(departamento1[0][2][3])
    cant_nueva_producto4=int(departamento1[0][3][3])
    cant_nueva_producto5=int(departamento1[0][4][3])
    cant_nueva_producto6=int(departamento2[0][0][3])
    cant_nueva_producto7=int(departamento2[0][1][3])
    cant_nueva_producto8=int(departamento2[0][2][3])
    cant_nueva_producto9=int(departamento2[0][3][3])
    cant_nueva_producto10=int(departamento2[0][4][3])
    cant_nueva_producto11=int(departamento3[0][0][3])
    cant_nueva_producto12=int(departamento3[0][1][3])
    cant_nueva_producto13=int(departamento3[0][2][3])
    cant_nueva_producto14=int(departamento3[0][3][3])
    cant_nueva_producto15=int(departamento3[0][4][3])
    cant_nueva_producto16=int(departamento4[0][0][3])
    cant_nueva_producto17=int(departamento4[0][1][3])
    cant_nueva_producto18=int(departamento4[0][2][3])
    cant_nueva_producto19=int(departamento4[0][3][3])
    cant_nueva_producto20=int(departamento4[0][4][3])
    
    #Variables de cantidad de ventas por vendedor.
    ventas_vendedor1_producto1=int(ventas_vendedor1[0][2])
    ventas_vendedor1_producto2=int(ventas_vendedor1[1][2])
    ventas_vendedor1_producto3=int(ventas_vendedor1[2][2])
    ventas_vendedor1_producto4=int(ventas_vendedor1[3][2])
    ventas_vendedor1_producto5=int(ventas_vendedor1[4][2])
    ventas_vendedor2_producto6=int(ventas_vendedor2[0][2])
    ventas_vendedor2_producto7=int(ventas_vendedor2[1][2])
    ventas_vendedor2_producto8=int(ventas_vendedor2[2][2])
    ventas_vendedor2_producto9=int(ventas_vendedor2[3][2])
    ventas_vendedor2_producto10=int(ventas_vendedor2[4][2])
    ventas_vendedor3_producto11=int(ventas_vendedor3[0][2])
    ventas_vendedor3_producto12=int(ventas_vendedor3[1][2])
    ventas_vendedor3_producto13=int(ventas_vendedor3[2][2])
    ventas_vendedor3_producto14=int(ventas_vendedor3[3][2])
    ventas_vendedor3_producto15=int(ventas_vendedor3[4][2])
    ventas_vendedor4_producto16=int(ventas_vendedor4[0][2])
    ventas_vendedor4_producto17=int(ventas_vendedor4[1][2])
    ventas_vendedor4_producto18=int(ventas_vendedor4[2][2])
    ventas_vendedor4_producto19=int(ventas_vendedor4[3][2])
    ventas_vendedor4_producto20=int(ventas_vendedor4[4][2])
    
    #Se le dan las opciones al usuario de qué quiere hacer.
    print("Escribe 'comprar' para comprar un artículo")
    print("Escribe 'registrar' para registrar llegada de artículo")
    print("Escribe 'inventario' para consultar el inventario")
    print("Escribe 'ventas' para consultar las ventas")
    print("Escribe 'ventas vendedor' para reporte de ventas por vendedor")
    print("Escribe 'ventas articulo' para reporte de ventas por artículo")
    n=input("¿Qué quieres hacer? ")
    #Según la opción que elija el usuario, se le lleva a la opción mediante un if.
    if n.lower()=="comprar":
        print("Hola, ¿a qué departamento quiere ir?")
        print("departamento1, departamento2,  departamento3 o departamento4")
        dep=input("Departamento: ")
        #En esta función se recibe  el dato de la cantidad del artículo antes de la venta y la cantidad que se quiere comprar.
        #Después toma ambos datos y los resta, para obtener la cantidad que queda de ese artículo.
        def venta(cantidad_articulo,cant_nueva):
                cant_nueva=cant_nueva-cantidad_articulo
                return cant_nueva
        #Dependiendo de que escriba el usuario, lo lleva a dicho departamento.
        #Por ejemplo al escribir 'departamento1', va al departamento de departamento1.
        if dep.lower()=="departamento1":
            print("Buen día, soy vendedor1, encargado del departamento de departamento1")
            print("nuestros artículos son: ")
            for articulo in departamento1:
                #Imprime los artículos disponibles en el departamento y su cantidad.
                print(articulo[0][3],articulo[0][2]+" disponibles.")
                print(articulo[1][3],articulo[1][2]+" disponibles.")
                print(articulo[2][3],articulo[2][2]+" disponibles.")
                print(articulo[3][3],articulo[3][2]+" disponibles.")
                print(articulo[4][3],articulo[4][2]+" disponibles.")
            #Se le pregunta al usuario qué comprará, y se hace lower en los if para que todo sea minúscula y evitar errores en el código.
            articulo_comprar=input("¿Qué quiere comprar? ")
            cantidad_articulo=int(input("¿Cuántas quiere? "))
            if articulo_comprar.lower()=="producto1":
                #Si no quedan artículos, envia un mensaje de que se acabaron.
                if int(cant_nueva_producto1)==0:
                    print("Lo siento, se nos acabaron.")
                #Si quedan suficientes artículos en la tienda, se ejecuta la venta.
                #Por medio de la función (venta) se resta la cantidad comprada a la total.
                #Al hacerse la compra, se le suma la cantidad que se compro a las ventas del vendedor de el departamento.
                elif cantidad_articulo<=cant_nueva_producto1:
                    cant_nueva_producto1=venta(cantidad_articulo,cant_nueva_producto1)
                    ventas_vendedor1_producto1=ventas_vendedor1_producto1+cantidad_articulo
                    print("Está bien, gracias por su compra")
                #Si la cantidad que pide el usuario es mayor a la disponible, se le notifica que no alcanzan, y se le dice la cantidad en existencia.
                elif cantidad_articulo>0 and cantidad_articulo>cant_nueva_producto1:
                    print("Lo siento, sólo nos quedan",cant_nueva_producto1)
            elif articulo_comprar.lower()=="producto2":
                if int(cant_nueva_producto2)==0:
                    print("Lo siento, se nos acabaron.")
                elif cantidad_articulo<=cant_nueva_producto2:
                    cant_nueva_producto2=venta(cantidad_articulo,cant_nueva_producto2)
                    ventas_vendedor1_producto2=ventas_vendedor1_producto2+cantidad_articulo
                    print("Está bien, gracias por su compra")
                elif cantidad_articulo>0 and cantidad_articulo>cant_nueva_producto2:
                    print("Lo siento, sólo nos quedan",cant_nueva_producto2)
            elif articulo_comprar.lower()=="producto3":
                if int(cant_nueva_producto3)==0:
                    print("Lo siento, se nos acabaron.")
                elif cantidad_articulo<=cant_nueva_producto3:
                    cant_nueva_producto3=venta(cantidad_articulo,cant_nueva_producto3)
                    ventas_vendedor1_producto3=ventas_vendedor1_producto3+cantidad_articulo
                    print("Está bien, gracias por su compra")
                elif cantidad_articulo>0 and cantidad_articulo>cant_nueva_producto3:
                    print("Lo siento, sólo nos quedan",cant_nueva_producto3)
            elif articulo_comprar.lower()=="producto4":
                if int(cant_nueva_producto4)==0:
                    print("Lo siento, se nos acabaron.")
                elif cantidad_articulo<=cant_nueva_producto4:
                    cant_nueva_producto4=venta(cantidad_articulo,cant_nueva_producto4)
                    ventas_vendedor1_producto4=ventas_vendedor1_producto4+cantidad_articulo
                    print("Está bien, gracias por su compra")
                elif cantidad_articulo>0 and cantidad_articulo>cant_nueva_producto4:
                    print("Lo siento, sólo nos quedan",cant_nueva_producto4)
            elif articulo_comprar.lower()=="producto5":
                if int(cant_nueva_producto5)==0:
                    print("Lo siento, se nos acabaron.")
                elif cantidad_articulo<=cant_nueva_producto5:
                    cant_nueva_producto5=venta(cantidad_articulo,cant_nueva_producto5)
                    ventas_vendedor1_producto5=ventas_vendedor1_producto5+cantidad_articulo
                    print("Está bien, gracias por su compra")
                elif cantidad_articulo>0 and cantidad_articulo>cant_nueva_producto5:
                    print("Lo siento, sólo nos quedan",cant_nueva_producto5)
            else:
                print("No tenemos ese artículo.")
                
        #Departamento de departamento2:
        if dep.lower()=="departamento2":
            print("Buen día, soy vendedor2, encargado del departamento de departamento2")
            print("nuestros artículos son: ")
            for articulo in departamento2:
                print(articulo[0][3],articulo[0][2]+" disponibles.")
                print(articulo[1][3],articulo[1][2]+" disponibles.")
                print(articulo[2][3],articulo[2][2]+" disponibles.")
                print(articulo[3][3],articulo[3][2]+" disponibles.")
                print(articulo[4][3],articulo[4][2]+" disponibles.")
            articulo_comprar=input("¿Qué quiere comprar? ")
            cantidad_articulo=int(input("¿Cuántas quiere? "))
            if articulo_comprar.lower()=="producto6":
                if int(cant_nueva_producto6)==0:
                    print("Lo siento, se nos acabaron.")
                elif cantidad_articulo<=cant_nueva_producto6:
                    cant_nueva_producto6=venta(cantidad_articulo,cant_nueva_producto6)
                    ventas_vendedor2_producto6=ventas_vendedor2_producto6+cantidad_articulo
                    print("Está bien, gracias por su compra")
                elif cantidad_articulo>0 and cantidad_articulo>cant_nueva_producto6:
                    print("Lo siento, sólo nos quedan",cant_nueva_producto6)
            elif articulo_comprar.lower()=="producto7":
                if int(cant_nueva_producto7)==0:
                    print("Lo siento, se nos acabaron.")
                elif cantidad_articulo<=cant_nueva_producto7:
                    cant_nueva_producto7=venta(cantidad_articulo,cant_nueva_producto7)
                    ventas_vendedor2_producto7=ventas_vendedor2_producto7+cantidad_articulo
                    print("Está bien, gracias por su compra")
                elif cantidad_articulo>0 and cantidad_articulo>cant_nueva_producto7:
                    print("Lo siento, sólo nos quedan",cant_nueva_producto7)
            elif articulo_comprar.lower()=="producto8":
                if int(cant_nueva_producto8)==0:
                    print("Lo siento, se nos acabaron.")
                elif cantidad_articulo<=cant_nueva_producto8:
                    cant_nueva_producto8=venta(cantidad_articulo,cant_nueva_producto8)
                    ventas_vendedor2_producto8=ventas_vendedor2_producto8+cantidad_articulo
                    print("Está bien, gracias por su compra")
                elif cantidad_articulo>0 and cantidad_articulo>cant_nueva_producto8:
                    print("Lo siento, sólo nos quedan",cant_nueva_producto8)
            elif articulo_comprar.lower()=="producto9":
                if int(cant_nueva_producto9)==0:
                    print("Lo siento, se nos acabaron.")
                elif cantidad_articulo<=cant_nueva_producto9:
                    cant_nueva_producto9=venta(cantidad_articulo,cant_nueva_producto9)
                    ventas_vendedor2_producto9=ventas_vendedor2_producto9+cantidad_articulo
                    print("Está bien, gracias por su compra")
                elif cantidad_articulo>0 and cantidad_articulo>cant_nueva_producto9:
                    print("Lo siento, sólo nos quedan",cant_nueva_producto9)
            elif articulo_comprar.lower()=="producto10":
                if int(cant_nueva_producto10)==0:
                    print("Lo siento, se nos acabaron.")
                elif cantidad_articulo<=cant_nueva_producto10:
                    cant_nueva_producto10=venta(cantidad_articulo,cant_nueva_producto10)
                    ventas_vendedor2_producto10=ventas_vendedor2_producto10+cantidad_articulo
                    print("Está bien, gracias por su compra")
                elif cantidad_articulo>0 and cantidad_articulo>cant_nueva_producto10:
                    print("Lo siento, sólo nos quedan",cant_nueva_producto10)
            else:
                print("No tenemos ese artículo.")
                    
        #Departamento de  departamento3:
        if dep.lower()==" departamento3":
            print("Buen día, soy vendedor3, encargado del departamento de  departamento3")
            print("nuestros artículos son: ")
            for articulo in  departamento3:
                print(articulo[0][3],articulo[0][2]+" disponibles.")
                print(articulo[1][3],articulo[1][2]+" disponibles.")
                print(articulo[2][3],articulo[2][2]+" disponibles.")
                print(articulo[3][3],articulo[3][2]+" disponibles.")
                print(articulo[4][3],articulo[4][2]+" disponibles.")
            articulo_comprar=input("¿Qué quiere comprar? ")
            cantidad_articulo=int(input("¿Cuántas quiere? "))
            if articulo_comprar.lower()=="producto11":
                if int(cant_nueva_producto11)==0:
                    print("Lo siento, se nos acabaron.")
                elif cantidad_articulo<=cant_nueva_producto11:
                    cant_nueva_producto11=venta(cantidad_articulo,cant_nueva_producto11)
                    ventas_vendedor3_producto11=ventas_vendedor3_producto11+cantidad_articulo
                    print("Está bien, gracias por su compra")
                elif cantidad_articulo>0 and cantidad_articulo>cant_nueva_producto11:
                    print("Lo siento, sólo nos quedan",cant_nueva_producto11)
            elif articulo_comprar.lower()=="producto12":
                if int(cant_nueva_producto12)==0:
                    print("Lo siento, se nos acabaron.")
                elif cantidad_articulo<=cant_nueva_producto12:
                    cant_nueva_producto12=venta(cantidad_articulo,cant_nueva_producto12)
                    ventas_vendedor3_producto12=ventas_vendedor3_producto12+cantidad_articulo
                    print("Está bien, gracias por su compra")
                elif cantidad_articulo>0 and cantidad_articulo>cant_nueva_producto12:
                    print("Lo siento, sólo nos quedan",cant_nueva_producto12)
            elif articulo_comprar.lower()=="producto13":
                if int(cant_nueva_producto13)==0:
                    print("Lo siento, se nos acabaron.")
                elif cantidad_articulo<=cant_nueva_producto13:
                    cant_nueva_producto13=venta(cantidad_articulo,cant_nueva_producto13)
                    ventas_vendedor3_producto13=ventas_vendedor3_producto13+cantidad_articulo
                    print("Está bien, gracias por su compra")
                elif cantidad_articulo>0 and cantidad_articulo>cant_nueva_producto13:
                    print("Lo siento, sólo nos quedan",cant_nueva_producto13)
            elif articulo_comprar.lower()=="producto14":
                if int(cant_nueva_producto14)==0:
                    print("Lo siento, se nos acabaron.")
                elif cantidad_articulo<=cant_nueva_producto14:
                    cant_nueva_producto14=venta(cantidad_articulo,cant_nueva_producto14)
                    ventas_vendedor3_producto14=ventas_vendedor3_producto14+cantidad_articulo
                    print("Está bien, gracias por su compra")
                elif cantidad_articulo>0 and cantidad_articulo>cant_nueva_producto14:
                    print("Lo siento, sólo nos quedan",cant_nueva_producto14)
            elif articulo_comprar.lower()=="producto15":
                if int(cant_nueva_producto15)==0:
                    print("Lo siento, se nos acabaron.")
                elif cantidad_articulo<=cant_nueva_producto15:
                    cant_nueva_producto15=venta(cantidad_articulo,cant_nueva_producto15)
                    ventas_vendedor3_producto15=ventas_vendedor3_producto15+cantidad_articulo
                    print("Está bien, gracias por su compra")
                elif cantidad_articulo>0 and cantidad_articulo>cant_nueva_producto15:
                    print("Lo siento, sólo nos quedan",cant_nueva_producto15)
            else:
                print("No tenemos ese artículo.")

        #Departamento de departamento4:
        if dep.lower()=="departamento4":
            print("Buen día, soy vendedor4, encargado del departamento de departamento4")
            print("nuestros artículos son: ")
            for articulo in departamento4:
                print(articulo[0][3],articulo[0][2]+" disponibles.")
                print(articulo[1][3],articulo[1][2]+" disponibles.")
                print(articulo[2][3],articulo[2][2]+" disponibles.")
                print(articulo[3][3],articulo[3][2]+" disponibles.")
                print(articulo[4][3],articulo[4][2]+" disponibles.")
            articulo_comprar=input("¿Qué quiere comprar? ")
            cantidad_articulo=int(input("¿Cuántas quiere? "))
            if articulo_comprar.lower()=="producto16":
                if int(cant_nueva_producto16)==0:
                    print("Lo siento, se nos acabaron.")
                elif cantidad_articulo<=cant_nueva_producto16:
                    cant_nueva_producto16=venta(cantidad_articulo,cant_nueva_producto16)
                    ventas_vendedor4_producto16=ventas_vendedor4_producto16+cantidad_articulo
                    print("Está bien, gracias por su compra")
                elif cantidad_articulo>0 and cantidad_articulo>cant_nueva_producto16:
                    print("Lo siento, sólo nos quedan",cant_nueva_producto16)
            elif articulo_comprar.lower()=="producto17":
                if int(cant_nueva_producto17)==0:
                    print("Lo siento, se nos acabaron.")
                elif cantidad_articulo<=cant_nueva_producto17:
                    cant_nueva_producto17=venta(cantidad_articulo,cant_nueva_producto17)
                    ventas_vendedor4_producto17=ventas_vendedor4_producto17+cantidad_articulo
                    print("Está bien, gracias por su compra")
                elif cantidad_articulo>0 and cantidad_articulo>cant_nueva_producto17:
                    print("Lo siento, sólo nos quedan",cant_nueva_producto17)
            elif articulo_comprar.lower()=="producto18":
                if int(cant_nueva_producto18)==0:
                    print("Lo siento, se nos acabaron.")
                elif cantidad_articulo<=cant_nueva_producto18:
                    cant_nueva_producto18=venta(cantidad_articulo,cant_nueva_producto18)
                    ventas_vendedor4_producto18=ventas_vendedor4_producto18+cantidad_articulo
                    print("Está bien, gracias por su compra")
                elif cantidad_articulo>0 and cantidad_articulo>cant_nueva_producto18:
                    print("Lo siento, sólo nos quedan",cant_nueva_producto18)
            elif articulo_comprar.lower()=="producto19":
                if int(cant_nueva_producto19)==0:
                    print("Lo siento, se nos acabaron.")
                elif cantidad_articulo<=cant_nueva_producto19:
                    cant_nueva_producto19=venta(cantidad_articulo,cant_nueva_producto19)
                    ventas_vendedor4_producto19=ventas_vendedor4_producto19+cantidad_articulo
                    print("Está bien, gracias por su compra")
                elif cantidad_articulo>0 and cantidad_articulo>cant_nueva_producto19:
                    print("Lo siento, sólo nos quedan",cant_nueva_producto19)
            elif articulo_comprar.lower()=="producto20":
                if int(cant_nueva_producto20)==0:
                    print("Lo siento, se nos acabaron.")
                elif cantidad_articulo<=cant_nueva_producto20:
                    cant_nueva_producto20=venta(cantidad_articulo,cant_nueva_producto20)
                    ventas_vendedor4_producto20=ventas_vendedor4_producto20+cantidad_articulo
                    print("Está bien, gracias por su compra")
                elif cantidad_articulo>0 and cantidad_articulo>cant_nueva_producto20:
                    print("Lo siento, sólo nos quedan",cant_nueva_producto20)
            else:
                print("No tenemos ese artículo.")

    #Registro de artículos nuevos que llegan a la tienda.
    if n.lower()=="registrar":
        print("¿De qué departamento es su artículo?")
        print("departamento1, departamento2,  departamento3 o departamento4")
        dep=input("Departamento: ")
        #Función donde recibe la cantidad del artículo inicial y la que se quiere agregar
        #Se suman las dos y luego regresa la cantidad total a una cadena de if, para ver
        #a que variable se le debe de agregar (artículo que se agregó).
        def registrar(cant_llegada,cant_nueva):
                cant_nueva=cant_nueva+cant_llegada
                return cant_nueva
        #Se lleva al departamento que corresponda dependiendo de que escribe el usuario.
        if dep.lower()=="departamento1":
            print("Buen día, soy vendedor1, encargado del departamento de departamento1")
            art_llegada=input("¿Qué artículo trae para nosotros? ")
            cant_llegada=int(input("¿Cuántos trae? "))
            #Por medio de la función (registrar) se suma la cantidad de artículos que trajo el repartidor,
            #más la cantidad de artículos que ya hay en el inventario.
            if art_llegada.lower()=="producto1":
                cant_nueva_producto1=registrar(cant_llegada,cant_nueva_producto1)
            if art_llegada.lower()=="producto2":
                cant_nueva_producto2=registrar(cant_llegada,cant_nueva_producto2)
            if art_llegada.lower()=="producto3":
                cant_nueva_producto3=registrar(cant_llegada,cant_nueva_producto3)
            if art_llegada.lower()=="producto4":
                cant_nueva_producto4=registrar(cant_llegada,cant_nueva_producto4)
            if art_llegada.lower()=="producto5":
                cant_nueva_producto5=registrar(cant_llegada,cant_nueva_producto5)
        elif dep.lower()=="departamento2":
            print("Buen día, soy vendedor2, encargado del departamento de departamento1")
            art_llegada=input("¿Qué artículo trae para nosotros? ")
            cant_llegada=int(input("¿Cuántos trae? "))
            if art_llegada.lower()=="producto6":
                cant_nueva_producto6=registrar(cant_llegada,cant_nueva_producto6)
            if art_llegada.lower()=="producto7":
                cant_nueva_producto7=registrar(cant_llegada,cant_nueva_producto7)
            if art_llegada.lower()=="producto8":
                cant_nueva_producto8=registrar(cant_llegada,cant_nueva_producto8)
            if art_llegada.lower()=="producto9":
                cant_nueva_producto9=registrar(cant_llegada,cant_nueva_producto9)
            if art_llegada.lower()=="producto10":
                cant_nueva_producto10=registrar(cant_llegada,cant_nueva_producto10)
        elif dep.lower()==" departamento3":
            print("Buen día, soy vendedor3, encargado del departamento de departamento1")
            art_llegada=input("¿Qué artículo trae para nosotros? ")
            cant_llegada=int(input("¿Cuántos trae? "))
            if art_llegada.lower()=="producto11":
                cant_nueva_producto11=registrar(cant_llegada,cant_nueva_producto11)
            if art_llegada.lower()=="producto12":
                cant_nueva_producto12=registrar(cant_llegada,cant_nueva_producto12)
            if art_llegada.lower()=="producto13":
                cant_nueva_producto13=registrar(cant_llegada,cant_nueva_producto13)
            if art_llegada.lower()=="producto14":
                cant_nueva_producto14=registrar(cant_llegada,cant_nueva_producto14)
            if art_llegada.lower()=="producto15":
                cant_nueva_producto15=registrar(cant_llegada,cant_nueva_producto15)
        elif dep.lower()=="departamento4":
            print("Buen día, soy vendedor4, encargado del departamento de departamento1")
            art_llegada=input("¿Qué artículo trae para nosotros? ")
            cant_llegada=int(input("¿Cuántos trae? "))
            if art_llegada.lower()=="producto16":
                cant_nueva_producto16=registrar(cant_llegada,cant_nueva_producto16)
            if art_llegada.lower()=="producto17":
                cant_nueva_producto17=registrar(cant_llegada,cant_nueva_producto17)
            if art_llegada.lower()=="producto18":
                cant_nueva_producto18=registrar(cant_llegada,cant_nueva_producto18)
            if art_llegada.lower()=="producto19":
                cant_nueva_producto19=registrar(cant_llegada,cant_nueva_producto19)
            if art_llegada.lower()=="producto20":
                cant_nueva_producto20=registrar(cant_llegada,cant_nueva_producto20)
        print("Gracias, la entrega quedó registrada.")
        
    #Consulta el inventario
    if n.lower()=="inventario":
        #Se imprimen las posiciones de cada artículo en la lista de cada departamento
        print("            INVENTARIO        ")
        print("Dpto."+"    "+"Modelo"+"    "+"Artículo"+"    "+"Cantidad")
        print(departamento1[0][0])
        print(departamento1[0][1])
        print(departamento1[0][2])
        print(departamento1[0][3])
        print(departamento1[0][4])
        print(departamento2[0][0])
        print(departamento2[0][1])
        print(departamento2[0][2])
        print(departamento2[0][3])
        print(departamento2[0][4])
        print(departamento3[0][0])
        print(departamento3[0][1])
        print(departamento3[0][2])
        print(departamento3[0][3])
        print(departamento3[0][4])
        print(departamento4[0][0])
        print(departamento4[0][1])
        print(departamento4[0][2])
        print(departamento4[0][3])
        print(departamento4[0][4])
        
        
    if n.lower()=="ventas":
        print("            VENTAS        ")
        print("Vendedor"+"    "+"Artículo"+"    "+"Ventas")
        #Se imprimen las listas de cada vendedor por elemento,
        #Estas sublistas contienen el nombre del vendedor, el artículo, y la cantidad de ventas de ese artículo.
        print(ventas_vendedor1[0])
        print(ventas_vendedor1[1])
        print(ventas_vendedor1[2])
        print(ventas_vendedor1[3])
        print(ventas_vendedor1[4])
        print(ventas_vendedor2[0])
        print(ventas_vendedor2[1])
        print(ventas_vendedor2[2])
        print(ventas_vendedor2[3])
        print(ventas_vendedor2[4])
        print(ventas_vendedor3[0])
        print(ventas_vendedor3[1])
        print(ventas_vendedor3[2])
        print(ventas_vendedor3[3])
        print(ventas_vendedor3[4])
        print(ventas_vendedor4[0])
        print(ventas_vendedor4[1])
        print(ventas_vendedor4[2])
        print(ventas_vendedor4[3])
        print(ventas_vendedor4[4])
        
    if n.lower()=="ventas vendedor":
        #Función que toma las variables de ventas para cada producto de un departamento y las suma.
        #Con esto, se pueden ver las ventas totales que ha hecho cada vendedor.
        def ventas_vendedor(ventas_prod_1,ventas_prod_2,ventas_prod_3,ventas_prod_4,ventas_prod_5):
            ventas_vendedor_totales=ventas_prod_1+ventas_prod_2+ventas_prod_3+ventas_prod_4+ventas_prod_5
            return ventas_vendedor_totales
        print("      VENTAS POR VENDEDOR       ")
        #Se corre la función (ventas_vendedor) dando los valores de ventas de cada producto de un departamento y se asigna el resultado a su encargado.
        totales_vendedor1=ventas_vendedor(ventas_vendedor1_producto1,ventas_vendedor1_producto2,ventas_vendedor1_producto3,ventas_vendedor1_producto4,ventas_vendedor1_producto5)
        print("Vendedor1 ha vendido "+str(totales_vendedor1)+" artículos en total.")
        totales_vendedor2=ventas_vendedor(ventas_vendedor2_producto6,ventas_vendedor2_producto7,ventas_vendedor2_producto8,ventas_vendedor2_producto9,ventas_vendedor2_producto10)
        print("vendedor2 ha vendido "+str(totales_vendedor2)+" artículos en total.")
        totales_vendedor3=ventas_vendedor(ventas_vendedor3_producto11,ventas_vendedor3_producto12,ventas_vendedor3_producto13,ventas_vendedor3_producto14,ventas_vendedor3_producto15)
        print("vendedor3 ha vendido "+str(totales_vendedor3)+" artículos en total.")
        totales_vendedor4=ventas_vendedor(ventas_vendedor4_producto16,ventas_vendedor4_producto17,ventas_vendedor4_producto18,ventas_vendedor4_producto19,ventas_vendedor4_producto20)
        print("vendedor4 ha vendido "+str(totales_vendedor4)+" artículos en total.")
        
    if n.lower()=="ventas articulo":
        print("    VENTAS POR ARTÍCULO       ")
        #Se imprime una cadena de strings en la que el valor de en medio es igual a las ventas
        #que ha habido por cada artículo.
        print("Se han vendido "+str(ventas_vendedor1_producto1)+" producto1.")
        print("Se han vendido "+str(ventas_vendedor1_producto2)+" producto2.")
        print("Se han vendido "+str(ventas_vendedor1_producto3)+" producto3.")
        print("Se han vendido "+str(ventas_vendedor1_producto4)+" producto4.")
        print("Se han vendido "+str(ventas_vendedor1_producto5)+" producto4.")
        print("Se han vendido "+str(ventas_vendedor2_producto6)+" producto6.")
        print("Se han vendido "+str(ventas_vendedor2_producto7)+"producto7")
        print("Se han vendido "+str(ventas_vendedor2_producto8)+" producto8.")
        print("Se han vendido "+str(ventas_vendedor2_producto9)+" producto9.")
        print("Se han vendido "+str(ventas_vendedor2_producto10)+" producto10.")
        print("Se han vendido "+str(ventas_vendedor3_producto11)+" producto11.")
        print("Se han vendido "+str(ventas_vendedor3_producto12)+" producto12.")
        print("Se han vendido "+str(ventas_vendedor3_producto13)+" producto13.")
        print("Se han vendido "+str(ventas_vendedor3_producto14)+" producto14.")
        print("Se han vendido "+str(ventas_vendedor3_producto15)+" producto15.")
        print("Se han vendido "+str(ventas_vendedor4_producto16)+" producto16.")
        print("Se han vendido "+str(ventas_vendedor4_producto17)+" producto17.")
        print("Se han vendido "+str(ventas_vendedor4_producto18)+" producto18.")
        print("Se han vendido "+str(ventas_vendedor4_producto19)+" producto19.")
        print("Se han vendido "+str(ventas_vendedor4_producto20)+" producto20.")
        
    #Aquí se escribe el archivo de inventario otra vez, pero ahora teniendo la variable de cantidad que corresponda
    #tras haber corrido todo el programa.
    archivo=open("Inventario.txt","w")
    #Inventario departamento1
    archivo.write("departamento1"+","+"0023"+","+"producto1"+","+str(cant_nueva_producto1)+",")
    archivo.write("departamento1"+","+"0192"+","+"producto2"+","+str(cant_nueva_producto2)+",")
    archivo.write("departamento1"+","+"1093"+","+"producto3"+","+str(cant_nueva_producto3)+",")
    archivo.write("departamento1"+","+"0456"+","+"producto4"+","+str(cant_nueva_producto4)+",")
    archivo.write("departamento1"+","+"1230"+","+"producto5"+","+str(cant_nueva_producto5)+",")
    #Inventario departamento2
    archivo.write("departamento2"+","+"1234"+","+"producto6"+","+str(cant_nueva_producto6)+",")
    archivo.write("departamento2"+","+"9203"+","+"producto7"+","+str(cant_nueva_producto7)+",")
    archivo.write("departamento2"+","+"0012"+","+"producto8"+","+str(cant_nueva_producto8)+",")
    archivo.write("departamento2"+","+"1833"+","+"producto9"+","+str(cant_nueva_producto9)+",")
    archivo.write("departamento2"+","+"3432"+","+"producto10"+","+str(cant_nueva_producto10)+",")
    #Inventario  departamento3
    archivo.write("departamento3"+","+"9239"+","+"producto11"+","+str(cant_nueva_producto11)+",")
    archivo.write("departamento3"+","+"1254"+","+"producto12"+","+str(cant_nueva_producto12)+",")
    archivo.write("departamento3"+","+"9223"+","+"producto13"+","+str(cant_nueva_producto13)+",")
    archivo.write("departamento3"+","+"1238"+","+"producto14"+","+str(cant_nueva_producto14)+",")
    archivo.write("departamento3"+","+"4352"+","+"producto15"+","+str(cant_nueva_producto15)+",")
    #Inventario departamento4
    archivo.write("departamento4"+","+"4321"+","+"producto16"+","+str(cant_nueva_producto16)+",")
    archivo.write("departamento4"+","+"3452"+","+"producto17"+","+str(cant_nueva_producto17)+",")
    archivo.write("departamento4"+","+"6582"+","+"producto18"+","+str(cant_nueva_producto18)+",")
    archivo.write("departamento4"+","+"8924"+","+"producto19"+","+str(cant_nueva_producto19)+",")
    archivo.write("departamento4"+","+"2323"+","+"producto20"+","+str(cant_nueva_producto20))
    archivo.close()
    
    #Aquí se escribe el archivo de ventas otra vez, pero ahora teniendo la variable de cantidad que corresponda
    #tras haber corrido todo el programa.
    ventas=open("Ventas.txt", "w")
    #Ventas de vendedor1, encargado de departamento de departamento1.
    ventas.write("vendedor1"+","+"producto1"+","+str(ventas_vendedor1_producto1)+",")
    ventas.write("vendedor1"+","+"producto2"+","+str(ventas_vendedor1_producto2)+",")
    ventas.write("vendedor1"+","+"producto3"+","+str(ventas_vendedor1_producto3)+",")
    ventas.write("vendedor1"+","+"producto4"+","+str(ventas_vendedor1_producto4)+",")
    ventas.write("vendedor1"+","+"producto5"+","+str(ventas_vendedor1_producto5)+",")
    #Ventas de vendedor2, encargado de departamento de departamento2.
    ventas.write("vendedor2"+","+"producto6"+","+str(ventas_vendedor2_producto6)+",")
    ventas.write("vendedor2"+","+"producto7"+","+str(ventas_vendedor2_producto7)+",")
    ventas.write("vendedor2"+","+"producto8"+","+str(ventas_vendedor2_producto8)+",")
    ventas.write("vendedor2"+","+"producto9"+","+str(ventas_vendedor2_producto9)+",")
    ventas.write("vendedor2"+","+"producto10"+","+str(ventas_vendedor2_producto10)+",")
    #Ventas de vendedor3, encargado de departamento de departamento3.
    ventas.write("vendedor3"+","+"producto11"+","+str(ventas_vendedor3_producto11)+",")
    ventas.write("vendedor3"+","+"producto12"+","+str(ventas_vendedor3_producto12)+",")
    ventas.write("vendedor3"+","+"producto13"+","+str(ventas_vendedor3_producto13)+",")
    ventas.write("vendedor3"+","+"producto14"+","+str(ventas_vendedor3_producto14)+",")
    ventas.write("vendedor3"+","+"producto15"+","+str(ventas_vendedor3_producto15)+",")
    #Ventas de vendedor4, encargado de departamento de departamento4.
    ventas.write("vendedor4"+","+"producto16"+","+str(ventas_vendedor4_producto16)+",")
    ventas.write("vendedor4"+","+"producto17"+","+str(ventas_vendedor4_producto17)+",")
    ventas.write("vendedor4"+","+"producto18"+","+str(ventas_vendedor4_producto18)+",")
    ventas.write("vendedor4"+","+"producto19"+","+str(ventas_vendedor4_producto19)+",")
    ventas.write("vendedor4"+","+"producto20"+","+str(ventas_vendedor4_producto20))
    ventas.close()
    
    #esta parte es para terminar el programa, si escribe s (que representa 'salir'), se usa quit() para terminar
    #sin embargo, si esto no se cumple, el while true del inicio vuelve a comenzar, por lo que se repite todo el programa.
    n=input("\n"+"Escribe s para terminar y cont para continuar: ")
    if n=="s":
        print("\n"+"Gracias por visitarnos, vuelva pronto")
        quit()


    
    
    
    

