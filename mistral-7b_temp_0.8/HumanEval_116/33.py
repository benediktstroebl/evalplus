
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

    #change array into binary representation
    array_binary = []
    for i in arr:
        array_binary.append(bin(i)[2:])

    #sort array
    sorted_array_binary = sorted(array_binary, key = len)

    #change array back to normal
    return_array = []
    for i in sorted_array_binary:
        return_array.append(int(i, 2))
    return return_array
