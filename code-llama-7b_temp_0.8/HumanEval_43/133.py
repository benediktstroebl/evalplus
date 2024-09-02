

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
    # check if list is empty
    if not l:
        return False

    # check if list has only one element
    if len(l) == 1:
        return False

    # Initialize a set
    s = set()

    # traverse through all elements and add each element 
    # to the set
    for i in l:
        if -i in s:
            return True
        s.add(i)
    return False
