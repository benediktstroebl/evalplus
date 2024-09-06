

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
    seen = set()
    for elem in l:
        if elem not in seen:
            seen.add(elem)
        else:
            if abs(elem) in seen:
                return True
    return False
    # store = {}
    # for elem in l:
    #     if elem not in seen:
    #         seen[elem] = 1
    #     else:
    #         seen[elem] += 1
    # for key, value in seen.items():
    #     if value >= 3:
    #         return True
    # return False
