import random
# karakterler
karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
# uzunluk
parola_uzunlugu = int(input("Parolanın uzunluğunu girin: "))
# şifre
parola = ""
#random
for _ in range(parola_uzunlugu):
    rastgele_karakter = random.choice(karakterler)
    parola += rastgele_karakter
# konsola yazdırma
print("Oluşturulan parola:", parola)