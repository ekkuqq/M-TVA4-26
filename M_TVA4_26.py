#1.2 Esimene programm
print("Tere maailm")
print("Tere veel kord!")
print("Mul on", 3, "kassi") #,->" "
print("Aasta on", 2026, sep="-")

print("2026", "10", "01", sep="-")
print("sama", end="") # end="\n" =Enter, "\t"=Tab
print("rida")
#1.3 Muutujad ja omistamine
nimi="Python" #str-sõne
vanus=25 #int-täisarv
laius=3.75 #float-ujukomaarv
täna_on_koolis=True #bool-tõeväärtus

print (nimi*3)
print (nimi+nimi)
print (vanus+laius)
print (täna_on_koolis)
print (vanus+1)

kaibemaks = 0.24
hind = 100
print ("Hind koos käibemaksuga:", hind * (1+kaibemaks))
nimi=input("mis on sinu nimi ")
print(f"Tere, {nimi}")
#a ja b on tekstid
a = input("Esimene arv: ")
b = input("Teine arv: ")
print(a + b)   #a+b="2"+"5"=>"25"
a = int(input("Esimene arv: ")) #"2" int("2") ->2
b = int(input("Teine arv: "))
print(a + b)

#Aritmeetilised põhioperatsioonid
print(f"astendamine {a}**{b} ={a**b}")
print(f"korrutamine {a}*{b} ={a*b}")
print(f"jagamine {a}/{b} ={a/b}")
# jagamise täisarvuline osa
# jagamisjääk
# liitmine
# lahutamine
print(f"... {a}...{b} ={a**b}")
print(f"... {a}...{b} ={a**b}")
from time import *
from os import *   #käivitamiseks kasuta Ctrl+F5
print("valgusfoor käivitub!")
print() # tühi rida
system("cls")   # ekraani puhastus
print("Punane põleb - seisa!")
sleep(5)
system("cls")
print("punane ja kollane põlevad - valmistu!")
sleep(2)
system("cls")
print("Roheline põleb - sõida!")
sleep(5)
system("cls")
print("Kollane põleb - tähelepanu!")
sleep(2)
system("cls")
print("Valgusfoor lõpetas töö.")