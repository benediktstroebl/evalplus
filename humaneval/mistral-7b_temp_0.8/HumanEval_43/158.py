

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
    if len(l) < 2:
        return False
    elif len(l) == 2:
        return l[0] + l[1] == 0
    else:
        for x in l[1:]:
            if x == -l[0]:
                return True
            elif x + l[0] == 0:
                return True
            else:
                for y in l[1:]:
                    if y + x == 0:
                        return True
    return False

