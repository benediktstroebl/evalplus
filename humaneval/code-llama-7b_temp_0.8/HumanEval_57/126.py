

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    # same logic as increasing, just check if the previous element (index -1) is
    # less or greater than the current one
    prev_val = None
    for i in range(len(l)):
        if i == 0:
            continue
        if prev_val > l[i]:
            return False
        prev_val = l[i]
    return True

