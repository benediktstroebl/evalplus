

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

    l.sort()
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[j] == l[i] and l[i] == 0:
                return True
            if l[i] == l[j]:
                return True
            if l[j] - l[i] == 0:
                return True
            if l[i] - l[j] == 0:
                return True
            if l[j] - l[i] == l[i] + l[j]:
                return True
            if l[i] - l[j] == l[j] + l[i]:
                return True
            if l[i] + l[j] == 0:
                return True
            if l[j] + l[i] == 0:
                return True
    return False
