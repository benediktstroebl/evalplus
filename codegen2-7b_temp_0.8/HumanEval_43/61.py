

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
    l_set = set(l)
    if len(l_set) == 1:
        return False
    else:
        l_set = set(l)
        l_set_difference = set(l) - set(l)
        if len(l_set_difference) == 2:
            return True
        else:
            return pairs_sum_to_zero(l_set_difference)

