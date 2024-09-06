

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
    # turn the list into a set to remove duplicates
    l = set(l)
    # iterate through the list
    for i in l:
        # if a match is found for i
        if (-1 * i) in l:
            # remove it from the list
            l.remove(-1 * i)
            # check if the remaining element in the list is in the list
            if i in l:
                # return True
                return True
    # return False if no matches are found
    return False
