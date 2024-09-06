

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

    # Sanity check
    if len(l) < 2:
        return False

    # store the set of the elements in l
    s = set(l)

    # for each element in s, if the sum of that element and
    # the element's complement is zero, return True
    for i in s:
        if (i * -1) in s and i != 0:
            return True

    return False

