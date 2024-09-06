
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
    else:
        pivot = arr[0]
        arr[:] = sort_array(list(map(int, str(pivot))))
        while True:
            i = 0
            for j in range(1, n):
                if arr[j] == pivot - (j // 2):
                    i = j + 1
                    break
            if i == n:
                break
            else:
                for k in range(i, n):
                    arr[k], arr[i] = arr[i], arr[k]
        return arr