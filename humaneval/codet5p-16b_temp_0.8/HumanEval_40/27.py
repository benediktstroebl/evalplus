

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
    length = len(l)
    for i in range(length - 2):
        if i > 0 and l[i] == l[i - 1]:
            continue
        j, k = i + 1, length - 1
        while j < k:
            if l[i] + l[j] + l[k] == 0:
                return True
            elif l[i] + l[j] + l[k] < 0:
                j += 1
            else:
                k -= 1
    return False

