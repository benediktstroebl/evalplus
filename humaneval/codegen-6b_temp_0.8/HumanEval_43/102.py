

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
    sorted_l = sorted(l)
    first = 0
    second = 1
    while first < len(sorted_l) - 1:
        while second < len(sorted_l) - 1:
            value = sorted_l[second] - sorted_l[first]
            if value == 0:
                return True
            second += 1
        first += 1
        second = first + 1
    return False

