print("1. feladat: Az adatok beolvasása.")
filepath = "valaszok.txt"
fileobject = open(filepath, "r")
competitors = -1  # a helyes válaszok sor miatt
for line in fileobject:
    competitors = competitors + 1
print("2. feladat: A versenyen", competitors, "versenyző indult.")
identities = input("3. feladat: Kérem adja meg a versenyző azonosítóját:")
if identities in fileobject:
    print("A válaszok")
else:
    print("Ilyen kóddal nem indult versenyző.")
megoldas = "BCCCDBBBBCDAAA"
print("4. feladat: A helyes megoldás:\n", megoldas)
while line in fileobject:
    if identities == megoldas:
        print('+')
    elif identities != megoldas:
        print('-')
number = input("5. feladat: Kérem adja meg a feladat sorszámát:")
students = 0
try:
    for line in fileobject:
        for character in line:
            if character != number:
                students + 1
            else:
                students + 0
except ValueError:
    print("A megadott érték helytelen!")
print(students)
percentage = students / (competitors + 1)
print("A feladatra,", students, f"fő, a versenyzők {percentage:.2%} %-a adott helyes választ.")
print("6. feladat: A versenyzők pontszámának meghatározása.")
list_of_three_points = []
list_of_four_points = []
list_of_five_points = []
list_of_three_points = []
stop = False
feladat = 0
three = 0
four = 0
five = 0
six = 0
while not stop:
    try:
        if 1 <= feladat <= 5:
            three + 1
        elif 6 <= feladat <= 10:
            four + 1
        elif 11 <= feladat <= 13:
            five + 1
        elif 14 <= feladat:
            six + 1
        else:
            stop = True
    except ValueError:
        print("A megadott érték helytelen!")
print("7. feladat: A verseny legjobbjai:")
point_of_first = 0
point_of_second = 0
point_of_third = 0
id_of_first = ""
id_of_second = ""
id_of_third = ""
print("1. díj (", point_of_first, "): ", id_of_first)
print("2. díj (", point_of_second, "): ", id_of_second)
print("3. díj (", point_of_third, "): ", id_of_third)
fileobject.close()
