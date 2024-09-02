

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
    # A dictionary to hold pairs that sum to 0
    sums = {}
    # Iterate through the list of values
    for value in l:
        # Iterate through the list of sums
        for key in sums:
            # If the current sum and the current value sum to 0
            if key + value == 0:
                # Return True
                return True
        # Add the current value to the dictionary of sums with the key being the
        # negative value of the current value
        sums[value * -1] = value
    # Return False
    return False
