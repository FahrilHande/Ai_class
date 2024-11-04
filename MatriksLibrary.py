import numpy as np

# Membuat matriks A berukuran 2x3
A = np.array([[1, 2, 3],
            [4, 5, 6]])

# Membuat matriks B berukuran 3x4
B = np.array([[7, 8, 9, 10],
            [11, 12, 13, 14],
            [15, 16, 17, 18]])

# Mengalikan matriks A dan B
C = np.dot(A, B)

print("Matriks A:")
print(A)
print("\nMatriks B:")
print(B)
print("\nHasil perkalian A * B:")
print(C)
