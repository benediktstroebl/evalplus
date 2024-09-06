
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

    # 1st step - transform every number to a binary string
    new_arr = []
    for num in arr:
        binary_str = f'{num:08b}'
        new_arr.append((binary_str.count('1'), num))

    # 2nd step - sort by 1st element in tuple
    new_arr.sort(key=lambda x: x[0])

    # 3rd step - return 2nd element in tuple
    return [x[1] for x in new_arr]

