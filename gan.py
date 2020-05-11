#pakai modul random gan ya :)
import random
#banner
print("    __  __           ______              ")
print("   / / / /___ __  __/ ____/__  _____     ")
print("  / /_/ / __ `/ |/_/ / __/ _ \/ __  /    ")
print(" / __  / /_/ />  </ /_/ /  __/ / / /     ")
print("/_/ /_/\__,_/_/|_|\____/\___/_/ /_/v1.0  ")
print("+++ Simple Andre Haxor Code Generator +++")
print()
                                    
teks  = input("Masukkan teks nya gan ya 🙂 : ") #input dulu data gan ya :)
haxor = ['🙂','gan','gaaan ya',''] #tambahan kata lord haxor disini gan ya :)
hasil = teks.split(' ')
for hitung, kata in enumerate(hasil):
	hasil[hitung] = kata + ' ' + random.choice(haxor)
print("hasilnya gan ya 🙂 : ",*hasil)
