
# Daftar nama dan nilai siswa
data_siswa = [
    {"nama": "Andi", "nilai": 65},
    {"nama": "Budi", "nilai": 80},
    {"nama": "Cici", "nilai": 55},
    {"nama": "Dewi", "nilai": 72},
    {"nama": "Eka", "nilai": 68},
]

# Membuat pengumuman untuk siswa yang remedial
print("Pengumuman Remedial:")
for siswa in data_siswa:
    if siswa["nilai"] < 70:
        print(f"- {siswa['nama']} harus mengikuti remedial (Nilai: {siswa['nilai']})")
