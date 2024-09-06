
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
    zero_index = [i for i, e in enumerate(arr) if e == 0]
    one_index = [i for i, e in enumerate(arr) if e == 1]
    zero_index.sort()
    one_index.sort()
    result = [0] * n
    j = 0
    for i in zero_index:
        result[i] = 0
    for i in one_index:
        result[i] = 1
    for i in range(n):
        if result[i] != i:
            j = i
            break
    if j < n - 1:
        temp = [result[j + 1]]
        for i in range(j + 1, n):
            if result[i] != temp[-1]:
                temp.append(result[i])
        result[j + 1 :] = temp
    return result

