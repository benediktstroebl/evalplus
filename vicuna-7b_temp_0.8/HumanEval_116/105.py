
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
    carry = 0
    for i in range(1, n):
        digit1 = arr[i]
        digit2 = carry
        for j in range(i):
            digit2 = (digit2 * 10 + arr[j]) // 2
        carry = (digit1 + digit2) % 10
        arr[i] = carry
    return arr[::-1]