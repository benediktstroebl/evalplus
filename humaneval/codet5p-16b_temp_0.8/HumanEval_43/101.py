

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
    l.sort()
    first_index = 0
    last_index = len(l) - 1
    while first_index < last_index:
        curr_sum = l[first_index] + l[last_index]
        if curr_sum == 0:
            return True
        elif curr_sum < 0:
            first_index += 1
        else:
            last_index -= 1
    return False

