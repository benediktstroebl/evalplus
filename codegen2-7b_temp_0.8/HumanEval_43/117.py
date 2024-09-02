

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
    s_sum = 0
    for i in range(0, len(l) - 1):
        if l[i] < 0:
            continue
        s_sum += l[i]
        for j in range(i + 1, len(l)):
            if l[j] < 0:
                continue
            if s_sum == 0:
                return True
            if s_sum == l[i] + l[j]:
                return True
            s_sum -= l[j]
    return False
