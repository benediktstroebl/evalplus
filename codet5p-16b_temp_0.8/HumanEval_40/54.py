

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

    if len(l) < 3:
        return False
    sum_to_zero = set()
    for i in range(len(l)):
        if l[i] not in sum_to_zero:
            sum_to_zero.add(l[i])
        else:
            sum_to_zero.remove(l[i])
            sum_to_zero.add(l[i])
            if sum(sum_to_zero) == 0:
                return True
    return False
