

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
    ### START CODE HERE (REPLACE INSTANCES OF 'None' with your code) ###

    # make a set from the input list
    s = set(l)

    # check if any two elements in the set sum to zero
    for n in s:
        if -(n) in s:
            return True

    # if the function hasn't returned True, then we know that no two elements in the
    # input list sum to zero
    return False

    ### END CODE HERE ###
