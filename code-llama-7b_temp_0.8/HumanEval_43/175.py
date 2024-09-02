

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
    # %%
    """
    linear approach:
    O(n^2) time, O(1) space
    """
    # for i in range(len(l) - 1):
    #     for j in range(i + 1, len(l)):
    #         if l[i] + l[j] == 0:
    #             return True
    # return False

    # %%
    """
    hashtable approach:
    O(n) time, O(n) space
    """
    seen = set()
    for elt in l:
        target = 0 - elt
        if target in seen:
            return True
        seen.add(elt)
    return False

