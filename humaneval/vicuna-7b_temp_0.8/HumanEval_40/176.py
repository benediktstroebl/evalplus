

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
    for i in range(len(l)):
        if i != 0:
            if l[i] == l[i-1]:
                continue
            if l[i-1] != l[i-2]:
                continue
            for j in range(i+1, len(l)):
                if l[j] != l[j-1] and l[j] != l[j-2] and l[j] != l[i]:
                    return True
    return False

triples_sum_to_zero([1, 3, 5, 0])
triples_sum_to_zero([1, 3, -2, 1])
triples_sum_to_zero([1, 2, 3, 7])
triples_sum_to_zero([2, 4, -5, 3, 9, 7])
triples_sum_to_zero([1])

result = triples_sum_to_zero([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
