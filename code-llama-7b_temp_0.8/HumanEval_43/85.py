

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

    # Determine a set of the numbers in l.
    numbers = set(l)

    # For each number in numbers
    for num in numbers:
        # determine the difference with 0
        diff = 0 - num

        # if the difference is in numbers
        if diff in numbers:
            # return True
            return True

    # return False
    return False

