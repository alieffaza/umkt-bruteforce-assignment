# Input
n = 5 # Jumlah desa
waktuKunjungan = [5, 1, 2, 5, 6]
banyakChakra = [
    [0, 2, 4, 6, 8],
    [2, 0, 3, 5, 7],
    [4, 3, 0, 7, 2],
    [6, 5, 7, 0, 1],
    [8, 7, 2, 1, 0]
]
batasWaktu = 20
totalChakra = 15

# Jutsu untuk menghitung total waktu dan chakra untuk satu kunjungan desa
def konsumsiChakra(urutanDesa, waktuKunjungan, banyakChakra):
    totalWaktu = 0
    totalChakra = 0
    for i in range(len(urutanDesa) - 1):
        totalWaktu += waktuKunjungan[urutanDesa[i]]
        totalChakra += banyakChakra[urutanDesa[i]][urutanDesa[i + 1]]
    totalWaktu += waktuKunjungan[urutanDesa[-1]]
    return totalWaktu, totalChakra

# Misi untuk mencari urutan desa terbaik menggunakan permutasi no jutsu
def misiRahasia(n, waktuKunjungan, banyakChakra, batasWaktu, totalChakra):
    daftarDesa = list(range(n))
    urutanDesa_terbaik = None
    waktuTerkecil = float('inf')
    chakraTerkecil = float('inf')
    statusMisi = False

    def jurusPermutasi(path, desaTersedia):
        nonlocal urutanDesa_terbaik, waktuTerkecil, chakraTerkecil, statusMisi

        if not desaTersedia:
            totalWaktu, totalChakra_dibutuhkan = konsumsiChakra(path, waktuKunjungan, banyakChakra)
            if totalWaktu <= batasWaktu and totalChakra_dibutuhkan <= totalChakra:
                statusMisi = True
                if totalWaktu < waktuTerkecil or (totalWaktu == waktuTerkecil and totalChakra_dibutuhkan < chakraTerkecil):
                    urutanDesa_terbaik = path[:]
                    waktuTerkecil = totalWaktu
                    chakraTerkecil = totalChakra_dibutuhkan
            return

        for i in range(len(desaTersedia)):
            next_desa = desaTersedia[i]
            jurusPermutasi(path + [next_desa], desaTersedia[:i] + desaTersedia[i+1:])

    # Memulai permutasi no jutsu dari desa pertama dan menggunakan semua desa yang tersedia
    jurusPermutasi([], daftarDesa)
    
    return urutanDesa_terbaik, waktuTerkecil, chakraTerkecil, statusMisi

# Menjalankan fungsi brute force no jutsu untuk misi rahasia
urutanDesa_terbaik, waktuTerkecil, chakraTerkecil, berhasil = misiRahasia(n, waktuKunjungan, banyakChakra, batasWaktu, totalChakra)

# Output hasil dari misi rahasia tersebut
if berhasil:
    print("- Urutan desa terbaik:", urutanDesa_terbaik)
    print("- Total waktu yang dihabiskan:", waktuTerkecil, "jam")
    print("- Total chakra yang terpakai:", chakraTerkecil, "chakra dari", totalChakra, "chakra")
    print("- Status misi : Misi berhasil diselesaikan, anda dipromosikan menjadi jounin.")
else:
    print("- Status misi : Misi anda gagal, anda diasingkan dari desa!")
    