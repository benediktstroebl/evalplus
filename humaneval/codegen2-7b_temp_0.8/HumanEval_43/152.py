

def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    >>> pairs_sum_to_zero([1, 3, 5, 0])
    False
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    False
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >>> pairs_sum_to_zero([1])
    False
    """
    for i in l:
        if len(l) > 1 and l[0] == l[1] and l[1] == l[2]:
            return True
        for j in l:
            if i == 0 and j == 0:
                continue
            if abs(i) == abs(j) and abs(i) + abs(j) == 0:
                return True
    return False



