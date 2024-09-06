

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
    if len(l) == 3:
        return l[0] + l[1] + l[2] == 0

    l.sort()
    for i in range(len(l) - 2):
        j = i + 1
        k = len(l) - 1
        while j < k:
            sum_of_3_terms = l[i] + l[j] + l[k]
            if sum_of_3_terms == 0:
                return True
            if sum_of_3_terms < 0:
                j += 1
            elif sum_of_3_terms > 0:
                k -= 1
    return False

