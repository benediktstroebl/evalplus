

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

    if len(l) <= 1:
        return False
    else:
        l_sorted = sorted(l)
        for i in range(len(l_sorted) - 1):
            j = i + 1
            if l_sorted[i] == l_sorted[j]:
                continue
            elif l_sorted[i] + l_sorted[j] == 0:
                return True
            else:
                continue
        return False

