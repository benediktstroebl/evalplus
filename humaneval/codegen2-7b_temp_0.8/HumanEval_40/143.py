

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
    if l:
        if len(set(l)) < len(l):
            return True
        else:
            i = 0
            while i + 1 < len(l):
                if (l[i] + l[i + 1]) in l:
                    i += 2
                else:
                    i += 1
            return i < len(l) and l[i] == 0
    else:
        return False

