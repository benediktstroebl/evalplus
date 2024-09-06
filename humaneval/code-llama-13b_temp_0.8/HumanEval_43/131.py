

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

    # make sure the list has at least two items
    if len(l) < 2:
        return False

    # if the list only has two items, check if the sum of the list is zero
    if len(l) == 2:
        return sum(l) == 0

    # create a new list that only includes elements that are not zero
    # and store them in a set to remove duplicates
    not_zero = set()
    for elem in l:
        if elem != 0:
            not_zero.add(elem)

    # check if any of the remaining elements sum to zero
    for elem in not_zero:
        if -elem in not_zero:
            return True

    # if we make it through the whole loop without returning anything
    # that means there are no two distinct elements in the list that sum to zero
    return False


