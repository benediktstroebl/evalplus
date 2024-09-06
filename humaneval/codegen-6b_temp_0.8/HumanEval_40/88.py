

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
    # remove any duplicates
    l2 = list(set(l))
    length = len(l2)
    self_minus = l2[0]
    l2 = l2[1:]
    for i in l2:
        if i != self_minus:
            self_minus = self_minus + i
            if self_minus == 0:
                return True
    return False

