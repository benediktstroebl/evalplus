

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
    for x in l:
        if x != 0:
            for y in l:
                if y != 0:
                    if x + y != 0:
                        if z = x + y + l.index(x) % 3 in l:
                            return True
                        elif z = x + y + l.index(y) % 3 in l:
                            return True
            if y != 0:
                if z = x + y + l.index(y) % 3 in l:
                    return True
    return False
