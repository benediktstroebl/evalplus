

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

    # make a copy of the list to iterate over
    my_list = l.copy()
    # initialize a list to store sums
    sums = []

    # get a list of all possible sums
    for i in my_list:
        sums.append(i)

    # find all sums that are 0
    for j in my_list:
        if (0 - j) in sums:
            return True

    return False
