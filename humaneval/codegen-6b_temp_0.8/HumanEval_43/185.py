

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
    n = len(l)
    horizontal_ls = [False for i in range(n)]
    for i in l:
        horizontal_ls[i] = True
    if n > 1:
        for j in range(n - 1):
            if not horizontal_ls[j]:
                for k in range(j + 1,n):
                    if (not horizontal_ls[k]) and l[j] + l[k] == 0:
                        return True
    return False