

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
    l.sort()
    index1 = 0
    index2 = len(l) - 1
    while index1 < index2:
        if l[index1] + l[index2] == 0:
            return True
        elif l[index1] + l[index2] < 0:
            index1 += 1
        else:
            index2 -= 1
    return False
