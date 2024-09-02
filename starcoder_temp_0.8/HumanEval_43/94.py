

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
    # Add each element of l to a dictionary
    d = dict()
    for i in l:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1

    # Iterate through the dictionary and return True if any element has a
    # value of 2
    for k in d:
        if d[k] == 2:
            return True

    return False
