

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

    # edge cases
    if len(l) < 3:
        return False

    # for each element in list
    for i in l:
        # for each element after the first
        for j in l[l.index(i) + 1:]:
            # for each element after the second
            for k in l[l.index(j) + 1:]:
                if i + j + k == 0:
                    return True

    return False

