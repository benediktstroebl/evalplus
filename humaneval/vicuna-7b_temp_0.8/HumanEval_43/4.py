

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
    # check if list is empty
    if not l:
        return False

    # check if list has only one element
    if len(l) == 1:
        return False

    # sort the list
    l.sort()

    # check if the last two elements are equal
    if l[-2] == l[-1]:
        return False

    # check if the sum of the first two elements is zero
    if (l[-2] - l[-1]) == l[-2] - l[-3] and l[-2] != 0:
        return True

    # check if the sum of any two adjacent elements is zero
    for i in range(2, len(l)-1):
        if (l[i] + l[i+1]) == 0:
            return True

    # check if the last element is zero
    if l[-1] == 0:
        return True

    return False