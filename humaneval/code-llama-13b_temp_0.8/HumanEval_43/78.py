

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
    # remove duplicate values
    # original_list = set(l)
    # for i in original_list:
    #     for j in original_list:
    #         if j + i == 0:
    #             return True
    # return False
    # Original solution
    # original_list = set(l)
    # for i in original_list:
    #     if -i in original_list:
    #         return True
    # return False

    # Better solution
    # set_a = set(l)
    # if 0 in set_a:
    #     return True
    # for i in set_a:
    #     if -i in set_a:
    #         return True
    # return False

    # EVEN BETTER
    return any([a + b == 0 for a in l for b in l])

