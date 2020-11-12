import unittest

from bisymmetric_matrix.model.bisymmetric import BisymmetricMatrix


class TestIsSquare(unittest.TestCase):
    def test_0_size_matrix(self):
        empty_matrix = BisymmetricMatrix()
        empty_matrix.init_matrix([])
        self.assertTrue(empty_matrix.is_square())

    def test_correct_square_matrix(self):
        square_matrix = BisymmetricMatrix()
        square_matrix.init_matrix([[3, 2, 1], [4, 3, 2], [5, 4, 3]])
        self.assertTrue(square_matrix.is_square())

    def test_not_square_matrix(self):
        not_square_matrix = BisymmetricMatrix()
        not_square_matrix.init_matrix([[3, 2, 1], [4, 3, 2]])
        self.assertFalse(not_square_matrix.is_square())
