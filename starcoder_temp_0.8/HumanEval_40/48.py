

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
    if len(l) < 3:
        return False
    l.sort()
    for i in range(0, len(l) - 2):
        if i > 0 and l[i] == l[i-1]:
            continue
        l_i_j = l[i]
        l_j_k = l[i+1]
        for j in range(i+2, len(l) - 1):
            if l[j] > l_j_k:
                break
            if j > i + 2 and l[j] == l[j-1]:
                continue
            l_i_j_j = l_i_j + l_j_k
            l_j_k_k = l[j+1]
            for k in range(j+2, len(l)):
                if l_i_j_j + l_j_k_k == 0:
                    return True
    return False
