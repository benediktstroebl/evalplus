

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
    if len(l) == 1:
        return False
    if len(l) == 2:
        if l[0] + l[1] == 0:
            return True
        else:
            return False
    # keep track of distinct elements we've seen
    seen = set()
    # for each element in our list
    for e in l:
        # if (0 - e) has already been seen, return True
        if (0 - e) in seen:
            return True
        # otherwise, add the current element to the set
        else:
            seen.add(e)
    return False
