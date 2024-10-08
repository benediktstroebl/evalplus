

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

    my_dict = {}

    for i in l:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1

    for i in l:
        for j in l:
            if i == j:
                continue
            if -(i + j) in my_dict:
                return True
    return False

