
import streamlit as st

def siswa_remedial(nilai_siswa):
    """
    Menerima dictionary dengan format {nama: nilai},
    mengembalikan list nama siswa yang nilainya di bawah KKM.
    """
    KKM = 70
    remedial = [nama for nama, nilai in nilai_siswa.items() if nilai < KKM]
    return remedial

st.title("Remedial Siswa Informatika")
st.write("Masukkan nama dan nilai siswa. Siswa dengan nilai di bawah KKM (70) akan remedial.")

data_nilai = {}
jumlah = st.number_input("Jumlah siswa", min_value=1, step=1)

for i in range(jumlah):
    nama = st.text_input(f"Nama siswa ke-{i+1}", key=f"nama_{i}")
    nilai = st.number_input(f"Nilai {nama if nama else 'siswa ke-'+str(i+1)}", min_value=0, max_value=100, key=f"nilai_{i}")
    if nama:
        data_nilai[nama] = nilai

if st.button("Cek Remedial"):
    siswa_perlu_remedial = siswa_remedial(data_nilai)
    if siswa_perlu_remedial:
        st.warning(f"Siswa yang harus remedial: {', '.join(siswa_perlu_remedial)}")
    else:
        st.success("Tidak ada siswa yang perlu remedial!")
