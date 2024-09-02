

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

    # replace this body with a working implementation
    # sort the list
    # iterate through the list twice
        # find the pair sum
    # return True or False based on the pair_sum
    sorted_l = sorted(l)
    #print(sorted_l)
    i = 0
    j = len(sorted_l) - 1
    while (i < j):
        if (sorted_l[i] + sorted_l[j] == 0):
            return True
        elif (sorted_l[i] + sorted_l[j] > 0):
            j -= 1
        else:
            i += 1
    return False
