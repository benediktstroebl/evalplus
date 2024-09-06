

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
    l = sorted(l)
    for i in range(0, len(l)):
        if l[i] < 0:
            return False

        target = 0 - l[i]
        start = i + 1
        end = len(l) - 1

        while start < end:
            if l[start] + l[end] == target:
                return True
            elif l[start] + l[end] < target:
                start += 1
            elif l[start] + l[end] > target:
                end -= 1

    return False

