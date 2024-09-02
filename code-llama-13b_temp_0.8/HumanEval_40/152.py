

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

    # make sure the list contains at least three elements
    if len(l) < 3:
        return False

    # create a dictionary with keys from -100 to 100
    d = {}
    for i in range(-100, 101):
        d[i] = 0

    # loop over the list
    for val in l:
        d[val] += 1

    # loop over dictionary
    for key in d:
        for j in range(-100, 101):
            if d[key] > 0 and d[j] > 0 and (key + j) == 0:
                return True

    return False

