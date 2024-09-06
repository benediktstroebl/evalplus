

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
    # input:
    # output:
    # triple is (1, 3, -2) -> True
    # triple is (1, 3, -3) -> False
    # triple is (1, 3, -4) -> False
    # triple is (1, 3, 0) -> False
    # triple is (0, 1, 3) -> False
    # triple is (1, -3, 0) -> False
    # triple is (1, 0, 3) -> True
    # triple is (1, 3, 3) -> False
    # triple is (0, 0, 0) -> True
    # triple is (1, 0, 0) -> True
    # triple is (0, 1, 0) -> True
    # triple is (0, 0, 1) -> True
    # triple is (1, 1, 1) -> False
    # triple is (1, 1, 0) -> False
    # triple is (1, 0, 0) -> True
    # triple is (0
