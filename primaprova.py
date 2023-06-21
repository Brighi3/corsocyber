'''print("Ciao da Michele")
print(2+2)
print(6-2)
print(2*2)
print(8/2)
print(4 % 2)
print("Ciao", "da Michele")
print(5 > 2)
print(5 > 15)
condizione = 5 > 5
print(condizione)
condizione1 = 5 > 5
if condizione == condizione1:
    print("sono entrambi ", condizione)
else:
    print("sono diversi")

nome = "Michele"
anni = 30
print(nome, " ", anni)
var2 = input("Inserisci un valore")
print("Hai inserito", var2)
print("Il valore x10 senza cast è ", var2*10)
var3 = int(var2)
print("Il valore x10 con cast è ", var3*10)'''


'''nom1 = input("Inserisci il tuo nome")
eta = input("Inserisci i tuoi anni")
print("Ciao ", nom1, "! Hai ", eta, " anni e fra 10 anni ne avrai", int(eta)+10)'''

'''utente = "Michele"
utpw = "12345"
nom1 = input("Inserire nome utente")
pw = input("Inserire password")
if nom1 == utente and pw == utpw:
    print("Login effettuato")
elif nom1 == utente:
    print("Password errata")
else:
    print("Accesso vietato: utente inesistente")'''

'''list1 = []
list1.append(input("Inserire 1° elemento"))
list1.append(input("Inserire 2° elemento"))
list1.append(input("Inserire 3° elemento"))
list1.append(input("Inserire 4° elemento"))
print(list1)'''

'''base = int(input("Inserisci la base "))
altezza = int(input("Inserisci l'altezza "))
area = base * altezza
perim = (base + altezza) * 2
print("L'area è ", area, " mentre il perimetro è ", perim)'''

'''val1=int(input("Inserisci valore 1 "))
val2=int(input("Inserisci valore 2 "))
print("La somma è ", val1+val2, " mentre il prodotto è", val1*val2)'''

'''val1 = int(input("Inserisci il valore 1 "))
val2 = int(input("Inserisci il valore 2 "))
val3 = int(input("Inserisci il valore 3 "))
if val1 > val2 and val1 > val3: print("Il valore più grande è", val1)
elif val2 > val3: print("Il valore più grande è", val2)
else: print("Il valore più grande è", val3)'''

'''crescente = []
val1 = int(input("Inserisci il valore 1 "))
val2 = int(input("Inserisci il valore 2 "))
val3 = int(input("Inserisci il valore 3 "))
if val1 <= val2 and val1 <= val3:
    crescente.append(val1)
    if val2 <= val3:
        crescente.append(val2)
        crescente.append(val3)
    else:
        crescente.append(val3)
        crescente.append(val2)
elif val2 <= val1 and val2 <= val3:
    crescente.append(val2)
    if val1 <= val3:
        crescente.append(val1)
        crescente.append(val3)
    else:
        crescente.append(val3)
        crescente.append(val1)
elif val3 <= val1 and val3 <= val2:
    crescente.append(val3)
    if val2 <= val1:
        crescente.append(val2)
        crescente.append(val1)
    else:
        crescente.append(val1)
        crescente.append(val2)
print(crescente)'''

'''lista = [1,2,3,4]
c = 0
while c < len(lista):
    print(lista[c])
    c = c+1'''

'''temperature, il programma chiede di inserire delle temperature climatiche e le registra in una lista,
successivamente viene stampata la media delle temperature'''

'''templ = []
ntemp = int(input("Inserisci il numero di temperature "))
i = 0
media = 0
for i in range(ntemp):
    templ.append(float(input("Inserisci la temperatura ")))
    media= media+templ[i]
media = media/ntemp
print("La media è: ", media)
for i in templ:
    if i < media: print(i, " è inferiore alla media")
    elif i == media: print(i, " è nella media")
    else: print(i, " è superiore alla media")'''

def guess_password(dictionary, password):
    for word in dictionary:
        if word == password:
            print(f"Password trovata: {word}")
        else:
            print(f"Password non trovata: {word}")

# Creazione del dizionario di parole
dictionary = [
    "ciao",
    "mela",
    "gatto",
    "sole",
    "mare",
    "rosso123",
    "verde",
    "blu",
    "casa",
    "amore",
    # Aggiungi altre parole al dizionario
]

# Password da indovinare
password = "rosso123"

# Tentativo di indovinare la password
guess_password(dictionary, password)
