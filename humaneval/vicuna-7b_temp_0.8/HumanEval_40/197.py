

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
    # sort the list
    l = sorted(l)
    # check the first and the last element
    if l[0] + l[-1] == 0:
        return True
    if l[0] == 0 and l[-1] == 0:
        return True
    # check if there are three distinct elements that sum to zero
    for i in range(1, len(l)):
        if l[i] + l[i+1] + l[i+2] == 0:
            return True
    return False