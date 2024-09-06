

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

    # iterate through the list
    # for each element in the list, create a set that contains that element and all the other elements
    # check if the set contains 0
    # if it does, return True
    # if not, return False

    for x in l:
        s = set(l)
        s.remove(x)
        if 0 in s:
            return True

    return False

