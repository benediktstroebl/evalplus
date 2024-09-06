

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
    # Takes a list of integers as an input
    # Returns true if the list contains two distinct elements that sum to zero
    # Otherwise returns false
    pair = []
    for i in l:
        if (-i) in l and not (-i) == i:
            pair.append(-i)
            pair.append(i)
    if not pair:
        return False
    return True
