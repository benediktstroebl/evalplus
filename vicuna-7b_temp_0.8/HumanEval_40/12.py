

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
    # use a set to check if there are 3 unique elements that sum to 0
    zero_triples = set()
    for i in range(len(l)):
        if (l[i] + l[i+1] + l[i+2]) == 0:
            zero_triples.add(l[i])
            zero_triples.add(l[i+1])
            zero_triples.add(l[i+2])

    # if there are 3 unique elements that sum to 0, return True
    return len(zero_triples) == 3
