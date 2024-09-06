

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
    elif len(l) == 3:
        if l[0] + l[1] + l[2] == 0:
            return True
        else:
            return False
    else:
        for x in range(len(l)):
            for y in range(len(l)):
                for z in range(len(l)):
                    if l[x] + l[y] + l[z] == 0 and x!= y and x!= z and y!= z:
                        return True
        return False
