

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

    def triples_sum_to_zero_helper(l, index, found_triple):
        if index == len(l):
            return found_triple
        if l[index] == 0:
            return triples_sum_to_zero_helper(l, index + 1, found_triple + 1)
        elif (found_triple > 0) and (l[index] + l[index - 1] + l[index - 2] == 0):
            return triples_sum_to_zero_helper(l, index + 1, found_triple + 1)
        else:
            return triples_sum_to_zero_helper(l, index + 1, found_triple)

    return triples_sum_to_zero_helper(l, 2, 0) > 0

