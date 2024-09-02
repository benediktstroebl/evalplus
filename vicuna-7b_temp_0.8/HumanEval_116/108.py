
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
    if not arr:
        return arr
    
    # create a copy of the array
    arr_copy = arr.copy()
    
    # sort the array
    arr_copy.sort()
    
    # reverse the order of elements if there is an even number of ones
    if len(arr_copy) % 2 == 0:
        arr_copy = arr_copy[::-1]
    
    return arr_copy