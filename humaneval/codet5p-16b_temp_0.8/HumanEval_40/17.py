

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
    first_elem = 0
    third_elem = len(l) - 1
    for i in range(len(l)):
        if i > 0 and l[i] == l[i - 1]:
            continue
        first_elem = i
        break
    for i in range(len(l) - 1, 0, -1):
        if i < third_elem and l[i] == l[i + 1]:
            continue
        third_elem = i
        break

    for i in range(third_elem):
        if i == first_elem:
            continue
        if l[i] + l[first_elem] + l[third_elem] == 0:
            return True
    return False

