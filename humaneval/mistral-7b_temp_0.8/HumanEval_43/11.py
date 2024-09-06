

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
    # sort the input list to allow us to check the conditions
    l.sort()
    # check if there are 2 distinct elements that sum to zero
    for i in range(len(l)):
        # check if there are 2 distinct elements that sum to zero
        if l[i] + l[i + 1] == 0:
            return True
    return False
