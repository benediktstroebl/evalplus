
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
    i = j = k = 0
    while j < n:
        while i <= j:
            if arr[i] > arr[j]:
                # move elements from i to j
                for p in range(i, j):
                    arr[p], arr[i] = arr[i], arr[p]
                    i += 1
            else:
                # move elements from j to i
                for p in range(j, n):
                    arr[p], arr[j] = arr[j], arr[p]
                    j += 1
        i += 1