

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
    t = set()
    for a in l:
        for b in l:
            if a == b:
                continue
            for c in l:
                if a == c or b == c:
                    continue
                if a + b + c == 0:
                    return True
                if a + b + c in t:
                    return True
                t.add(a + b + c)
    return False

