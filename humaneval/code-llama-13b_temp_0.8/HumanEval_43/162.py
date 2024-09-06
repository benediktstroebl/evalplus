

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

    # ### 1. Brute force ###
    #
    # for _ in range(len(l)):
    #     for __ in range(_ + 1, len(l)):
    #         if l[_] + l[__] == 0:
    #             return True
    # return False

    # ### 2. Sorting ###
    #
    # l = sorted(l)
    # for _ in range(len(l) - 1):
    #     if l[_] + l[_ + 1] == 0:
    #         return True
    # return False

    # ### 3. Hashing ###
    #
    # hash_ = dict()
    # for _ in l:
    #     if _ in hash_:
    #         return True
    #     hash_[-_] = True
    # return False

    ### 4. Math ###

    d = dict()
    for _ in l:
        if _ in d:
            return True
        d[0 - _] = True
    return False

