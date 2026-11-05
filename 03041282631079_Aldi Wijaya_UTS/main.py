# data arus dalam ampere
data_arus_utama = [1.6, 2.2, 3.5, 4.1, 5.4, 2.8, 6.0, 3.9, 1.9, 4.8, 5.1, 2.6, 3.2, 4.4, 5.8]
data_arus_tambahan = [3.18, 3.19, 4.54, 4.55, 10.0]
V = 220  # tegangan dalam volt
data_arus = data_arus_utama + data_arus_tambahan
data_daya = []
kategori_count = {"NORMAL": 0, "WARNING": 0, "BEBAN TINGGI": 0}

def hitung_daya(V, I): 
    return V * I

def status_beban(P):
    if P <= 700:
        return "NORMAL"
    elif 700 < P <= 1000:
        return "WARNING"
    else:
        return "BEBAN TINGGI"

def rata_rata(data):
    total = 0
    for nilai in data:
        total += nilai
    return total / len(data)


print("===== MONITORING DAYA =====")

for i in range(len(data_arus)):
        I = data_arus[i]
        P = hitung_daya(V, I)
        data_daya.append(P) 
        status = status_beban(P)
        kategori_count[status] += 1
        print(f"{i+1:02d} Arus: {I:5.2f} A, Daya: {P:7.2f} W -> {status}")

hasil_rata = rata_rata(data_daya)
maksimum = max(data_daya)
minimum = min(data_daya)

print("\n===== RINGKASAN =====")
print(f"Total data     : {len(data_arus)}")
print(f"NORMAL         : {kategori_count['NORMAL']}")
print(f"WARNING        : {kategori_count['WARNING']}")
print(f"BEBAN TINGGI   : {kategori_count['BEBAN TINGGI']}")
print(f"Rata-rata Daya : {hasil_rata:.2f} W")
print(f"Maksimum Daya  : {maksimum:.2f} W")
print(f"Minimum Daya   : {minimum:.2f} W")