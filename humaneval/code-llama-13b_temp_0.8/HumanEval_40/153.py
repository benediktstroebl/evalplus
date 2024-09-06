

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
    # hint1: Try creating two sets to store the sums of pairs of elements.
    # hint2: You can loop through the list twice, or use two for loops.

    # if len(l) < 3:
    #     return False
    #
    # sums = set()
    # for i in range(0, len(l)):
    #     for j in range(i+1, len(l)):
    #         sums.add(l[i]+l[j])
    #
    # for i in range(0, len(l)):
    #     if (-1 * l[i]) in sums:
    #         return True
    #
    # return False

    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[i] + l[j] == 0:
                return True

    return False
