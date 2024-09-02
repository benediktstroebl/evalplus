

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
    # we are loosing the advantage of O(n) space as we will be looking at the list
    # we can optimize the space by making use of a hash table
    # compute the absolute value of each element
    values = [abs(x) for x in l]
    # sort the list and iterate
    l.sort()
    for idx, val in enumerate(l):
        # we will not be using the first value, so skip it
        if idx == 0:
            continue
        # compute the difference between two consecutive elements
        diff = abs(val - l[idx - 1])
        # if the difference is less than a half of the value, then there is a match
        if diff < val / 2:
            # return True
            return True
    # if we reach here, there were no matches
    return False
