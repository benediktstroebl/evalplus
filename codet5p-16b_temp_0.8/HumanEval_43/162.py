

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

    sorted_l = sorted(l)
    for i in range(len(sorted_l)):
        if (sorted_l[i] == sorted_l[i-1] or (i+1 < len(sorted_l) and sorted_l[i] == sorted_l[i+1])) and sorted_l[i]!= 0:
            return False
    return True

