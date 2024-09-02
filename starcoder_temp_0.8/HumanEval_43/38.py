

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
    # check if list has more than one item, since we only need to check if
    # there are two distinct items.
    if len(l) > 1:
        # create a list of the indices of the items in the list
        indices = range(len(l))
        # zip together the indices and the items
        zipped_items = zip(indices, l)
        # check if a pair of items sum to 0
        for i, j in zipped_items:
            if (j + l[i - 1] == 0) and (i > 0):
                return True
    # if we get to this point, there aren't two distinct items that sum to 0
    return False
