

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

    ## UPERATED
    # for num in l:
    #     if -num in l:
    #         return True
    # return False

    ## CODE BELOW IS LENGTH ENCODED
    # for idx, num in enumerate(l):
    #     if -num in l[idx + 1:]:
    #         return True
    # return False

    ## FINAL APPROACH
    # l.sort()
    # for idx in range(len(l) - 1):
    #     if l[idx] + l[idx + 1] == 0:
    #         return True
    # return False

    ## O(1) SPACE
    for idx, num in enumerate(l):
        if -num in l[:idx] + l[idx + 1:]:
            return True
    return False



    # END OF CODE
