

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
    # make sure that the input is a list
    assert isinstance(l, list)
    # make sure that the input is a list of integers
    for element in l:
        assert isinstance(element, int)
    
    # list of indices that have already been used
    used_indices = []
    # whether or not there are two distinct elements that sum to zero
    pairs_sum_to_zero = False
    for index_1, element_1 in enumerate(l):
        for index_2, element_2 in enumerate(l):
            # make sure that the same element is not chosen twice
            # and make sure that the indices are not the same
            if (index_1 != index_2) and (index_1 not in used_indices) and (index_2 not in used_indices):
                used_indices.append(index_1)
                used_indices.append(index_2)
                # make sure that the two elements are not the same
                if element_1 != element_2:
                    if element_1 + element_2 == 0:
                        pairs_sum_to_zero = True
                else:
                    print("Warning: Two elements were the same")
    return pairs_sum_to_zero
