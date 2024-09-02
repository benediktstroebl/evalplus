

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

    l.sort()
    for i in range(len(l) - 2):
        if i > 0 and l[i] == l[i - 1]:
            continue
        l_copy = l[:]
        l_copy.pop(i)
        low = i + 1
        high = len(l_copy) - 1
        while low < high:
            if l_copy[low] + l_copy[high] == -l[i]:
                return True
            elif l_copy[low] + l_copy[high] < -l[i]:
                low += 1
            else:
                high -= 1
    return False

