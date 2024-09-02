

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
    # list.index(x) is the index of the first item in the list equal to x.
    # list.count(x) is the number of times x appears in the list.
    for i in range(len(l)):
        if l.count(l[i]) > 1:
            return True
        if l.count(-l[i]) == 1 and l.index(l[i])!= l.index(-l[i]):
            return True
    return False
