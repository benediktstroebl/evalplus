

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
    # TODO: implement me
    # Hint: You may find it useful to consider partitions of the list
    # using enumerate, or at least a nested loop
    # Don't forget to handle the case when the list has less than three elements

    # for x, i in enumerate(l):
    #     for j, k in enumerate(l):
    #         for h, l in enumerate(l):
    #             if i + k + l == 0:
    #                 return True

    # return False
    # a = 0
    # for x, i in enumerate(l):
    #     for j, k in enumerate(l):
    #         if j > x and j > i:
    #             a = j
    #             for h, l in enumerate(l):
    #                 if h > j and h > k and h > a:
    #                     if i + k + l == 0:
    #                         return True

    # return False

    for x, i in enumerate(l):
        for j, k in enumerate(l):
            if j > x:
                for h, l in enumerate(l):
                    if h > j and h > x:
                        if i + k + l == 0:
                            return True
    return False

