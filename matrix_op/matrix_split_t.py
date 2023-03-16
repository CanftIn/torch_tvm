import unittest

import numpy as np

from matrix_split import matrix_split, pad_matrix_multiple_four, remove_padding


class TestMatrixSplit(unittest.TestCase):
    def __init__(self, methodName: str = "TestMatrixSplit") -> None:
        super().__init__(methodName)
        # 创建一个 6x8 的矩阵
        self.matrix68 = np.arange(48).reshape(6, 8)
        # print(self.matrix68)

        # 将矩阵加padding后变为 4x4 大小倍数的矩阵
        self.pad_matrix68 = pad_matrix_multiple_four(self.matrix68)
        # print(self.pad_matrix68)

        # 创建一个 8x5 的矩阵
        self.matrix85 = np.arange(40).reshape(8, 5)
        # print(self.matrix85)

        # 将矩阵加padding后变为 4x4 大小倍数的矩阵
        self.pad_matrix85 = pad_matrix_multiple_four(self.matrix85)
        # print(self.pad_matrix85)

    def test_base(self):
        sub_matrices68 = matrix_split(self.pad_matrix68, 4, 4)
        # print(sub_matrices68)
        for row_matrices in sub_matrices68:
            for mat in row_matrices:
                # print(mat)
                self.assertEqual(mat.shape, (4, 4))

    def test_dot(self):
        sub_matrices68 = matrix_split(self.pad_matrix68, 4, 4)
        sub_matrices85 = matrix_split(self.pad_matrix85, 4, 4)

        transform_mat = []
        for i in range(len(sub_matrices68)):
            n = len(sub_matrices68[i])
            plus_mat = []
            for j in range(n):
                dot_mat_list = []
                for time in range(n):
                    dot_matrix = (sub_matrices68[i][time]).dot(sub_matrices85[time][j])
                    dot_mat_list.append(dot_matrix)

                mat = np.zeros((4, 4))
                for idx in range(len(dot_mat_list)):
                    mat += dot_mat_list[idx]
                plus_mat.append(mat)
            transform_mat.append(plus_mat)

        hstack_output = []
        for i in range(len(transform_mat)):
            hstack_output.append(np.hstack(transform_mat[i]))

        output_with_padding = np.vstack(hstack_output)
        output = remove_padding(output_with_padding, (6, 5))
        
        print(self.matrix68)
        print(self.matrix85)
        print(output)

if __name__ == "__main__":
    unittest.main()
