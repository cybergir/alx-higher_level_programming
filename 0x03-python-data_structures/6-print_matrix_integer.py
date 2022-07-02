#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        for col in range(len(line)):
            print(
                "{:d}".format(line[col]), end=" " if col+1 < len(line) else ""
            )
        print()
