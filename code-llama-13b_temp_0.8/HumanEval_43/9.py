

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
    # this is a long-nosed solution
    # for i in range(len(l)):
    #     for j in range(len(l)):
    #         if l[i] + l[j] == 0 and i != j:
    #             return True
    # return False

    # this is a short-nosed solution
    # it uses a dictionary
    d = {}
    for i in l:
        if i in d:
            return True
        else:
            d[i] = i
    return False

