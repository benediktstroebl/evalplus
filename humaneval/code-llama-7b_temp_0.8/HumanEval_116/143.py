
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
    list_one = []
    list_zero = []
    for i in arr:
        if (bin(i)[2:].count("1") == 0):
            list_zero.append(i)
        elif (bin(i)[2:].count("1") == 1):
            list_zero.append(i)
        elif (bin(i)[2:].count("1") == 2):
            list_one.append(i)
        elif (bin(i)[2:].count("1") == 3):
            list_one.append(i)
        elif (bin(i)[2:].count("1") == 4):
            list_one.append(i)
        elif (bin(i)[2:].count("1") == 5):
            list_one.append(i)
        elif (bin(i)[2:].count("1") == 6):
            list_one.append(i)
        elif (bin(i)[2:].count("1") == 7):
            list_one.append(i)
        elif (bin(i)[2:].count("1") == 8):
            list_one.append(i)

    list_one.sort()
    list_zero.sort()

    result = list_one + list_zero
    return result
