

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    is_increasing = True
    previous = l[0]
    for element in l[1:]:
        if element < previous:
            if is_increasing:
                is_increasing = False
            else:
                return False
        previous = element
    return is_increasing
