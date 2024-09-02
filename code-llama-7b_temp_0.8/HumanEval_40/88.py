

def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> triples_sum_to_zero([1, 3, 5, 0])
    False
    >>> triples_sum_to_zero([1, 3, -2, 1])
    True
    >>> triples_sum_to_zero([1, 2, 3, 7])
    False
    >>> triples_sum_to_zero([2, 4, -5, 3, 9, 7])
    True
    >>> triples_sum_to_zero([1])
    False
    """

    # create a map of elements to their indices
    l_indices = {i: l.index(i) for i in l}

    # this dict is going to map a sum value to indices of numbers that add up to it
    # for example: -3: (0,2) means that the numbers in l[0] and l[2] add up to -3
    sums = {}

    for i in l:
        for j in l:
            # we don't want to check the same indices twice, or negative sums
            # (we're not checking that here, but we have to account for it when we're using
            # sums in the loop below)
            if i != j and i+j != 0:
                # update the sum to the index pair
                sums[i+j] = (l_indices[i], l_indices[j])

    for s in sums:
        # check if s is in sums
        if -s in sums:
            # check if those indices are not the same
            if sums[s][0] != sums[-s][0] and sums[s][0] != sums[-s][1] \
                    and sums[s][1] != sums[-s][0] and sums[s][1] != sums[-s][1]:
                return True

    # if there's no such sum, return false
    return False




