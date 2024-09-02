

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

    # check if the list contains one item
    if len(l) <= 1:
        return False

    # sort the list
    l = sorted(l)

    # start from the first item and end at the second last item
    for i in range(len(l) - 1):
        # if the sum of two items is zero
        if l[i] + l[-1 - i] == 0:
            return True

    return False
