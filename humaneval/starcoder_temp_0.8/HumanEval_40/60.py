

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
    #return (sum(l) in [0, 0, 0])
    result = False
    if len(l) > 2:
        i = 0
        j = i + 1
        k = j + 1
        while i < len(l) and j < len(l) and k < len(l):
            if l[i] + l[j] + l[k] == 0:
                result = True
                break
            else:
                i += 1
                j = i + 1
                k = j + 1
        return result
    else:
        return False
