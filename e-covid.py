from array import *
import numpy as np

kondisi = ["Tanpa Gejala", "Gejala Ringan", "Gejala Sedang", "Gejala Berat"]

gejala = ["Muntah", "Mudah Lelah", "BAB/Diare", 
          "Pilek", "Sesak nafas", "Nyeri dada",
          "Nyeri tenggorokan", "Batuk kering",
          "Pusing/Sakit Kepala", "Bersin-bersin", "Nyeri otot dan sendi",
          "Hidung tersumbat", "Kehilangan selera makan", "Kehilangan indra pengecapan",
          "Kehilangan indra penciuman", "Kuku, bibir, dan kulit tampak pucat", 
          "Saturasi oksigen dibawah 93%", "Saturasi oksigen > 93%", "Demam > 38", "Denyut jantung tidak normal"]

pengetahuan = [["Gejala Ringan", "Muntah", 0.6, 0],
               ["Gejala Sedang", "Muntah", 0.5, 0],
               ["Gejala Berat", "Muntah", 0.5, 0],
               ["Gejala Ringan", "Mudah Lelah", 0.6, 0],
               ["Gejala Sedang", "Mudah Lelah", 0.7, 0],
               ["Gejala Berat", "Mudah Lelah", 0.7, 0],
               ["Gejala Ringan", "BAB/Diare", 0.6, 0],
               ["Gejala Sedang", "BAB/Diare", 0.7, 0],
               ["Gejala Berat", "BAB/Diare", 0.5, 0],
               ["Gejala Ringan", "Pilek", 0.6, 0],
               ["Gejala Sedang", "Pilek", 0.5, 0],
               ["Gejala Berat", "Pilek", 0.5, 0],
               ["Gejala Sedang", "Sesak nafas", 0.8, 0],
               ["Gejala Berat", "Sesak nafas", 0.9, 0],
               ["Gejala Berat", "Nyeri dada", 0.7, 0],
               ["Gejala Sedang", "Nyeri tenggorokan", 0.7, 0],
               ["Gejala Berat", "Nyeri tenggorokan", 0.8, 0],
               ["Gejala Ringan", "Batuk kering", 0.6, 0],
               ["Gejala Sedang", "Batuk kering", 0.8, 0],
               ["Gejala Berat", "Batuk kering", 0.7, 0],
               ["Gejala Ringan", "Pusing/Sakit Kepala", 0.6, 0],
               ["Gejala Sedang", "Pusing/Sakit Kepala", 0.7, 0],
               ["Gejala Berat", "Pusing/Sakit Kepala", 0.8, 0],
               ["Gejala Ringan", "Bersin-bersin", 0.6, 0],
               ["Gejala Sedang", "Bersin-bersin", 0.5, 0],
               ["Gejala Berat", "Bersin-bersin", 0.5, 0],
               ["Gejala Ringan", "Nyeri otot dan sendi", 0.6, 0],
               ["Gejala Sedang", "Nyeri otot dan sendi", 0.6, 0],
               ["Gejala Berat", "Nyeri otot dan sendi", 0.6, 0],
               ["Gejala Ringan", "Hidung tersumbat", 0.3, 0],
               ["Gejala Sedang", "Hidung tersumbat", 0.5, 0],
               ["Gejala Berat", "Hidung tersumbat", 0.5, 0],
               ["Gejala Ringan", "Kehilangan selera makan", 0.5, 0],
               ["Gejala Sedang", "Kehilangan selera makan", 0.5, 0],
               ["Gejala Berat", "Kehilangan selera makan", 0.5, 0],
               ["Gejala Sedang", "Kehilangan indra pengecapan", 0.7, 0],
               ["Gejala Berat", "Kehilangan indra pengecapan", 0.8, 0],
               ["Gejala Sedang", "Kehilangan indra penciuman", 0.6, 0],
               ["Gejala Berat", "Kehilangan indra penciuman", 0.8, 0],
               ["Gejala Berat", "Kuku, bibir, dan kulit tampak pucat", 0.6, 0],
               ["Gejala Berat", "Saturasi oksigen dibawah 93%", 0.9, 0],
               ["Gejala Sedang", "Saturasi oksigen > 93%", 0.8, 0],
               ["Gejala Berat", "Saturasi oksigen > 93%", 0.9, 0],
               ["Gejala Ringan", "Demam > 38", 0.6, 0],
               ["Gejala Sedang", "Demam > 38", 0.8, 0],
               ["Gejala Berat", "Demam > 38", 0.7, 0],
               ["Gejala Ringan", "Denyut jantung tidak normal", 0.5, 0],
               ["Gejala Sedang", "Denyut jantung tidak normal", 0.5, 0],
               ["Gejala Berat", "Denyut jantung tidak normal", 0.6, 0]]

