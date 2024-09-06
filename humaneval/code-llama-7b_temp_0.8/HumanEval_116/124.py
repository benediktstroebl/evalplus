
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
    list_of_ones_count = []
    for num in arr:
        # 1010101
        temp = bin(num)[2:]
        # 101010
        temp = temp.rstrip('0')
        # 1010
        ones_count = temp.count('1')
        list_of_ones_count.append((ones_count, num))
    # 101010
    list_of_ones_count.sort(key=lambda tup: (tup[0], tup[1]))
    return [x[1] for x in list_of_ones_count]
