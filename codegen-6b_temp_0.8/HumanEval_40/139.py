

def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> triples_sum_to_zero([1, 3, 5, 0])
    False
    >>> triples_sum_to_zero([1, 3, -2, 1])
    True
    >>> triples_sum_to_zero([1, 2, 3, 7])
    False
    >>> triples_sum_to_zero([2, 4, -5, 3, 9, 7])
    True
    >>> triples_sum_to_zero([1])
    False
    """
    if len(l) < 3:
        return False
    elif len(l) == 3:
        if sum(l) == 0:
            return True
        else:
            return False
    else:
        l.sort()
        for i in range(len(l) - 2):
            l_i = l[i]
            l_i_1 = l[i + 1]
            l_i_2 = l[i + 2]
            if (l_i + l_i_1 + l_i_2) == 0:
                return True
    return False
