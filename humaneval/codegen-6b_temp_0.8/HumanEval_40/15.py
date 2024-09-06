

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
    """
    list_len = len(l)

    for i in range(0, list_len-2):
        for j in range(i+1, list_len-1):
            for k in range(j+1, list_len):
                if l[i]+l[j]+l[k] == 0:
                    return True
    """
    return sum(l) == 0 and len(set(l)) == len(l)
