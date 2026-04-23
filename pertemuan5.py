
data_gejala = {
    "G1": "Nafas abnormal", "G2": "Suara serak", "G3": "Perubahan kulit", 
    "G4": "Telinga penuh", "G5": "Nyeri bicara menelan", "G6": "Nyeri tenggorokan", 
    "G7": "Nyeri leher", "G8": "Pendarahan hidung", "G9": "Telinga berdenging", 
    "G10": "Airliur menetes", "G11": "Perubahan suara", "G12": "Sakit kepala", 
    "G13": "Nyeri pinggir hidung", "G14": "Serangan vertigo", "G15": "Getah bening", 
    "G16": "Leher bengkak", "G17": "Hidung tersumbat", "G18": "Infeksi sinus", 
    "G19": "Beratbadan turun", "G20": "Nyeri telinga", "G21": "Selaput lendir merah", 
    "G22": "Benjolan leher", "G23": "Tubuh tak seimbang", "G24": "Bolamata bergerak", 
    "G25": "Nyeri wajah", "G26": "Dahi sakit", "G27": "Batuk", 
    "G28": "Tumbuh dimulut", "G29": "Benjolan dileher", "G30": "Nyeri antara mata", 
    "G31": "Radang gendang telinga", "G32": "Tenggorokan gatal", "G33": "Hidung meler", 
    "G34": "Tuli", "G35": "Mual muntah", "G36": "Letih lesu", "G37": "Demam"
}


data_penyakit = {
    "Tonsilitis": ["G37", "G12", "G5", "G27", "G6", "G21"],
    "Sinusitis Maksilaris": ["G37", "G12", "G27", "G17", "G33", "G36", "G29"],
    "Sinusitis Frontalis": ["G37", "G12", "G27", "G17", "G33", "G36", "G21", "G26"],
    "Sinusitis Edmoidalis": ["G37", "G12", "G27", "G17", "G33", "G36", "G21", "G30", "G13", "G26"],
    "Sinusitis Sfenoidalis": ["G37", "G12", "G27", "G17", "G33", "G36", "G29", "G7"],
    "Abses Peritonsiler": ["G37", "G12", "G6", "G15", "G2", "G29", "G10"],
    "Faringitis": ["G37", "G5", "G6", "G7", "G15"],
    "Kanker Laring": ["G5", "G27", "G6", "G15", "G2", "G19", "G1"],
    "Deviasi Septum": ["G37", "G17", "G20", "G8", "G18", "G25"],
    "Laringitis": ["G37", "G5", "G15", "G16", "G32"],
    "Kanker Leher & Kepala": ["G5", "G22", "G8", "G28", "G3", "G11"],
    "Otitis Media Akut": ["G37", "G20", "G35", "G31"],
    "Contact Ulcers": ["G5", "G2"],
    "Abses Parafaringeal": ["G5", "G16"],
    "Barotitis Media": ["G12", "G20"],
    "Kanker Nafasoring": ["G17", "G8"],
    "Kanker Tonsil": ["G6", "G29"],
    "Neuronitis Vestibularis": ["G35", "G24"],
    "Meniere": ["G20", "G35", "G14", "G4"],
    "Tumor Syaraf Pendengaran": ["G12", "G34", "G23"],
    "Kanker Leher Metastatik": ["G29"],
    "Osteosklerosis": ["G34", "G9"],
    "Vertigo Postular": ["G24"]
}

def tampilkan_gejala():
    print("\n--- DAFTAR GEJALA ---")
    for kode, nama in data_gejala.items():
        print(f"{kode} : {nama}")
    print("---------------------\n")

def diagnosa(input_gejala_user):
    hasil_diagnosa = []
    
    
    for penyakit, gejala_penyakit in data_penyakit.items():
      
        if all(g in input_gejala_user for g in gejala_penyakit):
            hasil_diagnosa.append(penyakit)
            
    return hasil_diagnosa

def main():
    print("Selamat datang di Sistem Pakar Diagnosa Penyakit THT")
    tampilkan_gejala()
    
   
    input_user = input("Masukkan kode gejala yang Anda alami (pisahkan dengan koma, cth: G37,G12,G5,G27,G6,G21): ")
    
    
    gejala_user = [g.strip().upper() for g in input_user.split(',')]
    
    
    gejala_valid = [g for g in gejala_user if g in data_gejala]
    
    if not gejala_valid:
        print("\n[!] Tidak ada kode gejala yang valid dimasukkan.")
        return

    print("\nGejala yang Anda alami:")
    for g in gejala_valid:
        print(f"- {data_gejala[g]}")
        
    print("\nSedang memproses diagnosa...")
    
    hasil = diagnosa(gejala_valid)
    
    print("\n--- HASIL DIAGNOSA ---")
    if hasil:
        print("Berdasarkan gejala tersebut, Anda kemungkinan mengalami:")
        for h in hasil:
            print(f"=> {h}")
    else:
        print("Sistem tidak dapat menemukan penyakit yang cocok dengan kombinasi gejala tersebut secara spesifik.")
        print("Saran: Periksa kembali gejala yang dimasukkan atau segera hubungi dokter THT.")

if __name__ == "__main__":
    main()