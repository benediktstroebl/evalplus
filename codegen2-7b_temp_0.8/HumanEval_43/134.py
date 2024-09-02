

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
    sums = []
    for i in range(len(l) - 1):
        for j in range(i + 1, len(l)):
            sums.append(l[i] + l[j])
    return len(set(sums)) > 2

    l.append(i)
    l2.append(i)
    if pairs_sum_to_zero(l):
        break
