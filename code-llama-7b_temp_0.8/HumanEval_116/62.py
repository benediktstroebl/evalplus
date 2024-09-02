
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

    from math import log2
    from bisect import bisect_left
    from itertools import groupby

    if len(arr) <= 1:
        return arr

    # Count number of ones in the binary representation of each number
    cnt_ones = [0] * (len(arr) + 1)
    for num in arr:
        cnt_ones[int(log2(num)) + 1] += 1

    # Partition array of ones by number of ones in binary representation
    cnt_ones_part = [0]
    for cnt in cnt_ones:
        cnt_ones_part.append(cnt_ones_part[-1] + cnt)

    # Sort the array of ones partition by number of ones in binary representation
    index_sorted_cnt_ones = sorted(range(len(cnt_ones)), key=cnt_ones.__getitem__)
    sorted_cnt_ones = [cnt_ones[i] for i in index_sorted_cnt_ones]

    # Transform array of ones partition into an array of its positions
    pos_ones_part = []
    for i in range(len(sorted_cnt_ones)):
        pos_ones_part.append(cnt_ones_part[i])
        if i + 1 < len(sorted_cnt_ones):
            pos_ones_part.append(cnt_ones_part[i + 1])

    # Sort the array of ones partition by its position in the array
    index_sorted_pos_ones = sorted(range(len(pos_ones_part)), key=pos_ones_part.__getitem__)
    sorted_pos_ones = [pos_ones_part[i] for i in index_sorted_pos_ones]

    # Return the number corresponding to the position of ones in the sorted array
    return [arr[bisect_left(sorted_pos_ones, i)] for i in range(len(arr))]

