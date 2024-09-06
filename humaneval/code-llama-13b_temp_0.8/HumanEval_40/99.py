

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

    # hint: how many elements does a list have to have to guarantee that there are three distinct elements in the list that sum to zero?
    # hint: use hash tables / sets
    # hint: iterate through the list, and subtract each element from the two other elements in the list.

    if len(l) < 3:
        return False

    seen = set()

    for i in l:
        for j in l:
            if i == j:
                continue
            if (j - i) in seen:
                return True
            seen.add(i)
    return False
