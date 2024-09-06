
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
    # if the array is empty, return an empty list
    if not arr:
        return []

    # if the array is a single element, return that element
    if len(arr) == 1:
        return [arr[0]]

    # find the number of ones in the binary representation of each element
    num_ones = [0] * len(arr)
    for i, val in enumerate(arr):
        num_ones[i] = (val > 0).sum()

    # sort the array based on the number of ones
    sorted_array = sorted(num_ones, reverse=True)

    # initialize the result list
    result = []

    # for each element in the array, append it to the result list
    for i in range(len(sorted_array)):
        result.append(arr[i])

    return result