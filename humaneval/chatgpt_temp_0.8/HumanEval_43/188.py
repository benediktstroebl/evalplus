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
    # check if the length of the list is less than 2
    if len(l) < 2:
        return False
    # create a set to store the elements that have been seen
    seen = set()
    # loop through the list
    for num in l:
        # check if the negative of the current number is in the set
        if -num in seen:
            return True
        # add the current number to the set
        seen.add(num)
    # if we get to the end of the loop, we didn't find a pair
    return False
