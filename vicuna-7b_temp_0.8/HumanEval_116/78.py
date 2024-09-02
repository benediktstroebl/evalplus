
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
    arr = list(arr)
    if not any(arr):
        return arr

    while arr:
        min_idx = arr.index(min(arr))
        max_idx = arr.index(max(arr))
        for i in range(min_idx, max_idx + 1):
            for j in range(i, len(arr)):
                if arr[j] == 1 and arr[i] != 1:
                    arr[i], arr[j] = arr[j], arr[i]
                    break
            else:
                arr[i], arr[j] = arr[j], arr[i]

        arr = arr[:min_idx] + arr[max_idx:]

    return arr
