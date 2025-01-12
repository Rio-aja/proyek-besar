# Data Array
menu_roti = [
    ["Roti Tawar", 10000, 20],
    ["Roti Coklat", 12000, 15],
    ["Roti Keju", 15000, 10],
    ["Roti Gandum", 20000, 8],
    ["Donat", 2000, 5] 
]

# Data Distribusi menggunakan Graph
# Format: {"Region": {"Item": jumlah}}
distribusi = {}

# Fungsi untuk menampilkan menu
def tampilkan_menu():
    print("Menu Roti Toko:")
    for i, roti in enumerate(menu_roti):
        print(f"{i+1}. {roti[0]} - Harga: Rp{roti[1]}, Stok: {roti[2]}")

# Untuk mencari nama roti 
def cari_roti(nama):
    for i, roti in enumerate(menu_roti):
        if roti[0].lower() == nama.lower():
            return i
    return -1

# Fungsi untuk membeli roti
def beli_roti(nama, jumlah):
    indeks = cari_roti(nama)
    if indeks == -1:
        print(f"Roti {nama} tidak ditemukan.")
        return
    if menu_roti[indeks][2] >= jumlah:
        total_harga = menu_roti[indeks][1] * jumlah
        menu_roti[indeks][2] -= jumlah
        print(f"Anda membeli {jumlah} {nama}. Total harga: Rp{total_harga}")
    else:
        print(f"Stok {nama} tidak mencukupi.")

# Fungsi untuk mengurutkan roti berdasarkan harga shorting (bubble sort)
def urutkan_roti():
    n = len(menu_roti)
    for i in range(n):
        for j in range(0, n-i-1):
            if menu_roti[j][1] > menu_roti[j+1][1]:
                menu_roti[j], menu_roti[j+1] = menu_roti[j+1], menu_roti[j]

# Fungsi untuk mendistribusikan stok ke wilayah tertentu
def distribusi_stok(region, nama, jumlah):
    indeks = cari_roti(nama)
    if indeks == -1:
        print(f"Roti {nama} tidak ditemukan.")
        return
    if menu_roti[indeks][2] >= jumlah:
        menu_roti[indeks][2] -= jumlah
        if region not in distribusi:
            distribusi[region] = {}
        if nama in distribusi[region]:
            distribusi[region][nama] += jumlah
        else:
            distribusi[region][nama] = jumlah
        print(f"{jumlah} {nama} berhasil didistribusikan ke {region}.")
    else:
        print(f"Stok {nama} tidak mencukupi untuk distribusi.")

# Fungsi untuk menampilkan distribusi stok
def tampilkan_distribusi():
    if not distribusi:
        print("Belum ada distribusi yang dilakukan.")
        return
    print("Status Distribusi:")
    for region, items in distribusi.items():
        print(f"Wilayah: {region}")
        for item, jumlah in items.items():
            print(f"  - {item}: {jumlah}")

# Fungsi alur utama program untuk menampilkan menu
def main():
    while True:
        print("\n==== Toko Roti ====")
        print("1. Tampilkan Menu Roti")
        print("2. Cari Roti")
        print("3. Beli Roti")
        print("4. Urutkan Menu Berdasarkan Harga")
        print("5. Distribusikan Stok ke Wilayah")
        print("6. Tampilkan Status Distribusi")
        print("7. Keluar")

        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            tampilkan_menu()
        elif pilihan == "2":
            nama = input("Masukkan nama roti yang dicari: ")
            indeks = cari_roti(nama)
            if indeks != -1:
                roti = menu_roti[indeks]
                print(f"{roti[0]} - Harga: Rp{roti[1]}, Stok: {roti[2]}")
            else:
                print(f"Roti {nama} tidak ditemukan.")
        elif pilihan == "3":
            nama = input("Masukkan nama roti yang ingin dibeli: ")
            jumlah = int(input("Masukkan jumlah: "))
            beli_roti(nama, jumlah)
        elif pilihan == "4":
            urutkan_roti()
            print("Menu berhasil diurutkan berdasarkan harga!")
            tampilkan_menu()
        elif pilihan == "5":
            region = input("Masukkan nama wilayah: ")
            nama = input("Masukkan nama roti yang ingin didistribusikan: ")
            jumlah = int(input("Masukkan jumlah: "))
            distribusi_stok(region, nama, jumlah)
        elif pilihan == "6":
            tampilkan_distribusi()
        elif pilihan == "7":
            print("Terima kasih telah menggunakan sistem Toko Roti!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

main()