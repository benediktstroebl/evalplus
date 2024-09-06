

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

    # make a set from the list
    s = set(l)

    # iterate through each element
    for i in s:
        # check if we can get zero by subtracting the number from i
        # if we can, we have found one of the numbers that sum to zero
        if -i in s:
            return True

    # if we get here, the list doesn't have any 3 numbers that sum to zero
    return False

