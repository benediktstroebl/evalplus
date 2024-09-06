

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
    # Create an empty dictionary
    tally = {}
    # Iterate through each element in list l
    for i in l:
        # Check if the inverse of i is in tally
        if (-i) in tally:
            # Return True if the inverse is in tally
            return True
        # Add i to tally
        tally[i] = i
    # Return False
    return False

