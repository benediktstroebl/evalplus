

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
    # Your code here
    sums = {}
    for elem in l:
        if elem not in sums:
            sums[elem] = 1
        else:
            sums[elem] += 1

    for k, v in sums.items():
        if k == 0:
            if v >= 2:
                return True
        elif -k in sums:
            if v >= 1 and sums[-k] >= 1:
                return True

    return False
