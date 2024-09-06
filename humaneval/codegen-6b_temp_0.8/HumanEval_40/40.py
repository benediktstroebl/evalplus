

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

    sum_dict = {}
    for elem in l:
        if elem in sum_dict:
            sum_dict[elem] += 1
        else:
            sum_dict[elem] = 1

    x, y, z = 0, 0, 0
    for key in sum_dict:
        if sum_dict[key] == 1:
            x = key
        if sum_dict[key] == 2:
            y = key
        if sum_dict[key] == 3:
            z = key
    if x + y + z == 0:
        return True
    else:
        return False

