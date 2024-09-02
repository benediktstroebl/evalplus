

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
    l_sorted = sorted(l)
    if l_sorted[0] == 0:
        return True
    elif l_sorted[-1] == 0:
        return True
    else:
        for i in range(len(l_sorted)):
            if i > 0 and l_sorted[i] == l_sorted[i-1]:
                return False
            else:
                if l_sorted[i] == -l_sorted[i-1]:
                    return True
        return False
