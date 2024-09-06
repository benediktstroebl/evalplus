

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
    # If there are less than 3 elements, then we cannot have 3 numbers that
    # add to zero
    if len(l) < 3:
        return False
    # If we have 3 elements, check if the 3 elements add to zero
    elif len(l) == 3:
        if sum(l) == 0:
            return True
        else:
            return False

    # Go through the list, and for every element check if the element
    # and any other element in the list add to zero.
    for i, element in enumerate(l[:len(l) - 2]):
        # We cannot check if the element and the same element add to zero
        if l[i] != element:
            # We cannot check if the element and an element after the element
            # add to zero
            if i != len(l) - 2:
                # Check if element + l[i + 1] + l[i + 2] add to zero
                if element + l[i + 1] + l[i + 2] == 0:
                    return True
    return False

