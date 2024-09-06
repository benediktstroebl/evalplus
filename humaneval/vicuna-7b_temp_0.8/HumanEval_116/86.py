
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
        count number of ones in binary representation of the number
        """
        return sum(num > i for i in range(8))

    def binary_to_decimal(num):
        """
        convert binary representation to decimal representation
        """
        binary = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        result = 0
        while num > 0:
            if num % 2 == 0:
                result = (result * 10) + (binary.count(num // 2) - 1)
                num //= 2
            else:
                result = (result * 10) + (num - 1)
                num //= 2
        return result

    def compare(a, b):
        """
        compare two numbers, returning 1 if a > b, -1 if a < b, and 0 if a == b
        """
        if a > b:
            return 1
        elif a < b:
            return -1
        else:
            return 0

    arr = sorted(arr, key=lambda x: count_ones(binary_to_decimal(x)))

    return arr