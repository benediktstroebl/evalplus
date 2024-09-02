

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
    for i in range(len(l)):
        if l[i] == 0:
            return True

    nums_to_sum = {}
    for i in range(len(l)):
        nums_to_sum[l[i]] = i

    for i in range(len(l)):
        if l[i] in nums_to_sum and i != nums_to_sum[l[i]]:
            return True
    return False

