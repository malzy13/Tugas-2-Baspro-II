# Input data pegawai
nama = input("Masukkan Nama: ")
nik = input("Masukkan NIK: ")
status = input("Masukkan Status (Pegawai Tetap/Honor): ")
golongan = input("Masukkan Golongan (A/B/C): ")

# Inisialisasi gaji dan bonus
gaji = 0
bonus = 0

# Menentukan gaji dan bonus berdasarkan status dan golongan
if status.lower() == "pegawai tetap":
    gaji = 1000000
    if golongan.upper() == "A":
        bonus = 200000
    elif golongan.upper() == "B":
        bonus = 400000
    elif golongan.upper() == "C":
        bonus = 550000
elif status.lower() == "honor":
    gaji = 750000
    if golongan.upper() == "A":
        bonus = 150000
    elif golongan.upper() == "B":
        bonus = 275000
    elif golongan.upper() == "C":
        bonus = 480000
else:
    print("Status tidak valid!")

# Menghitung total gaji
gaji_total = gaji + bonus

# Menampilkan hasil
print("\n--- Rincian Gaji ---")
print(f"Nama: {nama}")
print(f"NIK: {nik}")
print(f"Status: {status}")
print(f"Golongan: {golongan}")
print(f"Gaji Pokok: Rp{gaji:,}")
print(f"Bonus: Rp{bonus:,}")
print(f"Gaji Total: Rp{gaji_total:,}")