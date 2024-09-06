

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
    set_list = set(l)
    # If the length of the set is less than 3, it can't be true
    if len(set_list) < 3:
        return False

    for i in set_list:
        # If any of the elements are zero, return True
        if i == 0:
            return True
        for j in set_list:
            # Don't compare i with j (which is itself)
            if i == j:
                continue
            for k in set_list:
                if i == k or j == k:
                    continue
                if i + j + k == 0:
                    return True
    return False

