import numpy as np

def get_matrix(name):
    try:
        rows = int(input(f"Enter number of rows for {name}: "))
        cols = int(input(f"Enter number of columns for {name}: "))
        print(f"Enter the elements for {name} row by row (space-separated):")
        matrix = []
        for i in range(rows):
            row = list(map(float, input(f"Row {i+1}: ").split()))
            if len(row) != cols:
                raise ValueError("Incorrect number of elements in the row.")
            matrix.append(row)
        return np.array(matrix)
    except ValueError as ve:
        print("Input error:", ve)
        return None

def print_menu():
    print("\n💕💕 Matrix Calculator 💕💕")
    print("1. Add two matrices")
    print("2. Multiply two matrices")
    print("3. Transpose a matrix")
    print("4. Determinant of a matrix")
    print("5. Inverse of a matrix")
    print("6. Rank of a matrix")
    print("7. Exit")

while True:
    print_menu()
    choice = input("Choose an option (1-7): ")

    if choice == '1':
        A = get_matrix("Matrix A")
        B = get_matrix("Matrix B")
        if A is not None and B is not None:
            if A.shape == B.shape:
                print("Result:\n", A + B)
            else:
                print("Error: Matrices must be the same size for addition.")

    elif choice == '2':
        A = get_matrix("Matrix A")
        B = get_matrix("Matrix B")
        if A is not None and B is not None:
            if A.shape[1] == B.shape[0]:
                print("Result:\n", np.dot(A, B))
            else:
                print("Error: Columns of Matrix A must match rows of Matrix B for multiplication.")

    elif choice == '3':
        A = get_matrix("Matrix")
        if A is not None:
            print("Transpose:\n", A.T)

    elif choice == '4':
        A = get_matrix("Square Matrix")
        if A is not None:
            if A.shape[0] == A.shape[1]:
                try:
                    det = np.linalg.det(A)
                    print("Determinant:", det)
                except Exception as e:
                    print("Error calculating determinant:", e)
            else:
                print("Error: Matrix must be square.")

    elif choice == '5':
        A = get_matrix("Square Matrix")
        if A is not None:
            if A.shape[0] == A.shape[1]:
                try:
                    if np.linalg.det(A) == 0:
                        print("Error: Matrix is singular and has no inverse.")
                    else:
                        print("Inverse:\n", np.linalg.inv(A))
                except Exception as e:
                    print("Error calculating inverse:", e)
            else:
                print("Error: Matrix must be square.")

    elif choice == '6':
        A = get_matrix("Matrix")
        if A is not None:
            try:
                rank = np.linalg.matrix_rank(A)
                print("Rank of the matrix:", rank)
            except Exception as e:
                print("Error calculating rank:", e)

    elif choice == '7':
        print("Goodbye!😘")
        break

    else:
        print("Invalid choice. Please select between 1–7.")
