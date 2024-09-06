

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
    # this is the first approach:
    for a in l:
        for b in l:
            for c in l:
                if (a == b) and (b == c):
                    continue
                if (a + b + c) == 0:
                    return True

    # this is the second approach:
    # d = dict()
    # for n in l:
    #     d.setdefault(n, 0)
    #     d[n] += 1
    #
    # for i in d:
    #     if d[i] < 3:
    #         continue
    #     b = -(i * 2)
    #     if b in d:
    #         return True

    # this is the third approach:
    # for i in l:
    #     if 2 * i in l:
    #         return True

    return False

