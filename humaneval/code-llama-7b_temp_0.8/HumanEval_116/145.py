
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
    # our dict
    bin_to_num = {}
    for num in arr:
        # get binary representation of num
        bin_rep = bin(num)[2:]
        # key for dict is number of ones
        # value is decimal representation of num
        ones = bin_rep.count('1')
        if ones not in bin_to_num:
            bin_to_num[ones] = [num]
        else:
            bin_to_num[ones].append(num)

    # sort by key
    sorted_bin_to_num = sorted(bin_to_num.keys())
    # flatten dict
    sorted_arr = [x for ones in sorted_bin_to_num for x in bin_to_num[ones]]
    return sorted_arr
