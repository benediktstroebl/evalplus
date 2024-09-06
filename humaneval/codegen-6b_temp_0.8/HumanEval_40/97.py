

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
    dict = {}
    for ele in l:
        if ele in dict:
            dict[ele] = dict[ele]  + 1
        else:
            dict[ele] = 1

    for ele in dict:
        if dict[ele] > 1:
            dict[ele] = dict[ele] - 1
        if -1 * ele in dict:
            if dict[-1 * ele] > 0:
                dict[-1 * ele] = dict[-1 * ele] - 1
            else:
                return True
    return False

from doctest import testmod
