

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
    if len(l) <= 1:
        return False
    else:
        for i in range(len(l) - 1):
            if l[i] in l[i + 1:]:
                return True
            else:
                return False
    # if two values in the list are equal, that means that there is no zero pair.
    # Therefore, if all values in the list are distinct, then there cannot be
    # two distinct values that sum to zero.
    # If there are no duplicate values, then all the values must sum to zero.
    # If there is a duplicate value in the list, then at least two of the values
    # will sum to zero, so there must be at least two distinct values that sum
    # to zero.

