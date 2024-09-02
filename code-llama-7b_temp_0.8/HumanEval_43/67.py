

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
    # TODO: your code here
    # initialize the set of numbers we already saw
    # a = {1, 3, 5, 0}
    seen = set()
    # iterate over the list
    for num in l:
        # check if the number's complement exists in the set
        if -num in seen:
            # if so, return True
            return True
        # add the number to the set
        seen.add(num)
    # otherwise, return False
    return False

