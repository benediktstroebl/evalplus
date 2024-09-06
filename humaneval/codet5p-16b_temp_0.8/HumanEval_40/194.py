

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

    if not l:
        return False
    if len(l) == 1:
        return False
    if len(l) == 2:
        return False
    l.sort()
    i = 0
    j = len(l) - 1
    while i < j:
        current = l[i] + l[j]
        i += 1
        if i == j:
            return False
        if current < 0:
            i = 0
            j -= 1
            continue
        if current == 0:
            return True
        j -= 1
    return False
