import numpy as np


def matrix_split(matrix, row_num, col_num):
    m, n = matrix.shape

    row_count = m // row_num
    col_count = n // col_num

    sub_matrices = []
    # split
    for i in range(row_count):
        row_matrices = []
        for j in range(col_count):
            sub_matrix = matrix[
                i * row_num : (i + 1) * row_num, j * col_num : (j + 1) * col_num
            ]
            row_matrices.insert(j, sub_matrix)
        sub_matrices.insert(i, row_matrices)
    return sub_matrices


def pad_matrix_multiple_four(matrix):
    m, n = matrix.shape
    # row, col with add padding
    pad_m = ((m + 3) // 4) * 4
    pad_n = ((n + 3) // 4) * 4
    # init
    pad_matrix = np.zeros((pad_m, pad_n), dtype=matrix.dtype)
    pad_matrix[:m, :n] = matrix
    return pad_matrix

def join_matrix(transform_matrix):
    ret_mat = []
    for i in transform_matrix:
        np.hstack()

def remove_padding(matrix, original_shape):
    m, n = original_shape
    pad_m, pad_n = matrix.shape

    pad_row = pad_m - m
    pad_col = pad_n - n

    if pad_row > 0:
        matrix = matrix[:-pad_row, :]
    if pad_col > 0:
        matrix = matrix[:, :-pad_col]
    return matrix