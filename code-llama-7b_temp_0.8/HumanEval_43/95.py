

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
    # make a map from elements to their count
    element_count = {}
    for i in l:
        if i in element_count:
            element_count[i] += 1
        else:
            element_count[i] = 1

    for i in element_count:
        if element_count[i] > 1:
            # if a number occurs more than once, then it has to be excluded
            # from the list of potential pairs
            element_count[i] -= 1
            for j in element_count:
                if i != j and i + j == 0:
                    return True
    return False

