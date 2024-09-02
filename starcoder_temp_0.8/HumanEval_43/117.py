

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
    zero_check = []
    for i in range(len(l)):
        if l[i] == 0:
            zero_check.append(i)
    for j in range(len(zero_check)):
        for k in range(j+1, len(zero_check)):
            if l[zero_check[j]] + l[zero_check[k]] == 0:
                return True
    return False
