
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
    # from n(1) to 1, i.e. 1
    for i in range(2 ** (n - 1) - 1, -1, -1):
        print(i, arr)
        # print(i, arr)
        # print(arr)
        # i = 0
        if arr[n - 1] & i:
            arr.append(arr.pop(0))
    return arr

