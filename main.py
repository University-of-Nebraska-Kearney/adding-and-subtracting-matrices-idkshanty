def main():
    print("Enter values for Matrix 1")
    m1 = get_matrix()

    print("\nEnter values for Matrix 2")
    m2 = get_matrix()

    sum_matrix = add_matrix(m1, m2)

    if sum_matrix is not None:
        print("\nSum:")
        for row in sum_matrix:
            print(row)

def get_matrix():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    matrix = []

    for i in range(rows):
        row = []
        for j in range(cols):
            value = int(input(f"Enter value for row {i}, column {j}: "))
            row.append(value)
        matrix.append(row)

    return matrix
def add_matrix(matrix1, matrix2):
    if len(matrix1) != len(matrix2):
        print("Matrices are of different sizes, cant be addef")
        return None

    result = []

    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)

    return result

if __name__ == '__main__':
    main()