hasil_analisa = []
analisa = [[4, 7, 8, 10, 12, 19],
           [8, 19],
           [8, 12, 19, 20],
           [2, 8, 9, 11, 14, 15, 19],
           [5, 6, 17],
           [7, 9, 11, 13, 15, 19],
           [1, 2, 8, 16, 19, 20],
           [2, 5, 6, 11, 14, 19],
           [2, 8],
           [2, 5, 19],
           [2, 5, 6, 8, 9, 11, 14, 15, 19],
           [8, 13, 15, 19],
           [4, 5, 18, 19],
           [4, 5, 19],
           [1, 2, 19],
           [2, 4, 8, 11, 15, 19],
           [1, 2, 4, 8, 11, 15, 19],
           [2, 8, 14, 19],
           [2, 5, 8, 14, 19],
           [2, 3, 4, 7, 8, 9, 13, 14, 15, 19]]

target = ["Gejala Sedang",
          "Gejala Ringan",
          "Gejala Ringan",
          "Gejala Sedang",
          "Gejala Berat",
          "Gejala Sedang",
          "Gejala Berat",
          "Gejala Berat",
          "Gejala Ringan",
          "Gejala Sedang",
          "Gejala Berat",
          "Gejala Ringan",
          "Gejala Sedang",
          "Gejala Sedang",
          "Gejala Ringan",
          "Gejala Ringan",
          "Gejala Ringan",
          "Gejala Ringan",
          "Gejala Sedang",
          "Gejala Sedang"]

akurasi  = []

