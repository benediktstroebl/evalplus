

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
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[j] == 0 and l[i]!= l[j]:
                if j > i + 1 and l[j - 1] == l[j] and l[j - 2] == l[j]:
                    continue
                return True
    return False

