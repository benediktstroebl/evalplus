
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
    if len(arr) < 2:
        return arr
    
    one_arr = []
    zero_arr = []
    for i in arr:
        if i == 1:
            one_arr.append(i)
        else:
            zero_arr.append(i)
    
    if len(one_arr) > len(zero_arr):
        return sort_array(one_arr)
    else:
        return sort_array(zero_arr)

