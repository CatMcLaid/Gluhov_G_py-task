# Ввод размеров матрицы
n, m = map(int, input("Введите количество строк и столбцов: ").split())

# Проверка, что количество столбцов четное
if m % 2 != 0:
    print("Количество столбцов должно быть четным!")
else:
    # Ввод матрицы
    matrix = []
    print("Введите элементы матрицы:")
    
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    # Меняем местами столбцы
    for j in range(m // 2):
        for i in range(n):
            matrix[i][j], matrix[i][m - 1 - j] = matrix[i][m - 1 - j], matrix[i][j]

    # Вывод результата
    print("Матрица после перестановки столбцов:")
    for row in matrix:
        print(*row)
