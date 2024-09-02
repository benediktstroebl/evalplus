
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
    sorted_array = []
    for number in arr:
        if number < 0:
            sorted_array.append(number)
            continue
        sorted_array.append(str(number)[2:])
    sorted_array.sort()
    for i in range(len(arr)):
        arr[i] = int(sorted_array[i], 2)
    return arr
