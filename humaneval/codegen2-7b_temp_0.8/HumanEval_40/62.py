

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
    l_len = len(l)
    if l_len == 0:
        return False
    triple_trouble = False
    for index in range(l_len):
        if l[index] > 0:
            break
        if l[index] == 0:
            for n in range(index+1, l_len):
                if l[n] > 0:
                    triple_trouble = True
                    break
                elif l[n] == 0:
                    triple_trouble = True
    return triple_trou
