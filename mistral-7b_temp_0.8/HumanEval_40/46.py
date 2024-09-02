

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

    l.sort()

    i, j, k = 0, 1, 2

    while j < len(l) - 2:
        if l[i] + l[j] + l[k] == 0:
            return True
        if l[j] == l[j+1]:
            j += 1
            continue
        i, j, k = j, j+1, j+2

    return False
