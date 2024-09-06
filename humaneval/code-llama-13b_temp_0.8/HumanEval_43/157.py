

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
    # step 1: take the input list and make it into a set
    # step 2: iterate over the set and subtract each element from 0
    # step 3: check to see if that element is in the set
    #         (which means the complementary element is also in the set)
    # step 4: return True if any of those is True
    # step 5: return False if all of those are False

    # step 1:
    # set_l = set(l)
    # step 2:
    # for x in set_l:
    #     if 0 - x in set_l:
    #         return True
    # step 3:
    # return False
    # step 4:
    # step 5:

    return any(0 - x in l for x in l)

