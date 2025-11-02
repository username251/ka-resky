a = int(input("Masukkan Nilai ujian A: "))
b = int(input("Masukkan Nilai ujian B: "))


rata_rata = (a + b) / 2

print('nilai ujian A: ', a)
print('nilai ujian B: ', b)
print('nilai rata-rata: ', rata_rata)

if a > 80 and b > 80:
    print("status: Lulus")
else:
    print("status: Tidak lulus")
