

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

    for i in range(len(l)):
        if l[i] > 0:
            return False

    i = 0
    while i < len(l) - 2:
        j = i + 1
        while j < len(l) - 1:
            k = j + 1
            while k < len(l):
                if l[i] + l[j] + l[k] == 0:
                    return True
                k += 1
            j += 1
        i += 1
    return False
