
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
    # swap the first and last elements
    arr.reverse()

    # count the number of ones in the binary representation of each element
    ones = 0
    for i in range(len(arr)):
        while (arr[i] > 0):
            ones += arr[i]
            arr[i] = arr[i] % 10

    # reorder the elements according to the count of ones
    result = [0] * len(arr)
    for i in range(len(arr)):
        if ones > i:
            result[i] = arr[i]
        else:
            result[i] = arr[i - ones]

    return result