

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
    n = len(l)
    if n < 3:
        return False

    if l[0] == 0 and l[1] == 0 and l[2] == 0:
        return False
    elif l[0] == 0 and l[1] == 0:
        return True
    elif l[0] == 0:
        return triples_sum_to_zero(l[2:])
    elif l[1] == 0:
        return triples_sum_to_zero(l[2:])
    elif l[2] == 0:
        return triples_sum_to_zero(l[3:])
    else:
        return triples_sum_to_zero(l[3:]) or triples_sum_to_zero(l[2:])

