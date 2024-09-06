

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
    # our set of seen values
    seen_values = set()
    # for each item in l
    for i in l:
        # if we've already seen the value
        if i in seen_values:
            # then return True
            return True
        # otherwise, add the value to our set
        seen_values.add(i)
    # if we reach this point, there are no pairs that sum to zero
    return False
