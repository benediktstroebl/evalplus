

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
    t = l.copy()
    t.sort()
    for i in range(len(t)):
        start = i + 1
        end = len(t) - 1
        while start < end:
            if t[i] + t[start] + t[end] == 0:
                return True
            if t[i] + t[start] + t[end] > 0:
                end -= 1
            else:
                start += 1
    return False

