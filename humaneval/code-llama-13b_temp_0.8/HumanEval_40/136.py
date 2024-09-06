

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
    # hint: use 2 sets to get this in linear time
    if len(l) < 3:
        return False

    d_pos = set()
    d_neg = set()

    for i in l:
        if i < 0:
            if -i in d_pos:
                return True
            else:
                d_neg.add(i)
        else:
            if i in d_neg:
                return True
            else:
                d_pos.add(i)
    return False



