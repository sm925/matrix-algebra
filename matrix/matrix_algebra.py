import numpy as np


class Matrix:

    def __init__(self, row1, column1, list1, row2, column2, list2):
        """ Generic Matrix class for basic matrix operations.

        """
        self.matrix1 = np.array(list1).reshape(row1, column1)
        self.matrix2 = np.array(list2).reshape(row2, column2)

    def calculate_sum(self):
        """Function to add matrices using rows, columns and list.

        Args:


        Returns:
            matrix

        """

        result = self.matrix1 + self.matrix2

        return result

    def calculate_diff(self):
        """Function to subtract matrices using rows, columns and list.

        Args:


        Returns:
            matrix

        """

        result = self.matrix1 - self.matrix2

        return result

    def calculate_product(self):
        """Function to multiply matrices using rows, columns and list.

        Args:


        Returns:
        matrix

        """
        result = self.matrix1 * self.matrix2

        return result

    def calculate_inverse(self):
        """Function to inverse matrix using rows, columns and list.

        Args:


        Returns:
            matrix

        """

        result = np.linalg.inv(self.matrix1)

        return result
