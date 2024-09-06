

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

    if len(l) == 0:
        return False
    # start with first element
    element = l[0]
    # start with second element
    second_element = l[1]
    # start with third element
    third_element = l[2]

    # if the third element is the second element's negation
    if third_element == -second_element:
        # start with 4th element
        fourth_element = l[3]
        # if 4th element is the first element's negation
        if fourth_element == -element:
            return True
        else:
            # if not
            return False
    else:
        return False

