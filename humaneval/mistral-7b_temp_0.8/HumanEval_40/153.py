

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
    l = sorted(l)
    # negative_index = l.index(-1)
    # negative_index = l.index(-1)
    # positive_index = l.index(1)
    negative_index = bisect_left(l, -1)
    positive_index = bisect_left(l, 1)
    if negative_index == 0:
        return False
    if negative_index + positive_index < len(l):
        return False
    return negative_index + positive_index + 1 == len(l)

