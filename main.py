# PROGRAMMA NAAM: Hangman, the return
# GESCHREVEN DOOR: Ties Morshuis

################
# GLOBALE VARIABELEN
################

import random, math, turtle, string
woord_ingevoerd = False
spel_afgelopen = False
lijst_gekozen = False
niveau_gekozen = False
extern_gekozen = False
woord_toegevoegd = False
alfabet_lijst = list(string.ascii_lowercase)
goede_woord_lijst = []
gekozen_woord_lijst = []
geraden_letters_lijst = []
ingevoerde_woord_lijst = []
woord_checken = []
ingevoerde_letter = str()
keuze = 0
fouten = 0
maximale_fouten = 9
aantal_fouten_over = 0

##############
# DEFINITIES 
##############

#Hiermee kies je of je een woord kiest uit een lijst die vantevoren is gemaakt, of een woord of woordenlijst maakt
def woordtype_kiezen(lijst_gekozen, extern_gekozen, woord_toegevoegd):

  #zolang deze False is wordt er altijd om invoer gevraagd, dus hij blijft het vragen tot je een goed antwoord invoert. 
  while lijst_gekozen == False:
    keuze = input("Typ 1 voor onze lijst, typ 2 als je eigen woord of lijst wilt gebruiken: ")
    keuze = keuze.replace(" ", "")

    #als deze If 1 is gaat het programma door naar de vantevoren gemaakte lijst. 
    if keuze == "1":
      lijst_gekozen, gekozen_woord = algemeen_woord()

    #als de elif 2 is gaat die door naar het maken van een eigen woord of woordenlijst.
    elif keuze == "2":
      lijst_gekozen, gekozen_woord = eigen_woord(extern_gekozen, woord_toegevoegd,)

    else:
      print("Deze invoer kon ik niet begrijpen, probeer het opnieuw.")
  return(gekozen_woord)

#Deze kiest een woord uit een lijst die ik vantevoren heb gemaakt.
def algemeen_woord():
  gekozen_woord = woord_niveaus(niveau_gekozen)
  gekozen_woord = gekozen_woord.replace("\n", "")
  print("\n" * 50) #Om het scherm leeg te maken
  return(True, gekozen_woord)
     
#Hiermee kun je je eigen woord of eigen woordenlijst maken
def eigen_woord(extern_gekozen, woord_toegevoegd):
      
  woordenteller = 1

  #zolang deze False is blijft die vragen om input, hij wordt pas op True gezet als er een goed antwoord is gegeven.
  while extern_gekozen == False:
    externe_lijst = input("Heb je een eigen woordenlijst erin gevoegd? ")
    externe_lijst = externe_lijst.replace(" ", "")

    if externe_lijst == "nee" or externe_lijst == "Nee":
      bestand = open("eigen_woordenlijst.txt", "w")
      bestand.close()
      extern_gekozen = True

    elif externe_lijst == "ja" or externe_lijst == "Ja":
      extern_gekozen = True

    else:
      print("Sorry dat begreep ik niet, probeer het opnieuw.")

    #de functie om een woord toe te voegen in je eigen lijst
  eigen_woord_toevoegen_lijst(woord_toegevoegd, woordenteller)

  bestand = open("eigen_woordenlijst.txt", "r")    
  woordlijst = bestand.readlines()
  eigen_nieuwe_woordlijst = []
      
  for woord in woordlijst:
    woord = woord.replace("\n", "")
    eigen_nieuwe_woordlijst.append(woord)
  gekozen_woord = random.choice(eigen_nieuwe_woordlijst)
  bestand.close()
  return(True, gekozen_woord)

