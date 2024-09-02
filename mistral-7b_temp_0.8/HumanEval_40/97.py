

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

    if not len(l) >= 3:
        return False

    l_copy = list(l)
    l_copy.sort()
    # 3 pointers
    start = 0
    mid = len(l_copy) - 1
    end = len(l_copy) - 1

    # sum of first two
    s = l_copy[start] + l_copy[mid]

    while start < mid and mid < end:
        if s == 0:
            return True
        elif s > 0:
            # sum is greater than 0, move the pointer to the smaller side
            mid -= 1
            s = l_copy[start] + l_copy[mid]
        else:
            # sum is less than 0, move the pointer to the bigger side
            start += 1
            s = l_copy[start] + l_copy[mid]
    return False
