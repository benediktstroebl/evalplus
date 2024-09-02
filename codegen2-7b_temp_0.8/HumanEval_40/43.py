

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
    triples = []
    for i in range(len(l)):
        if l[i] < 0:
            continue
        for j in range(i+1, len(l)):
            if l[i] + l[j] == 0:
                triples.append((l[i], l[j]))
    if len(triples) < 3:
        return False
    for i in range(len(l)-2):
        if triples[i] in triples[i+1:]:
            return True
    return False