#Hiermee kun je woorden toevoegen in je eigen woordenlijst
def eigen_woord_toevoegen_lijst(woord_toegevoegd, woordenteller):
  #Deze while loop zorgt ervoor dat je worden kan toevoegen in de lijst, als je "klaar" of "nee" typt gaat het programma door.
  while woordenteller == 1:
    woord_toegevoegd = False
    woord = input("Typ een woord dat je wilt gebruiken, of wilt toevoegen in de lijst. Als je klaar bent, typ dan 'klaar': ")
    woord = woord.replace(" ", "")
    woord_checken[:0] = woord
    #dit checkt of er geen tekens in het woord zitten zodat het woord onmogelijk is om te raden.
    for x in woord_checken:
      if x not in alfabet_lijst:
        print("Dit woord bevat tekens die niet toegestaan zijn, probeer het opnieuw")
        continue

    #Als je klaar intypt stopt het invullen van woorden, om klaar te maken voor het raden, maar hij kijkt eerst of je wil wat hebt ingevuld.
    if woord == "klaar" or woord == "Klaar":
      bestand = open("eigen_woordenlijst.txt", "r")
      lege_lijst_check = []
      lege_lijst_check = bestand.readlines()
      for x in lege_lijst_check:
        str(x).replace(" ", "")
        lege_lijst_check.append(x)

      if lege_lijst_check == []:
        print("Je hebt geen woord ingevoerd, probeer het opnieuw.")
        continue
          
      woordenteller = 0
      #Om het scherm leeg te maken, zodat je het ingevoerde woord niet ziet.
      print( "\n" * 50)

    else:    
      bestand = open("eigen_woordenlijst.txt", "a")
      woord = woord.lower()
      bestand.write(woord)
      bestand.write("\n")

      #Nogmaals een while loop die zorgt dat er geen verkeerde antwoorden ingevoerd kunnen worden
      while woord_toegevoegd == False:
        antwoord = input("wil je nog een woord toevoegen? ")
        antwoord = antwoord.replace(" ", "")

        if antwoord == "ja" or antwoord == "Ja":
          woordenteller = 1
          woord_toegevoegd = True

        elif antwoord == "nee" or antwoord == "Nee" or antwoord == "klaar" or antwoord == "Klaar":
          woordenteller = 0
          print("\n" * 50)
          woord_toegevoegd = True

        else:
          print("Sorry dat begreep ik niet, voer het opniew in.")

      bestand.close() 

#Het gedeelte dat de letters vervangt als ze goed geraden zijn
def letters_vervangen(ingevoerde_letter):

    for i in range(len(gekozen_woord)):

        if ingevoerde_letter == goede_woord_lijst[i]:
            letter_index = i
            gekozen_woord_lijst[letter_index] = ingevoerde_letter

#Het gekozen woord naar een lijst omzetten om de lijst voor het raden mee te vergelijken
def gekozen_woord_naar_lijst(woord):
    goede_woord_lijst[:0] = woord
    return gekozen_woord_lijst

#Het gedeelte waarmee je letters raad en checkt of ze goed zijn
def letters_raden(ingevoerde_letter, goede_woord_lijst, gekozen_woord_lijst, maximale_fouten, aantal_fouten_over, fouten, woord_ingevoerd, alfabet_lijst):
    print(gekozen_woord_lijst)
    if fouten != maximale_fouten:
      #zolang het goede woord lijst niet gelijk is aan de lijst met de ingevoerde letters blijft het programma runnen
      if goede_woord_lijst != gekozen_woord_lijst:
        ingevoerde_letter = input("Voer een letter in die je wilt raden, als je het hele woord wil raden, typ dan 'woord': ")
        ingevoerde_letter = ingevoerde_letter.lower()
        ingevoerde_letter = ingevoerde_letter.replace(" ", "")

        #als het "woord" intypt tijdens het raden van letters heb je de optie om het hele 
        if ingevoerde_letter == "woord" or ingevoerde_letter == "Woord":
          spel_afgelopen == hele_woord_raden(ingevoerde_woord_lijst, fouten, aantal_fouten_over, maximale_fouten, woord_ingevoerd, goede_woord_lijst, alfabet_lijst)
          if goede_woord_lijst == ingevoerde_woord_lijst:
            return(True, fouten)
          else:
            return(False, fouten)

        if ingevoerde_letter not in alfabet_lijst:
          #bovenin staat een lijst met alle letters uit het alfabet, daar vergelijkt hij de letter mee, en als die er niet in staat geeft hij een foutmelding.
          print("Sorry, deze invoer klopt niet, probeer het opnieuw.")
          return(False, fouten)

        if ingevoerde_letter in geraden_letters_lijst:
          print("Deze letter heb je al geraden, probeer het opnieuw.")
        
        #Als de letter wel in het woord zit, wordt die toegevoegd aan de lijst met geraden letters, en wordt de letter op de goede plek gezet.
        elif ingevoerde_letter in gekozen_woord:
          print("Goed geraden! Deze letter zit in het woord!")
          print("Deze letters heb je tot nu toe geraden:")
          geraden_letters_lijst.append(ingevoerde_letter)
          letters_vervangen(ingevoerde_letter)
          print(geraden_letters_lijst)
          print("\n")

        #Als de letter niet goed is wordt die toegevoegd aan de geraden letters lijst, komt er 1 fout bij, en wordt het aantal fouten dat je nog mag maken laten zien
        elif ingevoerde_letter not in gekozen_woord:
          fouten += 1
          aantal_fouten_over = maximale_fouten - fouten
          print("Helaas, deze letter zit niet in het woord.")
          print("Je mag nog " + str(aantal_fouten_over) + " fouten maken.")
          print("Deze letters heb je tot nu geraden:")
          geraden_letters_lijst.append(ingevoerde_letter)
          print(geraden_letters_lijst)
          print("\n")
          galg_tekening(fouten)
          
        return(False, fouten)

      else:
        return(True, fouten)

    else:  
      return(True, fouten)
    
