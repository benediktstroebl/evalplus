

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
    # BEGIN PSEUDOCODE
    # For each pair of elements in the input list:
    #     If the sum of the pair is 0, return True
    #     If the sum of the pair is not 0, return False
    #
    # END PSEUDOCODE
    # BEGIN SOLUTION
    # Create a set of values from the input list
    seen_numbers = set(l)
    # For each element in the list, see if the sum of that element
    # and - that element is in the set
    for num in l:
        if -num in seen_numbers:
            return True
    return False
    # END SOLUTION
