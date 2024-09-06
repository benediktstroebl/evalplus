

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

    assert isinstance(l, list), "Input must be a list"
    l.sort()
    l_len = len(l)
    i = 0
    while i < l_len - 2:
        j = i + 1
        while j < l_len - 1:
            k = j + 1
            while k < l_len:
                if l[i] + l[j] + l[k] == 0:
                    return True
                k += 1
            j += 1
        i += 1
    return False

