

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

    l.sort()
    n = len(l)
    for i in range(n - 1):
        a = l[i]
        if i == 0 or a!= l[i - 1]:
            for j in range(i + 1, n):
                b = l[j]
                if j == i + 1 or b!= l[j - 1]:
                    for k in range(j + 1, n):
                        c = l[k]
                        if c == l[k - 1] or k == j + 1:
                            if a + b + c == 0:
                                return True
    return False
