

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
    ## precondition: l is a list of integers
    # postcondition: returns True if there are two distinct elements in the list
    # that sum to zero, and False otherwise
    # check that there are at least two elements in the list
    if len(l) < 2:
        return False
    else:
        # initialise list to hold pairs that sum to zero
        pairs_summing_to_zero = []
        # iterate over each element in the list
        for i in l:
            # iterate over each element in the list
            for j in l:
                # check if i and j are the same element
                if i == j:
                    # check if the list already contains the pair of elements
                    if [i, j] in pairs_summing_to_zero:
                        # skip to next iteration
                        continue
                # check if i + j is zero
                if i + j == 0:
                    # add the pair of elements to the list
                    pairs_summing_to_zero.append([i, j])
        # check if the list of pairs is not empty
        if len(pairs_summing_to_zero) > 0:
            return True
        # if we make it to this point, the list is empty
        return False
