

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

    for index, element in enumerate(l):
        for index2, element2 in enumerate(l):
            if index == index2:
                continue
            for index3, element3 in enumerate(l):
                if index2 == index3:
                    continue
                if element + element2 + element3 == 0:
                    return True
    return False



