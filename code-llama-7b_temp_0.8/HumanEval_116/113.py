
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

    # FIND SOLUTION

    # BUILD ARRAY
    ones = []
    twos = []

    for num in arr:
        count_ones = len(str(bin(num))[2:].split('1'))
        if count_ones == 1:
            ones.append((num, count_ones))
        elif count_ones == 2:
            twos.append((num, count_ones))

    ones = sorted(ones, key=lambda x: x[0])
    twos = sorted(twos, key=lambda x: x[0])

    result = []
    result += ones
    result += twos

    return [num[0] for num in result]



