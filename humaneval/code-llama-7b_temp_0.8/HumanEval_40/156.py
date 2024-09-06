

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

    # the dict keys are the values in the input list
    # the values are the indices of the input list
    indices_of_values = {val: idx for idx, val in enumerate(l)}
    # keys of indices_of_values are all distinct

    for first in range(len(l)):
        for second in range(first + 1, len(l)):
            for third in range(second + 1, len(l)):
                if l[first] + l[second] + l[third] == 0:
                    return True

    return False

