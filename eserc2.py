'''Scrivere un programma Calcolatrice che chiede all’utente di inserire due numeri interi
x e y, poi chiede di inserire un numero compreso tra 1 e 4, che servir`a per determinare che operazione
calcolare su x e y secondo la seguente mappatura
• 1 ⇒ somma
• 2 ⇒ sottrazione
• 3 ⇒ moltiplicazione
• 4 ⇒ divisione (intera)'''

val1 = int(input("Inserisci il valore 1 "))
val2 = int(input("Inserisci il valore 2 "))
val3 = int(input("Inserisci un numero tra 1 e 4 "))
if val3 == 1: print("Somma: ", val1+val2)
elif val3 == 2: print("Sottrazione: ", val1-val2)
elif val3 == 3: print("Prodotto: ", val1*val2)
elif val3 == 4: print("Divisione: ", val1/val2)
else: print("Errore: operazione inesistente")
