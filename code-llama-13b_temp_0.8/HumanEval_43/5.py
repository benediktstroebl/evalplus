

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
    # if l is empty, return false
    if not l:
        return False
    # if l contains one element, return false
    if len(l) == 1:
        return False

    # initalize a set
    s = set()

    # traverse the list
    for elem in l:
        if elem in s:
            return True
        else:
            s.add(-elem)

    return False

