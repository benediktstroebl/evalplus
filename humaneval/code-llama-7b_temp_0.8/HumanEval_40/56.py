

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
    # all possible pairs in list
    pairs = [[a, b] for a in l for b in l]
    # all possible triples in list
    triples = [[a, b, c] for a in l for b in l for c in l]
    # filter for pairs that sum to zero
    pairs_sum_to_zero = filter(lambda x: sum(x) == 0, pairs)
    # filter for triples that sum to zero
    triples_sum_to_zero = filter(lambda x: sum(x) == 0, triples)

    # return True if there are 3 triples
    if len(list(triples_sum_to_zero)) == 3:
        return True

    return False

