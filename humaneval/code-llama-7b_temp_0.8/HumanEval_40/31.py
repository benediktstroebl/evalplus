

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

    # we can solve this with a set of 2 for loops and some conditional checking
    # if the len of the list is less than 4, it is not a valid solution, so we return False
    if len(l) < 3:
        return False

    l = sorted(l)
    for i in range(len(l)):
        a = l[i]
        # i + 1 because we need a gap between elements of l and a possible solution
        for j in range(i + 1, len(l)):
            b = l[j]
            for k in range(j + 1, len(l)):
                c = l[k]
                # if a + b + c = 0, return True
                if a + b + c == 0:
                    return True

    # if none of the combinations of elements in the list sum to zero, return False
    return False

