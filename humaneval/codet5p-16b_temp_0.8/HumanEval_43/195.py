

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

    set_l = set(l) #list to set
    if len(set_l) < 2: #if set is empty or only has 1 element, return False
        return False
    if 0 in set_l: #if set contains 0, remove it and recheck if set is empty
        set_l.remove(0)
        if len(set_l) < 2:
            return False
    for i in set_l:
        if (-i) in set_l: #if there are 2 elements in set that sum to zero, return True
            return True
    return False

