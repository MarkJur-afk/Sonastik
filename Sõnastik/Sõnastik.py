from SonastikModule import *

print ("Tere tulemast sõnastikku!")

while True:
    print("\nVali:")
    print("1 - Tolgib eesti to vene")
    print("2 - Tolgib vene to eesti")
    print("3 - Lisada uue sona")
    print("4 - Parandada sona")
    print("5 - Kontrollida teadet")
    print("6 - Valja")    

    choice = input("Teie valik: ")

    if choice == "1":
        word = input("Kirjutage sona eesti keeles").strip()
        print("Tolg vene keele:", tolgi_est_rus(word))

    elif choice == "2":
        word = input("Kirjutage sona vene keeles: ").strip()
        print("Tolginud sona:", tolgi_rus_est(word))

    elif choice == "3":
        est = input("Kirjutage uus sona eesti keeles: ").strip()
        rus = input("Kirjutage uus sona vene keeles: ").strip()
        print(lisa_sona(est, rus))

    elif choice == "4":
        old = input("Kirjutage vana sona eesti keeles: ").strip()
        new_est = input("Kirjutage uus sona eesti keeles: ").strip()
        new_rus = input("Kirjutage uus sona vene keeles: ").strip()

    elif choice == "5":
        testi_teadmisi()

    elif choice == "6":
        print("Head aega!")
        break

    else:
        print("Vaale kood, proovi kirjutega uuesti")
