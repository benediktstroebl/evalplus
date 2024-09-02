

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
    for i in range(len(l)-2):
        if l[i] == 0:
            continue
        else:
            for j in range(i+1, len(l)-1):
                if l[j] == 0:
                    continue
                elif l[i] + l[j] == 0:
                    return True
                else:
                    break
            for k in range(i+1, len(l)):
                if l[i] + l[k] == 0:
                    return True
    return