for y in range(len(analisa)):
    hasil = []
    gejala_dipilih = []
    id_row_gejala = analisa[y]
    print(id_row_gejala)
    for i in range(len(id_row_gejala)):
        id_penyakit = int(id_row_gejala[i]) - 1
        gejala_dipilih.append(gejala[id_penyakit])
    print("Gejala dipilih", gejala_dipilih)

    penyakit_terpilih = []
    for i in range(len(pengetahuan)):
        for j in range(len(gejala_dipilih)):
            if(pengetahuan[i][1] == gejala_dipilih[j]):
                if(pengetahuan[i][0] not in penyakit_terpilih):
                    penyakit_terpilih.append(pengetahuan[i][0])
    print("Penyakit Terpilih", penyakit_terpilih)

    list_cf = []
    for i in range(len(penyakit_terpilih)):
        print("==== " + penyakit_terpilih[i] + " ==== ")
        jmlpengetahuan = 0
        pengetahuanke = 0
        for j in range(len(pengetahuan)):
            if(pengetahuan[j][0] == penyakit_terpilih[i]) and (pengetahuan[j][1] in gejala_dipilih):
                jmlpengetahuan = jmlpengetahuan + 1
        mblama = 0
        mdlama = 0
        for j in range(len(pengetahuan)):
            if(pengetahuan[j][0] == penyakit_terpilih[i]) and (pengetahuan[j][1] in gejala_dipilih): 
                pengetahuanke = pengetahuanke + 1
                if (jmlpengetahuan == 1):
                    mb = pengetahuan[j][2]
                    md = pengetahuan[j][3]
                    cf = mb - md
                    print("mb = ", mb)
                    print("md = ", md)
                    print("cf = mb - md = ", mb, " - ", md, " = ", cf)
                    list_cf.append(cf)
                
                elif (jmlpengetahuan > 1):
                    if (pengetahuanke == 1):
                        mblama = pengetahuan[j][2]
                        mdlama = pengetahuan[j][3]
                        print("mblama = ", mblama)
                        print("mdlama = ", mdlama)
                    elif (pengetahuanke == 2):
                        mbbaru = pengetahuan[j][2]
                        mdbaru = pengetahuan[j][3]
                        mbsementara = (mblama + mbbaru) * (1 - mblama)
                        mdsementara = (mdlama + mdbaru) * (1 - mdlama)
                        print("mbsementara = (mblama + mbbaru) * (1 - mblama)")
                        print("            = (", mblama, " + ", mbbaru, ") * (1 - ", mblama, ")")
                        print("            = ", mbsementara)
                        print("mdsementara = (mdlama + mdbaru) * (1 - mdlama)")
                        print("            = (", mdlama, " + ", mdbaru, ") * (1 - ", mdlama, ")")
                        print("            = ", mdsementara)
                        if (jmlpengetahuan == 2):
                            mb = mbsementara
                            md = mdsementara
                            cf = mb - md
                            print("mb = mbsementara = ", mb)
                            print("md = mdsementara = ", md)
                            print("cf = mb - md = ", mb, " - ", md, " = ", cf)
                            list_cf.append(cf)
                    elif (pengetahuanke >= 3):
                        mblama = mbsementara
                        mdlama = mdsementara
                        print("mblama = mbsementara = ", mblama)
                        print("mdlama = mdsementara = ", mdlama)
                        mbbaru = pengetahuan[j][2]
                        mdbaru = pengetahuan[j][3]
                        mbsementara = (mblama + mbbaru) * (1 - mblama)
                        mdsementara = (mdlama + mdbaru) * (1 - mdlama)
                        print("mbsementara = (mblama + mbbaru) * (1 - mblama)")
                        print("            = (", mblama, " + ", mbbaru, ") * (1 - ", mblama, ")")
                        print("            = ", mbsementara)
                        print("mdsementara = (mdlama + mdbaru) * (1 - mdlama)")
                        print("            = (", mdlama, " + ", mdbaru, ") * (1 - ", mdlama, ")")
                        print("            = ", mdsementara)
                        if (jmlpengetahuan == pengetahuanke):
                            mb = mbsementara
                            md = mdsementara
                            cf = mb - md
                            print("mb = mbsementara = ", mb)
                            print("md = mdsementara = ", md)
                            print("cf = mb - md = ", mb, " - ", md, " = ", cf)
                            list_cf.append(cf)
                        
    print("Penyakit Terpilih", penyakit_terpilih)
    print(list_cf)
    penyakitrangking = []
    cfrangking = []
    for i in range(len(penyakit_terpilih)):
        penyakitrangking.append(penyakit_terpilih[i])
        cfrangking.append(list_cf[i])
    for i in range(len(penyakit_terpilih)):
        for j in range(len(penyakit_terpilih)):
            if j > i:
                if cfrangking[j] > cfrangking[i]:
                    tmpcf = cfrangking[i]
                    tmppenyakit = penyakitrangking[i]
                    cfrangking[i] = cfrangking[j]
                    penyakitrangking[i] = penyakitrangking[j]
                    cfrangking[j] = tmpcf
                    penyakitrangking[j] = tmppenyakit
    print("Rangking Penyakit : ", penyakitrangking)
    print("Rangking CF : ", cfrangking)
    print("\n")
    nilai_hasil = [item for sublist in zip(penyakitrangking, cfrangking) for item in sublist]
    hasil = [gejala_dipilih, target[y], nilai_hasil]
    hasil_analisa.append(hasil)
    if penyakitrangking[0] == target[y]:
        nilai_akurasi = 1
    else:
        nilai_akurasi = 0
    akurasi.append(nilai_akurasi)


for r in hasil_analisa:
    for c in r:
        print(c, end = "")
    print()
print("\n")

total_akurasi = sum(akurasi)

for i in range(len(akurasi)):
    print([str(i+1),akurasi[i]], end="\n")
print("\nTotal Akurasi = ", total_akurasi)
