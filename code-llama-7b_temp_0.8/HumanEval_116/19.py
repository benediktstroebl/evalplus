
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
    l1 = []
    l2 = []
    l3 = []

    for i in range(len(arr)):
        j = bin(arr[i])
        j = j[2:]
        l1.append(j.count('1'))
        l2.append(arr[i])

    for i in range(len(l1)):
        for j in range(len(l1)):
            if l1[i] < l1[j]:
                l1[i], l1[j] = l1[j], l1[i]
                l2[i], l2[j] = l2[j], l2[i]
    return l2

