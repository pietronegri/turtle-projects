########################POLIGONO REGOLARE#####################
### II A Tecnico IoC Parmenide Roccadaspide (SA)
#*#*#*#*#!!!!!RUN in https://pythonsandbox.com/turtle#*!!!!#
#Struttura base programma 1. + 2. + 3.

############___1. Importo il CODICE SCRITTO DA ALTRI 
import turtle
############___2. Definisco le VARIABILI
numero_lati=12 #numero lati poligono regolare
lunghezza_lato=40 #lunghezza singolo lato 
t=turtle.Turtle() #N.B. rispettare maiuscole e minuscole

############___3. Scrivo il MIO CODICE 
######così implemento algoritmo e risolvo problema 
######uso SOLO variabili e valori fissi e noti
######(es. 360 per angolo giro)
alfa=360/numero_lati 
#la tartaruga fa un giro completo (360 gradi) 
#un numero di volte pari a "numero_lati"
#CICLO FOR, vantaggio: evito ripetizione istruzioni inutili
for i in range(numero_lati) : ######___ NOTARE I due punti ":"
	#INDENTARE istruzioni da ripetere!
  t.forward(lunghezza_lato) #lato di lunghezza "lunghezza_lato"
  t.right(alfa) #ruoto di alfa
  #N.B. 180-alfa= angolo interno del poligono. 
  #N.B. il FOR ripete istruzioni un numero di volte pari a 
  ##numero_lati
