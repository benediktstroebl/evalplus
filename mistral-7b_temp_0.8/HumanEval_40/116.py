

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

    d = {}
    for i in l:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    for i in d:
        if i == 0 and d[i] > 2:
            return True
        if d[i] > 1:
            for j in d:
                if i + j == 0:
                    return True
    return False

