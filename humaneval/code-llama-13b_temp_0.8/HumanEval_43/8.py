

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
    # start by making a dictionary of the list
    # iterate through dictionary and check if there is a pair that sums to 0
    # if so, return True
    # if not, return False
    if len(l) < 2:
        return False
    nums = {}
    for num in l:
        if num in nums:
            return True
        else:
            nums[-num] = num
    return False