#De animatie van de galg
def galg_tekening(fouten):
    #ondergrond, platform en trapje
    if fouten == 0:
        turtle.speed(500)
        turtle.pendown()
        turtle.right(180)
        turtle.forward(350)
        turtle.right(180)
        turtle.forward(320)
        turtle.left(90)
        turtle.forward(55)
        turtle.left(180)
        turtle.forward(55)
        turtle.right(90)
        turtle.forward(20)
        turtle.right(90)
        turtle.forward(35)
        turtle.right(45)
        turtle.forward(28)
        turtle.left(135)
        turtle.forward(120)
        turtle.left(90)
        turtle.forward(55)
        turtle.left(90)
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(35)
        turtle.left(45)
        turtle.forward(28)
        turtle.left(180)
        turtle.forward(28)
        turtle.left(45)
        turtle.forward(80)
        turtle.penup()
        turtle.left(90)
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(10)
        turtle.right(90)
        turtle.pendown()
        turtle.forward(15)
        turtle.left(90)
        turtle.forward(15)
        turtle.right(90)
        turtle.forward(15)
        turtle.left(90)
        turtle.forward(15)
        turtle.right(90)
        turtle.forward(15)
        turtle.left(90)
        turtle.forward(15)
        turtle.right(90)
        turtle.forward(90)
    elif fouten == 1:
        #Verticale Balk
        turtle.right(90)
        turtle.forward(200)
        turtle.right(180)
        turtle.forward(200)
        turtle.right(90)
        turtle.forward(25)
        turtle.right(90)
        turtle.forward(225)
        turtle.right(135)
        turtle.forward(35)
    elif fouten == 2:
        #Horizontale balk
        turtle.left(45)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(25)
        turtle.left(90)
        turtle.forward(225)
    elif fouten == 3:
        #Diagonale balk
        turtle.left(135)
        turtle.penup()
        turtle.forward(35)
        turtle.right(45)
        turtle.forward(60)
        turtle.left(90)
        turtle.forward(1)
        turtle.left(45)
        turtle.pendown()
        #Via de stelling van pythagoras heb ik de lengte van de diagonale balken berekend. 
        turtle.forward(math.sqrt(7200))
        turtle.back(math.sqrt(7200))
        turtle.left(135)
        turtle.right(90)
        turtle.forward(15)
        turtle.right(45)
        turtle.forward(math.sqrt(4050))
        turtle.back(math.sqrt(4050))
        turtle.left(45)
        turtle.forward(45)
        turtle.right(90)
        turtle.forward(190)
    elif fouten == 4:
        #Het touw
        turtle.right(90)
        turtle.forward(20)
    elif fouten == 5:
        #Het hoofd
        turtle.right(90)
        turtle.circle(15)
        turtle.penup()
        turtle.left(90)
        turtle.forward(30)
        turtle.pendown()
    elif fouten == 6: 
        #Het lijf
        turtle.forward(40)
        turtle.right(180)
    elif fouten == 7:
        #De armen
        turtle.penup()
        turtle.forward(24)
        turtle.pendown()
        turtle.left(45)
        turtle.forward(20)
        turtle.back(20)
        turtle.right(90)
        turtle.forward(20)
        turtle.back(20)
        turtle.right(135)
        turtle.forward(24)
    elif fouten == 8: 
        #Been #1
        turtle.right(45)
        turtle.forward(20)
        turtle.back(20)
    elif fouten == 9:
        #Been #2
        turtle.left(90)
        turtle.forward(20)
        turtle.back(20)

        #Het woord "Helaas"
        turtle.speed(100)
        turtle.penup()
        turtle.right(45)
        turtle.forward(200)
        turtle.right(90)
        turtle.forward(150)
        turtle.pendown()

        #H
        turtle.left(90) 
        turtle.forward(50)
        turtle.back(25)
        turtle.left(90)
        turtle.forward(15)
        turtle.right(90)
        turtle.forward(25)
        turtle.back(50)
        turtle.penup()
        turtle.left(90)
        turtle.forward(25)
        turtle.pendown()

        #E
        turtle.forward(20) 
        turtle.back(20)
        turtle.right(90)
        turtle.forward(50)
        turtle.back(25)
        turtle.left(90)
        turtle.forward(20)
        turtle.back(20)
        turtle.right(90)
        turtle.forward(25)
        turtle.left(90)
        turtle.forward(20)
        turtle.penup()
        turtle.forward(25)
        turtle.left(90)
        turtle.forward(50)
        turtle.right(180)
        turtle.pendown()

        #L
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(20)
        turtle.penup()
        turtle.forward(37.5)
        turtle.left(90)
        turtle.forward(50)
        turtle.pendown()

        #A
        turtle.right(204.6)
        turtle.forward(55.07958)
        turtle.back(55.07958)
        turtle.left(49.6)
        turtle.forward(55.07958)
        turtle.back(55.07958 / 2)
        turtle.right(114.6)
        turtle.forward(23.10324)
        turtle.back(23.10324 / 2)
        turtle.penup()
        turtle.right(90)
        turtle.forward(25)
        turtle.right(90)
        turtle.forward(50)
        turtle.pendown()

        #A
        turtle.right(114.6)
        turtle.forward(55.07958)
        turtle.back(55.07958)
        turtle.left(49.6)
        turtle.forward(55.07958)
        turtle.back(55.07958 / 2)
        turtle.right(114.6)
        turtle.forward(23.10324)
        turtle.back(23.10324 / 2)
        turtle.penup()
        turtle.right(90)
        turtle.forward(25)
        turtle.right(90)
        turtle.forward(62.5)
        turtle.right(180)
        turtle.pendown()

        #S
        turtle.forward(16.67)
        turtle.circle(8.33,90)
        turtle.forward(8.33)
        turtle.circle(8.33,90)
        turtle.forward(8.33)
        turtle.circle(-8.33,90)
        turtle.forward(8.33)
        turtle.circle(-8.33, 90)
        turtle.forward(16.67)
        turtle.penup()
        turtle.right(90)
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(45)
        turtle.pendown()

        #!
        turtle.right(90)
        turtle.forward(35)
        turtle.left(90)
        turtle.forward(10)
        turtle.left(90)
        turtle.forward(35)
        turtle.left(90)
        turtle.forward(10)
        turtle.penup()
        turtle.left(90)
        turtle.forward(45)
        turtle.pendown() 
        turtle.circle(5)

        #Pijltje van het scherm krijgen
        turtle.penup() 
        turtle.forward(150)

