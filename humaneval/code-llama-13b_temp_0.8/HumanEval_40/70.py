

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

    # Use sets because we don't care if there are duplicate triples,
    # only if there is a triple.
    s = set()

    # for each item in the list...
    for i in l:
        # for each item in the list again...
        for j in l:
            # for each item in the list again...
            for k in l:
                # if the first item plus the second plus the third is zero...
                if i + j + k == 0:
                    # add the triple to the set
                    s.add((i, j, k))

    # if the length of the set is at least one, then there is a triple.
    # otherwise, there is not a triple.
    return len(s) >= 1
