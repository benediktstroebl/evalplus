
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
    max_one = max([bin(x)[2:].count("1") for x in arr])

    sorted_arr = [[] for _ in range(n)]

    for num in arr:
        bit_val = bin(num)[2:].count("1")
        sorted_arr[n - bit_val].append(num)

    return [item for sublist in sorted_arr for item in sublist]