#Hiermee kun je het hele woord raden als je "woord" intypt tijdens het raden van letters
def hele_woord_raden(ingevoerde_woord_lijst, fouten, aantal_fouten_over, maximale_fouten, woord_ingevoerd, goede_woord_lijst, alfabet_lijst):
  while woord_ingevoerd == False:
    ingevoerd_woord = input("typ het woord dat je wil raden: ")
    ingevoerd_woord = ingevoerd_woord.replace("\n", "")
    ingevoerde_woord_lijst[:0] = ingevoerd_woord
    for x in ingevoerde_woord_lijst:
      if x not in alfabet_lijst:
        print("Dat is geen geldig woord, probeer het opnieuw.")
        return(ingevoerde_woord_lijst, fouten, aantal_fouten_over, maximale_fouten, woord_ingevoerd, goede_woord_lijst)
      elif x in alfabet_lijst:
        woord_ingevoerd = True

  #het woord dat je intypt wordt omgezet tot een lijst, die hier wordt vergeleken met de lijst waar het goede woord instaat
  if ingevoerde_woord_lijst == goede_woord_lijst:
    print(ingevoerde_woord_lijst)
    return(True)

  #Als het woord fout is wordt de lijst weer leeggemaakt, anders stapelen de woorden op in de lijst, en klopt het vergelijken niet meer
  else:
    fouten += 1
    aantal_fouten_over = maximale_fouten - fouten
    ingevoerde_woord_lijst.clear()
    print("Helaas, dat was niet het goede woord.")
    print("Je mag nog " + str(aantal_fouten_over) + " fouten maken.")
    print("\n")
    galg_tekening(fouten)
    return(False)

