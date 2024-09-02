

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
    # sort the list
    l = sorted(l)
    # if the list is empty, return False
    if len(l) == 0:
        return False
    # otherwise, we can iterate through the list, checking for two
    # adjacent values that sum to zero
    for i in range(len(l) - 1):
        if l[i] + l[i + 1] == 0:
            return True
    # if we haven't found any pairs, then return False
    return False
