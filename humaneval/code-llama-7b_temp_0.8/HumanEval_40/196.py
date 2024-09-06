

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
    # define an empty set to hold numbers found to sum to zero
    s = set()
    # add each number in the list to the set, without checking for duplicates
    for n in l:
        s.add(n)

    # now check that there are three distinct elements in the set
    if len(s) != 3:
        return False

    # and that they sum to zero
    return s.pop() + s.pop() + s.pop() == 0

