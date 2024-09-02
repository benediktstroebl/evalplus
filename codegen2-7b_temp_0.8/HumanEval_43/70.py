

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
    """
    The following solution is O(N) time,
    but it's certainly not the most optimal solution.
    There could be more efficient ways,
    e.g. there could be a function that returns all pairs,
    and check if there are any two pairs of elements that sum to zero.
    """
    pair_sum = 0
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if pair_sum == 0 and l[i] + l[j] == 0:
                return True
            pair_sum += l[i] + l[j]
    return False
