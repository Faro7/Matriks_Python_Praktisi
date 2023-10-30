# No 1
import numpy as np

# Membuat dua matriks 3x3 menggunakan NumPy
matriks1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

matriks2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print("Matriks penjumlahan dan pengurangan")
# Operasi penjumlahan matriks
hasil_penjumlahan = np.add(matriks1, matriks2)

# Operasi pengurangan matriks
hasil_pengurangan = np.subtract(matriks1, matriks2)

# Cetak hasil penjumlahan
print(hasil_penjumlahan)

# Cetak hasil pengurangan
print(hasil_pengurangan)

# No 2
# Perkalian matriks
print("Perkalian matriks")
matriks1 = np.array([[2, 6], [8, 2]])
matriks2 = np.array([[6, 4], [2, 8]])
print(np.dot(matriks1, matriks2))

# No 3
import numpy as np

matriks = np.array([[1, 2, 3], [4, 5, 6]])
print("Transpose matriks")
# Transpose matriks
print(np.transpose(matriks))

# No 4
# Invers matriks
print("Invers matriks")
matriks1 = np.array([[4, -2, 1], [5, 0, 3], [-1, 2, 6]])

print(np.linalg.inv(matriks1))

# No 5
import numpy as np

# Buat matriks identitas 4x4
matriks_identitas = np.eye(4)
print("Matriks identitas")
print(matriks_identitas)

# No 6
import numpy as np

matriks = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])

# Reshape matriks menjadi 4x4
matriks_reshape = np.reshape(matriks, (2, 8))
print("Matriks reshape")
print(matriks_reshape)
