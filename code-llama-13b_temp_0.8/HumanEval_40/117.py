

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
    # make a set to store elements that sum to zero
    # iterate over the list
    # for each element in the list, check if zero - element is in the set
    # if it is, then we have found two elements that sum to zero and
    # we return true
    # otherwise, add element to the set
    # if we have gone through all the elements in the list and have not
    # returned True, return False
    pass

