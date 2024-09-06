

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
    first = 0
    last = len(l) - 1
    while first < last:
        curr = l[first] + l[last]
        while curr < 0:
            curr += l[first]
            first += 1
            if first > last:
                break
        if curr > 0:
            curr -= l[last]
            last -= 1
        else:
            return True
    return False
