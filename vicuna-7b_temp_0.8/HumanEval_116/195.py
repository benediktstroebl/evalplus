
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
    # Initialize variables to store number of 1's in the binary representation of each number
    ones = [0] * n
    for i in range(n):
        ones[i] = sum(d > 0 for d in arr[i:])

    # Sort the array based on number of 1's in the binary representation
    for i in range(n - 1):
        j = i + 1
        while (ones[i] > ones[j] and arr[i] > arr[j]) or (ones[i] == ones[j] and arr[i] < arr[j]):
            arr[i], arr[j] = arr[j], arr[i]
            ones[i], ones[j] = ones[j], ones[i]
            i += 1
            j += 1

    return arr
