#!/usr/bin/python3
"""
This module defines a function that divides all elements of
a matrix by a divisor
"""


def matrix_divided(matrix, div):
    """divides each element of a matrix by div
    Args:
        matrix (list): matrix to divide
        div (int): divisor
    Raises:
        TypeError: div must be a number
        TypeError: each row of the matrix must have the same size
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        ZeroDivisionError
    Returns:
        lists: matrix divided by div
    """
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    matrix_error = 'matrix must be a matrix (list of lists) of integers/floats'

    if not isinstance(matrix, list):
        raise TypeError(matrix_error)

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(matrix_error)

    if not all(isinstance(el, (int, float)) for row in matrix for el in row):
        raise TypeError(matrix_error)

    if len(matrix) == 0:
        raise TypeError(matrix_error)

    for i in matrix:
        if len(i) == 0:
            raise TypeError(matrix_error)

    for line in matrix:
        if len(line) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')

    return list(map(lambda row: list(map(lambda v:
                                         round(v/div, 2), row)), matrix))
