
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
    n = len(arr)
    if n == 0:
        return []

    # binary_to_decimal[i] returns the decimal equivalent of the i-th binary number
    binary_to_decimal = {
        0b0: 0,
        0b1: 1,
        0b10: 2,
        0b11: 3,
        0b100: 4,
        0b101: 5,
        0b110: 6,
        0b111: 7
    }

    def count_ones(x):
        return sum(1 for _ in x)

    return sorted(arr, key=lambda x: (count_ones(x), binary_to_decimal[x]))