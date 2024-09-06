
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
    if not arr:
        return arr
    if arr[0] == 1 and arr[1] == 1:
        # If the first two elements are 1, we can sort it
        sorted_arr = []
        for i in range(1, len(arr)):
            while arr[i] == 1 and arr[i-1] == 1:
                arr[i] = arr[i] + arr[i-1]
                i -= 1
            sorted_arr.append(arr[i])
        return sorted_arr
    else:
        # Otherwise, we use the following steps:
        n = 1
        pivot = arr[0]
        for i in range(1, len(arr)):
            while arr[i] == pivot and arr[i-1] != pivot:
                arr[i] = arr[i] + arr[i-1]
                i -= 1
            n += 1
            pivot = arr[i]
        return arr[n:] + arr[:n]