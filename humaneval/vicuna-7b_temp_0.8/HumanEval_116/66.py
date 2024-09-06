
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
    # 1. Get the number of ones in each number
    n1 = count_ones(arr[0])
    n = n1 + arr[1]
    
    # 2. Create a new array with the sorted numbers
    sorted_arr = []
    for i in range(n):
        # 2.1. If n1 > 0, put the next number in sorted_arr
        if n1 > 0:
            sorted_arr.append(arr[i])
            n1 -= 1
        # 2.2. If n1 == 0, and n > 0, put the next number in sorted_arr
        if n1 == 0 and n > 0:
            sorted_arr.append(arr[i])
            n -= 1
    
    return sorted_arr
