import random

print("^^^\Permainan Tebak Angka/^^^")
print("masukkan angka 1-100.")

angka_rahasia = random.randint(1, 100)
percobaan = 0

while True:
    try:
        tebakan = int(input("Masukkan tebakanmu: "))
        percobaan += 1

        if tebakan < angka_rahasia:
            print("Terlalu kecil!")
        elif tebakan > angka_rahasia:
            print("Terlalu besar!")
        else:
            print(f"Benar! Angkanya adalah {angka_rahasia}.")
            print(f"Kamu berhasil menebak dalam {percobaan} percobaan.")
            break
    except ValueError:
        print("Masukkan angka yang valid!")

