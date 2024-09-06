
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
    arr = [x for x in arr if x != 0]
    max_index = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if (arr[i] > arr[j] and (arr[j]-arr[i]) % 2 == 0) or (arr[i] < arr[j] and (arr[j]-arr[i]) % 2 != 0):
                arr[max_index] = arr[i]
                max_index = i
    return [x for x in arr if x != 0]
