# функция умножения матрицы на ветор столбец
# на вход подаются matrix и vector:
# matrix - матрица в формате [addres, volues, columns],
# где addres - список количества ненулевых элементов для каждой строки
# volues - значения матрицы
# columns - номера столбцов, содержащих не нулевые элементы матрицы
# vector - вектор, на который умножается матрица
def multiplication(matrix, vector):
    ad = matrix[0]
    v = matrix[1]
    c = matrix[2]
    y = []
    if len(vector) == (max(c) + 1):
        for i in range(len(vector)):
            sum = 0
            left_index = ad[i]
            right_index = ad[i + 1]
            for j in range(left_index, right_index):
                sum += v[j] * vector[c[j]]
            y.append(sum)
        return y
    else:
        return 'Невозможно выполнить умножение - длина вектора и количество столбцов матрицы не совпадают!'

# функция перевода матрицы из формата списка списков по всем элементам в формат CRS
def matrix_CRS_form(matrix):
    addres = [0]
    volues = []
    columns = []
    kol = 0
    for row in matrix:
        col = 0
        for elem in row:
            if elem != 0:
                columns.append(col)
                volues.append(elem)
                kol += 1
            col += 1
        addres.append(kol)
    return [addres, volues, columns]


# Умножим матрицу
# (1 0 7 0
#  2 3 0 0
#  9 0 0 6
#  5 4 3 1)
# на вектор (7 0 1 2)^T

# addres = [0, 2, 4, 6, 10]
# volues = [1, 7, 2, 3, 9, 6, 5, 4, 3, 1]
# columns = [0, 2, 0, 1, 0, 3, 0, 1, 2, 3]
# matrix = [addres, volues, columns]
vector = [7, 0, 1, 2]
matrix = [[1, 0, 7, 0],
          [2, 3, 0, 0],
          [9, 0, 0, 6],
          [5, 4, 3, 1]]
print(multiplication(matrix_CRS_form(matrix), vector))
