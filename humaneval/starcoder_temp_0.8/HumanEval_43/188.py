

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
    # Make sure the list is not empty
    if not l:
        return False
    # Make a dictionary to record all of the unique elements in the list.
    d = {}
    for x in l:
        if x not in d:
            d[x] = 0
    # If there are two or more distinct elements in the list, then we can
    # make pairs with the sum of zero.
    return len(d) >= 2
