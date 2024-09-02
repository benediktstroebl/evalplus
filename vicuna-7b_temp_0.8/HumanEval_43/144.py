

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
    # if the list is empty, return False
    if not l:
        return False

    # if the list has only one element, return True
    if len(l) == 1:
        return True

    # sort the list
    l = sorted(l)

    # if the list is not sorted, put it in a set and sort it
    if not l:
        l = set(l)
        l.sort()

    # if the list has only one element, return True
    if len(l) == 1:
        return True

    # check if the list has two distinct elements that sum to zero
    # if it does, return True, otherwise return False
    for i in range(1, len(l)):
        if (l[i] - l[i-1]) == 0 and (l[i] + l[i-1]) != 0:
            return True
    return False
