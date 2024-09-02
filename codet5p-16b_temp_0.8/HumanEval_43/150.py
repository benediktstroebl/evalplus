

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

    if not l or len(l) < 2:
        return False
    else:
        new_l = []
        for i in l:
            if i < 0:
                new_l.append(-i)
        new_l.sort()
        for i in range(len(new_l)):
            if new_l[i] < 0 and (new_l[i] + new_l[i + 1]) == 0:
                return True
    return False
