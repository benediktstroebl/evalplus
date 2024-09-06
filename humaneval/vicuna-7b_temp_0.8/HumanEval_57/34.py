

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    first = l[0]
    last = max([max(l[1:]), min(l[1:])])
    for element in l[1:]:
        if element > last:
            return False
        if element < first:
            return False
        last = element
    return True
