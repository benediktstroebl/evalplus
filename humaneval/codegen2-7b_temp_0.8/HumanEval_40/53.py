

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
    if len(l) == 3:
        return True
    if len(l) == 2:
        return l[0] == 0 or l[1] == 0 or l[0] == l[1]
    if l[0] == 0:
        return triples_sum_to_zero(l[1:])
    elif l[1] == 0:
        return triples_sum_to_zero(l[2:])
    return triples_sum_to_zero(l[1:]) or triples_sum_to_zero(l[2:
