

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
    # if the first two elements are different, the list contains no pairs that sum to zero
    if l[0] != l[1]:
        return False
    # if the next two elements are different, the list contains no pairs that sum to zero
    if l[1] != l[2]:
        return False
    # the list contains at least one pair that sums to zero
    return True