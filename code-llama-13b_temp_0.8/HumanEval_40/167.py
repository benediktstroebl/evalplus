

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
    # if len(l) < 3:
    #     return False
    # for x in l:
    #     y = x + 0
    #     z = x + 0
    #     if (y + z == 0):
    #         return True
    # return False
    # Your code here
    # another solution
    seen = set()
    for x in l:
        if x not in seen:
            if -(x + 0) in seen:
                return True
            seen.add(x)
    return False

