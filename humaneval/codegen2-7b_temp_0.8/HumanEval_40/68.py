

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
    if all([i == 0 for i in l]):
        return False
    l2 = l[:]
    for i in range(0, len(l2)):
        if i == 0:
            pass
        elif i == 1:
            if l2[0] + l2[1] == 0:
                return True
        elif l2[i] + l2[i+1] == 0:
            return True
    return False
