

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
    # keep track of the numbers we've seen
    seen = set()
    # loop through every number in the list
    for num in l:
        # check if the negative of the number is in the set
        if num in seen:
            return True
        # add the number to our set
        seen.add(num)
    # if we make it here, there was no pair of numbers that summed to zero
    return False

