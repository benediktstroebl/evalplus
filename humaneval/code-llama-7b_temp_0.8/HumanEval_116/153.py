
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
    ones_dict = {}
    for i in arr:
        bin_str = str(bin(i))
        count_of_ones = 0
        for j in range(len(bin_str)):
            if bin_str[j] == '1':
                count_of_ones += 1
        if count_of_ones not in ones_dict:
            ones_dict[count_of_ones] = [i]
        else:
            ones_dict[count_of_ones].append(i)
    res = []
    for i in range(len(ones_dict)):
        res.extend(sorted(ones_dict[i]))
    return res
