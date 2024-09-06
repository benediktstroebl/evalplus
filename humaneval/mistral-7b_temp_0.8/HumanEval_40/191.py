

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
    # Write your code here
    l_len = len(l)
    if l_len == 0:
        return False
    elif l_len == 1:
        return False
    elif l_len == 2:
        return False
    elif l_len == 3:
        if l[0] + l[1] + l[2] == 0:
            return True
        else:
            return False
    else:
        for i in range(len(l) - 1):
            for j in range(i + 1, len(l)):
                if l[i] + l[j] + l[j - 1] == 0:
                    return True
        return False

