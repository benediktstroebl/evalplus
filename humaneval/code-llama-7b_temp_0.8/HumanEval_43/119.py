

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
    # hash table that keeps track of what we have seen
    seen = {}

    for i in l:
        # determine what the opposite number to i would be
        complement = -i
        # if the complement is in the hash table
        if complement in seen:
            return True
        # else add the number to the hash table
        seen[i] = i

    return False

