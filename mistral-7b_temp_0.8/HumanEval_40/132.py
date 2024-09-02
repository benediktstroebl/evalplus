

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

    if len(l) == 1:
        return False

    def sum_to_zero(s: list):
        if len(s) == 0 or len(s) == 1:
            return False

        for i in range(len(s) - 1):
            for j in range(i + 1, len(s)):
                if s[i] + s[j] == 0:
                    return True
        return False

    for i in range(len(l)):
        if sum_to_zero(l[i:]) is True:
            return True

    return False

