

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
    triplets = [i for i in l if i < 0 and i < -3]
    if len(triplets) > 0:
        return False
    else:
        s1 = [i for i in l if i < 0 and i < -2]
        s2 = [i for i in l if i < 0 and i < -1]
        return len(s1)!= len(s2)
