

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
    if len(l) == 3:
        if sum(l) == 0:
            return True
        else:
            return False
    else:
        sum_to_zero = False
        for i in range(len(l)):
            tmp = l[:i] + l[i + 1 :]
            if len(tmp) < 3:
                break
            else:
                if sum(tmp) == 0:
                    sum_to_zero = True
        return sum_to_zero

