
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
    count_map = {}
    for num in arr:
        num_in_bin = bin(num)[2:]
        ones = num_in_bin.count('1')
        if ones not in count_map:
            count_map[ones] = []
        count_map[ones].append(num)
    result = []
    for ones_count, numbers in sorted(count_map.items()):
        for num in sorted(numbers):
            result.append(num)
    return result

