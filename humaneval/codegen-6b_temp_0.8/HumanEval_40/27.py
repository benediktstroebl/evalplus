

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
    # sort the input list
    l.sort()
    # store all but first element
    t = l[1:]
    # store second element
    s = l[0]
    # iterate through the list and check
    for i in t:
        if abs(i-s) == 1:
            pass
        elif abs(i-s) == 0:
            return True
    return False
