

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
    if l == []:
        return False
    elif len(l) == 1:
        return False
    elif len(l) == 2:
        if l[0] + l[1] == 0:
            return True
        else:
            return False
    else:
        for i in range(len(l)):
            l1 = l[:i]
            l2 = l[i+1:]
            if l1 + l2 == [-1 * x for x in l]:
                return True
        return False
