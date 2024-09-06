

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

    # list of tuples with each element and it's frequency
    freq = {}
    for i in l:
        freq.setdefault(i, 0)
        freq[i] += 1

    # no way for 3 elements to sum to zero with one as a negative number
    for i in l:
        if i < 0:
            return False

    # loop through dictionary of frequencies
    for i in freq.items():
        for j in freq.items():
            if j[1] + freq.get(i[0] + j[0]) == 3:
                return True
    return False

