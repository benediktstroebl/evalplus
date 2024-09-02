

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

    # A set of unique elements in the list
    set_of_unique_elements = set(l)

    # If there is only 1 element in the list, it cannot be pairs sum to zero
    if len(set_of_unique_elements) == 1:
        return False

    # Otherwise, check if there exists a pair of distinct elements that sum to zero
    for i in set_of_unique_elements:
        if i * -1 in set_of_unique_elements and i != 0:
            return True

    return False

