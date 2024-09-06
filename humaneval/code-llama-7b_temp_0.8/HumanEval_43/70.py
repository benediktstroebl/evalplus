

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
    # Initialize an empty set.
    pairs = set()
    # Loop over all the elements in l.
    for num in l:
        # Check if negative num is in the set.
        if -num in pairs:
            # If so, we have found a pair, return True.
            return True
        else:
            # Otherwise, add the non-negative number to the set.
            pairs.add(num)
    # We have looped over all the numbers, and did not find a pair.
    # Therefore, return False.
    return False

