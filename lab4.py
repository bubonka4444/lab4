"""1.	Формируется матрица F следующим образом: если количество нулей в В в области 1 больше,
чем в области 3, то поменять в ней симметрично области 2 и 4 местами, иначе D и Е поменять местами несимметрично.
При этом матрица А не меняется. После чего вычисляется выражение: A*AT – K * F.
Выводятся по мере формирования А, F и все матричные операции последовательно.
"""

import random
import time


def print_matrix(M, matr_name, tt):
    print("матрица " + matr_name + " промежуточное время = " + str(format(tt, '0.2f')) + " seconds.")
    for i in M:  # перебор всех строк матрицы
        for j in i:  # перебор всех элементов в строке
            print("%5d" % j, end=' ')
        print()


print("\n-----Результат работы программы-------")
try:
    row_q = int(input("Введите количество строк (столбцов) квадратной матрицы в интервале от 6 до 100:"))
    while row_q < 6 or row_q > 100:
        row_q = int(input(
            "Вы ввели неверное число\nВведите количество строк (столбцов) квадратной матрицы в интервале от 6 до 100:"))
    K = int(input("Введите число К="))
    start = time.time()
    A, F, KF, AT, AAT, AF = [], [], [], [], [], []  # задаем матрицы
    for i in range(row_q):
        A.append([0] * row_q)
        F.append([0] * row_q)
        KF.append([0] * row_q)
        AT.append([0] * row_q)
        AAT.append([0] * row_q)
        AF.append([0] * row_q)
    time_next = time.time()
    print_matrix(F, "F", time_next - start)

    for i in range(row_q):  # заполняем матрицу А
        for j in range(row_q):
            if i < j and j < row_q - 1 - i:
                A[i][j] = 1
            elif i < j and j > row_q - 1 - i:
                A[i][j] = 2
            elif i > j and j > row_q - 1 - i:
                A[i][j] = 3
            elif i > j and j < row_q - 1 - i:
                A[i][j] = 4

    time_prev = time_next
    time_next = time.time()
    print_matrix(A, "A", time_next - time_prev)
    for i in range(row_q):  # F
        for j in range(row_q):
            F[i][j] = A[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(F, "F", time_next - time_prev)

    B = []  # задаем матрицу B
    size = row_q // 2
    for i in range(size):
        B.append([0] * size)

    for i in range(size):  # формируем подматрицу B
        for j in range(size):
            B[i][j] = F[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(B, "B", time_next - time_prev)

    zeros_1 = 0
    zeros_3 = 0
    for i in range(size):  # обрабатываем подматрицу B
        for j in range(i + 1, size // 2, 1):
            if B[i][j] == 0:
                zeros_1 += 1
    for i in range(size):  # обрабатываем подматрицу B
        for j in range(i - 1, size // 2, -1):
            if B[i][j] == 0:
                zeros_3 += 1

    if zeros_1 > zeros_3:
        for i in range(1, size // 2, 1):  # меняем подматрицу С
            for j in range(0, i, 1):
                B[i][j], B[size - i - 1][size - j - 1] = B[size - i - 1][j], B[i][j]
        for i in range(size // 2, size, 1):
            for j in range(0, i, 1):
                B[i][j], B[size - i - 1][j] = B[size - i - 1][j], B[i][j]
        print_matrix(B, "B")
        for i in range(size):  # формируем матрицу F
            for j in range(size):
                F[i][size - row_q % 2 + j] = B[i][j]
    else:
        for j in range(row_q // 2):
            for i in range(row_q // 2 + row_q % 2, row_q, 1):
                F[i][j], F[i][row_q // 2 + row_q % 2 + j] = F[i][row_q // 2 + row_q % 2 + j], F[i][j]

    time_prev = time_next
    time_next = time.time()
    print_matrix(F, "F", time_next - time_prev)
    print_matrix(A, "A", 0)

    for i in range(row_q):  # K*F
        for j in range(row_q):
            F[i][j] = K * F[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(F, "K*F", time_next - time_prev)

    for i in range(row_q):  # AT
        for j in range(i, row_q, 1):
            AT[i][j], AT[j][i] = A[j][i], A[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(AT, "A^T", time_next - time_prev)

    for i in range(row_q):
        for j in range(row_q):
            AAT[i][j] = (AT[j][i] * A[i][j])
    time_prev = time_next
    time_next = time.time()
    print_matrix(AAT, "A*A^T", time_next - time_prev)

    for i in range(row_q):  # A*AT – K * F
        for j in range(row_q):
            AF[i][j] = AAT[i][j] - F[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(AF, "A*AT – K * F", time_next - time_prev)

    finish = time.time()
    result = finish - start
    print("Program time: " + str(result) + " seconds.")

# except ValueError:
#    print("\это не число")

except FileNotFoundError:
    print(
        "\nФайл text.txt в директории проекта не обнаружен.\nДобавьте файл в директорию или переименуйте существующий *.txt файл.")
