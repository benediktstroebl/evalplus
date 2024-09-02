

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
    pairs = {}
    for n in l:
        pairs[n] = pairs.get(n, 0) + 1

    # if the list has an even number of elements, return False.
    if len(l) % 2 == 1:
        return False

    for n in pairs:
        if -n in pairs and pairs[n] > 1 and n != -n:
            return True


    return False
