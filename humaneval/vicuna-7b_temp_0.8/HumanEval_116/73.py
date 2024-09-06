
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
    # The array is already sorted, so it's already ascending order
    if n == 1:
        return arr[0]
    # Check all pairs of elements
    for i in range(1, n):
        for j in range(i + 1, n):
            if arr[i] != arr[j]:
                # Swap them
                arr[i], arr[j] = arr[j], arr[i]
                # Recursively sort the sorted array
                sort_array(arr[:i])
                sort_array(arr[i+1:])
                # Swap back
                arr[i], arr[j] = arr[j], arr[i]
    return arr[1]