

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
    # check if list is empty
    if len(l) == 0:
        return False
    # check if list has only one element
    elif len(l) == 1:
        return False
    # check if list has two elements
    elif len(l) == 2:
        return l[0] + l[1] == 0
    else:
        for i in range(len(l) - 1):
            for j in range(i + 1, len(l)):
                if l[i] + l[j] == 0:
                    return triples_sum_to_zero(l[i + 1:])
                else:
                    continue
        return False
