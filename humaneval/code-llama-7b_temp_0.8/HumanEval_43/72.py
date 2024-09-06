

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
    # Create a dictionary with the values as keys.
    values = {}
    # Iterate over each value.
    for x in l:
        # Check if value exists in dictionary.
        if values.get(x) is not None:
            # If value exists, return True.
            return True
        # If value doesn't exist, add it to dictionary.
        else:
            values[0 - x] = x
    # Return False.
    return False
