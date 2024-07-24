import random

while True:
    choices = ["guri", "leter", "gershere"]

    kompjuteri = random.choice(choices)
    lojtari = None

    while lojtari not in choices:
        lojtari = input("guri , leter, ose gershere?: ").lower()

    if lojtari == kompjuteri:
        print("kompjuteri: ", kompjuteri)
        print("lojtari: ", lojtari)
        print("Barazim!")

    elif lojtari == "guri":
        if kompjuteri == "leter":
            print("kompjuteri: ", kompjuteri)
            print("lojtari: ", lojtari)
            print("Ju humbet!")
        if kompjuteri == "gershere":
            print("kompjuteri: ", kompjuteri)
            print("lojtari: ", lojtari)
            print("Ju fituat!")

    elif lojtari == "gershere":
        if kompjuteri == "guri":
            print("kompjuteri: ", kompjuteri)
            print("lojtari: ", lojtari)
            print("Ju humbet!")
        if kompjuteri == "leter":
            print("kompjuteri: ", kompjuteri)
            print("lojtari: ", lojtari)
            print("Ju fituat!")

    elif lojtari == "leter":
        if kompjuteri == "gershere":
            print("kompjuteri: ", kompjuteri)
            print("lojtari: ", lojtari)
            print("Ju humbet!")
        if kompjuteri == "guri":
            print("kompjuteri: ", kompjuteri)
            print("lojtari: ", lojtari)
            print("Ju fituat!")

    luani_perseri = input("Dëshironi të luani përseri? (Po/Jo): ").lower()

    if luani_perseri != "po":
        break

print("Mirupafshim!")
