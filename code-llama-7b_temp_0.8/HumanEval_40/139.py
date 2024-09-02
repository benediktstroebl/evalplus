

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
    list_len = len(l)
    if list_len < 3:
        return False

    for i in range(list_len - 2):
        for j in range(i + 1, list_len - 1):
            sum_ = l[i] + l[j]
            for k in range(j + 1, list_len):
                if sum_ + l[k] == 0:
                    return True
    return False
