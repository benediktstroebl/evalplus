
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
    aux = [0] * len(arr)
    for i, num in enumerate(arr):
        shift = 0
        while num > 0:
            if num & 1:
                aux[shift] += 1
            num >>= 1
            shift += 1
    aux = [(num, i) for i, num in enumerate(aux)]
    aux.sort()
    for i, num in enumerate(aux):
        arr[i] = num[1]
    return arr

