

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
    # First, check that the input list is not empty
    if not l:
        return False
    
    # Initialize variables to keep track of the number of elements
    # and the number of negative elements
    n = len(l)
    neg = 0
    for i in range(n):
        if l[i] < 0:
            neg += 1
        else:
            nonneg = n - neg - 1
            if nonneg == 0:
                return True
    
    return False
