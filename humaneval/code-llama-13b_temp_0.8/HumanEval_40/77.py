

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
    # ====================================
    # Do not change this function!
    # ====================================
    # the following tests verify that this function works as required
    assert triples_sum_to_zero([1, 3, 5, 0]) is False
    assert triples_sum_to_zero([1, 3, -2, 1]) is True
    assert triples_sum_to_zero([1, 2, 3, 7]) is False
    assert triples_sum_to_zero([2, 4, -5, 3, 9, 7]) is True
    assert triples_sum_to_zero([1]) is False

    # write your code here

    # ====================================
    # Do not change this function!
    # ====================================
    return False

