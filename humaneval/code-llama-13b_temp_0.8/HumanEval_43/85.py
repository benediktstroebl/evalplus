

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
    # empty lists
    if len(l) <= 1:
        return False
    # Sort the list
    l = sorted(l)
    # if the list has two elements
    if len(l) == 2:
        if (l[0] + l[1]) == 0:
            return True
        else:
            return False
    # if the list has more than two elements
    left = 0
    right = len(l) - 1
    while left < right:
        if (l[left] + l[right]) == 0:
            return True
        elif (l[left] + l[right]) > 0:
            right -= 1
        else:
            left += 1
    return False

