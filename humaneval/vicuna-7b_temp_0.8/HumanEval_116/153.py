
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
    # first step is to convert all numbers to 0 and 1
    binary = [int(x) for x in arr]
    binary_index = [0] * len(binary)
    binary_count = [0] * len(binary)
    for i in range(len(binary)):
        for j in range(i+1, len(binary)):
            binary_count[binary_index[i]] += binary_count[binary_index[j]]
        binary_count[binary_index[i]] += 1
        binary_index[binary_count[binary_index[i]]] = i
    return binary_index
