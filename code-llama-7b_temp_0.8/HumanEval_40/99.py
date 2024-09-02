

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
    d = dict()

    for num in l:
        if num not in d:
            d[num] = 1
        else:
            d[num] += 1

    for key1, val1 in d.items():
        for key2, val2 in d.items():
            if key1 + key2 == -key1:
                if key1 == key2:
                    if val1 > 2:
                        return True
                else:
                    return True
    return False