#Hiermee kun je kiezen hoe moeilijk het woord is, als je voor de algemene lijst hebt gekozen
def woord_niveaus(niveau_gekozen):
    gekozen_woord = str()
    bestand = open("algemene_woordenlijst.txt", "r")

    #Deze while loop blijft lopen tot er een geldig antwoord is gekozen, zodat het programma niet crashed als je wat anders invult
    while niveau_gekozen == False:
      niveau = input("Kies een moeilijkheidsniveau van 1 (makkelijk) tot 4 (moeilijk): ")

      #om een random woord te kiezen wordt er een random nummer gepakt tussen bepaalde waarden die overeenkomen met de woorden van het gekozen niveau
      if niveau == "1":
          index = random.randint(1, 6)
          niveau_gekozen = True

      elif niveau == "2":
          index = random.randint(9, 14)
          niveau_gekozen = True

      elif niveau == "3":
          index = random.randint(17, 21)
          niveau_gekozen = True

      elif niveau == "4":
          index = random.randint(24, 35)
          niveau_gekozen = True

      else:
        print("Hmm, er is iets fout gegaan met invoeren van het niveau, probeer het even opnieuw.")
    
    te_lezen_lines = [index]

    #als het random nummer is gekozen wordt hiermee het woord gekozen
    for positie, line in enumerate(bestand):
      if positie in te_lezen_lines:
            gekozen_woord = line

    bestand.close()
    return(gekozen_woord)

################
# HOOFDPROGRAMMA
################

print("Welkom")
print("We gaan galgje spelen, het werkt zo:")
print("Je kan eerst kiezen of je zelf een woord wil bedenken, of er een willekeurig woord wordt gekozen uit een lijst die ik heb gemaakt.")
print("Als je zelf een woord hebt ingevuld wordt de terminal leeg gemaakt, zodat de andere speler het woord niet ziet.")
print("Het doel van het spel is om het geheime woord te raden voor de tekening van de galg compleet is.")
print("Dit doe je door 1 voor 1 een letter in te vullen.")
print("Veel plezier!")
if maximale_fouten == 9:
  galg_tekening(fouten)

gekozen_woord = woordtype_kiezen(lijst_gekozen, extern_gekozen, woord_toegevoegd)

#Hiermee worden de streepjes getekend die je ziet met spelen.
for x in gekozen_woord:
  gekozen_woord_lijst.append("_")

gekozen_woord_naar_lijst(gekozen_woord)

#Zolang spel_afgelopen False is, blijft het spel lopen
while spel_afgelopen == False:
  spel_afgelopen, fouten = letters_raden(ingevoerde_letter, goede_woord_lijst, gekozen_woord_lijst, maximale_fouten, aantal_fouten_over, fouten, woord_ingevoerd, alfabet_lijst)

#Als het aantal fouten gelijk is aan het aantal maximale fouten dat je mag maken is, heb je verloren
if fouten == maximale_fouten:
  print("Helaas, je hebt verloren. Probeer het opnieuw door het programma nog een keer te runnen.")
  print("Het geheime woord was: " + gekozen_woord)
  print("Dankjewel voor het spelen!")
  #Dit zorgt ervoor dat de turtle niet gelijk weggaat, bij turtle.done() of turtle.mainloop() loopt het vast
  turtle.speed(1)
  turtle.forward(2000)

#Als het aantal gemaakte fouten niet gelijk is aan het aantal maximale fouten heb je gewonnen
elif fouten != maximale_fouten:
  print("Gefeliciteerd! Je hebt gewonnen!")
  print("Het geheime woord was: " + gekozen_woord)
  print("Dankjewel voor het spelen!")