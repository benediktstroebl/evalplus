

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

    # if there are less than two elements in the list, there's nothing to sum
    if len(l) < 2:
        return False

    # generate a list of all possible pairs of elements in the list
    pairs = [(l[i], l[j]) for i in range(len(l)) for j in range(i + 1, len(l))]

    # for each pair, check if the sum is 0
    for pair in pairs:
        if pair[0] + pair[1] == 0:
            return True

    # if no pair sums to zero, return False
    return False
