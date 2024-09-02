

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
    l1 = l.copy()
    l2 = l.copy()
    l3 = l.copy()
    l1.sort()
    l2.sort()
    l3.sort()
    for num1 in l1:
        for num2 in l2:
            for num3 in l3:
                if num1 + num2 + num3 == 0:
                    return True
    return False

