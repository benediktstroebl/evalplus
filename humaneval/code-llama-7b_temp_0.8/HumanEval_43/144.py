

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
    # Your code here
    # Hint: you might use the "sum" function
    # Solution 1:
    # s = set(l)
    # for e1 in s:
    #     for e2 in s:
    #         if (e1 + e2) == 0:
    #             return True
    # return False
    # Solution 2:
    # l.sort()
    # s = set()
    # for e in l:
    #     if -e in s:
    #         return True
    #     else:
    #         s.add(e)
    # return False
    # Solution 3:
    s = set()
    for e in l:
        if -e in s:
            return True
        else:
            s.add(e)
    return False
