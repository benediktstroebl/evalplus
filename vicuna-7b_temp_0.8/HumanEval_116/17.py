
def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    """
    def count_ones(num):
        """
        :param num: An integer.
        :return: The number of ones in its binary representation.
        """
        return sum(1 for i in range(len(num)) if num[i] == 1)

    def compare(a, b):
        """
        :param a: An integer.
        :param b: An integer.
        :return: -1 if b < a, 1 if b > a, 0 if a == b
        """
        return count_ones(a) - count_ones(b)

    return sorted(arr, key=compare)