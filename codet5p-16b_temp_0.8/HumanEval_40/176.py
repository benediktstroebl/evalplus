

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
    # create dictionary to hold our values
    d = {}
    # loop over each element
    for i in l:
        if i in d:
            return True
        # if element + current element == 0, then we have a match
        elif i + i in d.values():
            return True
        # if element + current element == -element, then we have a match
        elif i + i == -i:
            return True
        d[i] = i
    return False
