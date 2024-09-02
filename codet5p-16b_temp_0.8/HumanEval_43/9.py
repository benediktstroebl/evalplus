

def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    >>> pairs_sum_to_zero([1, 3, 5, 0])
    False
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    False
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >>> pairs_sum_to_zero([1])
    False
    """

    sorted_list = sorted(l)
    sums = set()
    for i in range(len(sorted_list)):
        if sorted_list[i] == sorted_list[i-1] and sorted_list[i]!= 0:
            sums.add(sorted_list[i] + sorted_list[i-1])
        elif sorted_list[i] == 0:
            if 0 in sums:
                return True
            else:
                sums.add(0)
        elif sorted_list[i] == sorted_list[i-1] and sorted_list[i] == 0:
            if 0 in sums:
                return True
            else:
                sums.add(0)
        else:
            continue
    return False
