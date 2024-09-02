
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
    array_ = []
    for i in arr:
        one_count = count_ones(i)
        one_count = str(one_count)
        if len(one_count) > 1:
            one_count = int(one_count, 2)
        elif len(one_count) == 1:
            one_count = int(one_count)
        else:
            continue
        array_.append(((one_count, i)))
    return sorted(array_)
