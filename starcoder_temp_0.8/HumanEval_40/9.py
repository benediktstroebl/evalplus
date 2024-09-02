

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
    # don't modify l:
    l2 = l.copy()
    # sort l2:
    l2.sort()
    i = 0
    j = len(l2) - 1
    while i < j:
        if l2[i] + l2[j] == 0:
            return True
        elif l2[i] + l2[j] > 0:
            j -= 1
        elif l2[i] + l2[j] < 0:
            i += 1
    return False
