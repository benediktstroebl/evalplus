
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
        Returns the number of ones in the binary representation of the number.
        """
        return sum(bin(i)[2:].count('1') for i in range(len(num)))

    arr = sorted(arr, key=count_ones)
    result = [i for i in arr if not i < 0]
    return result