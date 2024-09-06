

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

    # create an empty list to store elements summed to zero
    pairs_sum_to_zero = []

    # loop through the list once
    for i in l:

        # find if the element's negative is in the list
        if (-1 * i) in l:
            # if so, append both elements to the empty list
            pairs_sum_to_zero.append(i)
            pairs_sum_to_zero.append(-1*i)

    # check if there are two elements in the list
    if len(pairs_sum_to_zero) > 2:
        return True
    return False
