

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
    if len(l) < 2:
        return False
    else:
        # complete the body of the function
        # HINT: remember, this is a list of integers
        # remember, we want True if we find two distinct
        # elements in our list that sum to zero, and False otherwise.
        # we can return True when we find the first pair that satisfies this.

        for i in range(len(l)):
            for j in range(len(l)):
                if l[i] + l[j] == 0:
                    return True

        return False

        # return ...


