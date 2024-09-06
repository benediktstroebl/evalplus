

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

    l.sort()
    l_set = set(l)
    l_len = len(l)
    if l_len < 3:
        return False
    for i in range(l_len-2):
        current_sum = l[i] + l[i+1] + l[i+2]
        if current_sum == 0:
            return True
        if current_sum > 0:
            return False
        for j in range(i+1, l_len-2):
            current_sum = l[i] + l[j] + l[j+1]
            if current_sum == 0:
                return True
            if current_sum > 0:
                return False
            for k in range(j+1, l_len-2):
                current_sum = l[i] + l[j] + l[k]
                if current_sum == 0:
                    return True
                if current_sum > 0:
                    return False
    return False
