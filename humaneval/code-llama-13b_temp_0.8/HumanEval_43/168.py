

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
    # some callers pass lists.  We'll make a set
    l = set(l)

    # this is the time complexity of our algorithm.
    # we iterate through the entire list once.
    # for each item, we look up that item in the set.
    # the set lookups take constant time.
    for item in l:
        if (0 - item) in l:
            return True

    # if we complete the above loop without returning,
    # then we know there are no two items that sum to zero.
    return False
