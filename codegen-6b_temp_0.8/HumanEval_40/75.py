

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
    # set() can go from a list to a set, and a set to a list, but not the other way around.
    # set() returns a new set that has the unique elements from the list, and discards
    # the rest.
    # For our purposes, we need to pass a new list to the iterable, and that's what the lambda does.
    # However, it is a good thing to know that the inner for loop does not return anything new,
    # so we'll need to check that.
    uniques = set(l)
    if len(uniques) < 3:
        return False
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            for k in range(j + 1, len(l)):
                if l[i] + l[j] + l[k] == 0:
                    return True
    return False

