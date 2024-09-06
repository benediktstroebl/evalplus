

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
    # Store set of non-negative numbers seen so far
    # Store set of negative numbers seen so far
    seen_pos = set()
    seen_neg = set()

    # Go through each number
    for n in l:
        # If number is negative
        if n < 0:
            # If the negative of the number is in the set of non-negative numbers
            if -n in seen_pos:
                # Return True
                return True
            # Otherwise, add the number to the set of negative numbers
            else:
                seen_neg.add(n)
        # Otherwise
        else:
            # If the number is in the set of negative numbers
            if n in seen_neg:
                # Return True
                return True
            # Otherwise, add the number to the set of non-negative numbers
            else:
                seen_pos.add(n)
    # Return False
    return False

