

def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> triples_sum_to_zero([1, 3, 5, 0])
    False
    >>> triples_sum_to_zero([1, 3, -2, 1])
    True
    >>> triples_sum_to_zero([1, 2, 3, 7])
    False
    >>> triples_sum_to_zero([2, 4, -5, 3, 9, 7])
    True
    >>> triples_sum_to_zero([1])
    False
    """
    l = sorted(l)
    if l[0] > 0:
        return False
    if l[-1] < 0:
        return False
    for i in range(len(l) - 2):
        left_idx = i + 1
        right_idx = len(l) - 1
        while left_idx < right_idx:
            if l[i] + l[left_idx] + l[right_idx] == 0:
                return True
            elif l[i] + l[left_idx] + l[right_idx] < 0:
                left_idx += 1
            else:
                right_idx -= 1
    return False

