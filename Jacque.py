import random 
print("Elige una opcion :")
print("                                1) Cosas que amo de ti ")
print("                                2) Razones por las que te amo")      
print("                                3) Momentos que me encatan ")        
print("                                4) Cosas que no me atrevo a decir")
print("                                5) Cosas que te dedico")
print("                                Con 0 se termina el programa")
print("Si ve algun problema porfavor reportarlo")

eleccion = input("Seleccione su numero : ")
while eleccion != 0:
    if eleccion == "1":
        gacha = random.randint(1, 11)
        if gacha == 1:
            print("Tu sonrisa")
            eleccion = input("Seleccione su numero : ")
        elif gacha == 2:
            print("Tus ojos")
            eleccion = input("Seleccione su numero : ")
        elif gacha == 3:
            print("Tu pelo")
            eleccion = input("Seleccione su numero : ")
        elif gacha == 4:
            print("Tus besos")
            eleccion = input("Seleccione su numero : ")
        elif gacha == 5:
            print("Tu humor, el como me molestas")
            eleccion = input("Seleccione su numero : ")
        elif gacha == 6:
            print("Como amas")
            eleccion = input("Seleccione su numero : ")
        elif gacha == 7:
            print("La forma de tu cuerpo")
            eleccion = input("Seleccione su numero : ")
        elif gacha == 8:
            print("Tus valores")
            eleccion = input("Seleccione su numero : ")
        elif gacha == 9 :
            print("Tu como persona")
            eleccion = input("Seleccione su numero : ")
        elif gacha == 10:
            print("Eres muy inteligente")       
        else :
            print("Tu nuca")
            eleccion = input("Seleccione su numero : ")

            
    elif eleccion == "2":
        gacha = random.randint(1, 11)
        if gacha == 1:
            print("Siento que puedo decirte cualquier cosa, confio mucho en ti ")
            eleccion = input("Seleccione su numero : ")
        elif gacha == 2:
            print("Siento que te preocupas por mi, me hacen sentir querido")
            eleccion = input("Seleccione su numero : ")
        elif gacha == 3:
            print("Me encanta como me tratas, me haces sentir especial ")
            eleccion = input("Seleccione su numero : ")
        elif gacha == 4:
            print("Eres todo lo que imagine, y todo lo que quiero")
            eleccion = input("Seleccione su numero : ")
        elif gacha == 5:
            print("Me puedo imaginar en un futuro contigo, es mas anhelo ese futuro")
            eleccion = input("Seleccione su numero : ")
        elif gacha == 6:
            print("Eres muy graciosa, siempre es grato estar contigo, hay veces en donde no he podido parar de reir")
            eleccion = input("Seleccione su numero : ")
        elif gacha == 7:
            print("Cuando te he necesitado he podido confiar en ti, me gusta saber que estas para mi")
            eleccion = input("Seleccione su numero : ")
        elif gacha == 8:
            print("Algunos de mis defectos que creia insoportables, los aceptas, me aceptas")
            eleccion = input("Seleccione su numero : ")
        elif gacha == 9 :
            print("Me puedo mostrar tal y como soy, no tengo la necesidad de aparentar")
            eleccion = input("Seleccione su numero : ")
        elif gacha == 10 :
            print("Me cuesta mucho estar sin ti, en cuanto dejo tu casa ya te empiezo a extrañar")
            eleccion = input("Seleccione su numero : ")
        else :
            print("Eres increible tengo mucha admiracion por tu persona, me hace estar orgullo el hecho de estar contigo")
            eleccion = input("Seleccione su numero : ")


    elif eleccion == "3":
        gacha = random.randint(1, 11)
        if gacha == 1 :
            print("Me encanta comer contigo, me acostumbre mucho sentarme a tu lado son momentos que woah")
            eleccion = input("Seleccione su numero : ")
        elif gacha == 2:
            print("Dormir contigo, como me gusta aunque aveces no me sientas, me da risa como aveces lanzas golpes o empujones porque tienes calor y cuando estas por despertar te giras a abrazarme y me haec pensar la amo")
            eleccion = input("Seleccione su numero : ")
        elif gacha == 3:
            print("Sacarnos fotos, aunque sea horrible posando las tengo todas guardadas y las miro de tanto en tanto, las amo ")
            eleccion = input("Seleccione su numero : ")
        elif gacha == 4:
            print("Verte trabajar, es algo que tengo desde el hospital pero me encanta verte haciendo cosas, cuando estas en los sims o overcook amo")
            eleccion = input("Seleccione su numero : ")
        elif gacha == 5:
            print("Abrazarte es una de las cosas que me generan woah, el hecho de sentirte cerca tu piel, saber que te puedo apretar simplemente me encanta")
            eleccion = input("Seleccione su numero : ")
        elif gacha == 6:
            print("Darte besos, obvio podria pasar dias enteros solo darte besos, me encantan tus labios son perfectos")
            eleccion = input("Seleccione su numero : ")
        elif gacha == 7:
            print("Existir juntos, es algo que me he dado cuenta que no me desagrada, que te vayas a tu cajita es como estar sin estar, ir a estudiar a tu starbucks, estar presente pero no del todo")
            eleccion = input("Seleccione su numero : ")
        elif gacha == 8:
            print("Me gusta tener intimidad contigo, es algo que aprecio mucho, siento que despertarte demaciado mi sexualidad, esque tu simplemente me encantas")
            eleccion = input("Seleccione su numero : ")
        elif gacha == 9 :
            print("Cuando eres orgullosa, o sabes que eres inteligente, la voz que pones las caras, amo todo eso de ti, y naciste para ser glorificada")
            eleccion = input("Seleccione su numero : ")
        elif gacha == 10 :
            print("Me encanta tus pequeños gestos, que me esciribas pelotudo tkm, o kmi, tengo muchos ejemplos pero intento acortar un poco, me hacen sonrojar  ")
            eleccion = input("Seleccione su numero : ")
        else :
            print("Cuando estas en algo que te gusta, tu skincare, tus hijas, cuando empiezas a sacor fotos o  cuando jugabas sims me encanta ver esa obsecion que te da con algunas cosas hasta con teresa intento darte toda mi atencion")
            eleccion = input("Seleccione su numero : ")

        
    elif eleccion == "4" :
        gacha = random.randint(1, 6)
        if gacha == 1 :
            print("Antes de conocerte: antes de que jacqueline existiera en mi vida, el 2021 fue un año no muy grato, no tenia mucha motivacion ni alguna razon para hacer lo que estaba haciendo todavia me afectaba la perdida de mi abuelo, y no creo que sienta alguna felicidad en ese momento, entre al hospital porque queria plata y todos decian que era bueno que tuviea nuevas experiencias ")
            eleccion = input("Seleccione su numero : ")
        elif gacha == 2:
            print("Cuando te conoci: Bueno al principio no creia que ibas a ser importante, aunque desde el primer minuto tu sonrisa me fascino, la primera interaccion que considero es la de haberte pedido el turno, despues de eso me gustaba mucho que me tocara contigo, te encontraba graciosa aparte tenias el topico de molestarnos, eras la persona que mejoraba mis turnos, desde mucho tiempo siempre me gusto ver tu nombre en mi rotativa, eras la persona con la que agradecia si me tocaba, siempre fuiste mejor que los demas para mi  ")
            eleccion = input("Seleccione su numero : ")
        elif gacha == 3:
            print("Cuando te empece a querer: A medida que iba pasando mas tiempo contigo, cada vez querias mas ya te consideraba alguien importante, alguien confiable y tambien sentia cierta atraccion hacia ti, pero para mi seguias siendo un lugar agradable en el que podia pasar mucho tiempo sin aburrirme, me gustaba pasar tiempo contigo, salir al carrito de los cuatro alamos, ir a comer, turnarnos juntos, en fin desde aqui me encantaba 100 pasar tiempo contigo")
            eleccion = input("Seleccione su numero : ")
        elif gacha == 4:
            print("Cuando te empece a amar: Esta epoca creo que empiza desde agosto, eran especial para mi, eras mi persona contigo queria estar, cuando vimos got pasar mucho tiempo contigo, creo que aqui empece a querer ser especial para ti, para mi eras increible, brillante, hermosa y pensaba aprovechar cada momento a tu lado, agosto hasta octubre solo pensaba en ti, queria decirtelo grabe un video diciendo que lo iba a ser, porque eras demaciado para mi, lo que siempre soñe, eras la persona con la que fantaseaba sin nisiquiera conocerte, no intentaba aprovecharme de ti, te deseo el bien desde el fondo de mi corazon")
            eleccion = input("Seleccione su numero : ")
        elif gacha == 5:
            print("Avance de mi amor, cuando acepte que sentia amor x ti, tenia que aceptar algo mas, que no ibas a estar conmigo durante este proceso siempre te ame mas, aunque aveces solo discutia, te amo y mucho, pero no querias esa version de mi por eso intentaba controlar mis sentimientos ""superarte "", pero me referia a que necesitaba poder controlar mis emociones , envidiaba a las personas que podian tener tu atencion , agradezco no haberte nunca dejado del todo, esta epoca me ayudo a madurar mucho la verdad, eres mi primer amor, y espero que el unico asi que no queria estar sin ti, intentaba hacerme creer que ya no sentia tanto para poder estar contigo de alguna forma, aunque hayan sucedido cosas que me hacan daño o sabia que habian cosas que me hacian daño ")
            eleccion = input("Seleccione su numero : ")
        else  :
            print("Ahora: Es dificil intentar acortar todo lo quiero decir, pero ahora me cuesta no pensar en ti, cuando no te veo mis dias son malos y cuando te veo son buenos, cuando siento tu olor me siento comodo y la ausencia de este me hace sentir perdido, eres parte fundamental de mi vida y quiero que sigaas asi, me cuesta pensar en una vida sin ti en estos momentos, espero que nunca me toque vivirla aunque sea medio torpe aveces cuando no me veo feliz o cosas asi, la verdad esque siempre estoy expectante a cundo pueda estar contigo, a tocarte a besarte y mas, talvez aveces me centro los 2. Siento que hemos tenido malas experiencia con la palabra familia, no aprecio muxo a la mia aunque la palabra pese, quiero que seas la persona con la que decidi estar, con quien decida gastar mi tiempo, con quien decida vivir, cocn quien decicda un futuro, talvez sea mucho para ti, pero quiero ser un lugar comodo, un lugar agradable, intento trabajar en eso aunque aveces falle, la verdad hay muchas cosas que no tengo idea, pero si se que te amo y mucho, te amo elevado a infiito y mas")
            eleccion = input("Seleccione su numero : ")

    elif eleccion == "5":
        gacha = random.randint(1, 11)
        if gacha == 1:
            print("Elvis Presley Can't Help Falling In Love (cancion) ")
            eleccion = input("Seleccione su numero : ")
        elif gacha == 2:
            print("Paramore Only Exception (cancion)")
            eleccion = input("Seleccione su numero : ")
        elif gacha == 3:
            print("Billie Eilish everything i wanted (cancion) ")
            eleccion = input("Seleccione su numero : ")
        elif gacha == 4:
            print("The 1975 All i need to hear (cancion)")
            eleccion = input("Seleccione su numero : ")
        elif gacha == 5:
            print("Twenty One Pilots we dont believe whats on tv (cancion)")
            eleccion = input("Seleccione su numero : ")
        elif gacha == 6:
            print("Radiohead Creep (cancion) ")
            eleccion = input("Seleccione su numero : ")
        elif gacha == 7:
            print("Artic Monekeys i wanna be yours (cancion)")
            eleccion = input("Seleccione su numero : ")
        elif gacha == 8:
            print("Cigarretes After Sex Sweet(cancion)")
            eleccion = input("Seleccione su numero : ")
        elif gacha == 9 :
            print("Bon Jovi Thank you for loving me (cancion)")
            eleccion = input("Seleccione su numero : ")
        elif gacha == 10 :
            print("Lana del Rey Say yes the heaven(cancion)")
            eleccion = input("Seleccione su numero : ")
        else :
            print("Julieta Venegas Limon y sal ")
            eleccion = input("Seleccione su numero : ")

            
    else :
        print("Ese numero es invalido")
        eleccion = input("Seleccione su numero : ")

    
