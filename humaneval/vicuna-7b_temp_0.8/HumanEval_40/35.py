

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
    # Check for a single element
    if len(l) == 1:
        return False
    # Check for the list not containing any negative values
    for value in l:
        if value < 0:
            return False
    # Check for every other element being 0
    for i in range(len(l)-1):
        if l[i] == 0 and l[i+1] == 0:
            return False
    # If we reach this point, there must be three distinct elements
    # that sum to zero
    return True