

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

    # we can't find a pair if the list contains fewer than two elements
    if len(l) < 2:
        return False

    # we should only consider distinct elements, so we use a set instead of a list
    # sets only contain distinct elements
    s = set(l)

    # this is a runtime of O(n^2)
    # we will improve this later
    for e1 in s:
        for e2 in s:
            if e1 + e2 == 0:
                return True

    return False

