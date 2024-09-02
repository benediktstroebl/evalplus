

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
    #for index, x in enumerate(l):
    #    target = x
    #    for y in l[index+1:]:
    #        target = target + y
    #        if target == 0:
    #            return True
    #    return False
    i = 0
    while i < len(l):
        if (-1 * l[i] in l) and (l[i] in l):
            return True
        i = i + 1
    return False
