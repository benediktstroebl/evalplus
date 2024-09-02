

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    # O(n) time
    # O(1) space - constant space
    if len(l) < 3:
        return True

    is_positive = l[0] < l[1]
    for i in range(1, len(l)-1):
        if is_positive and l[i] > l[i+1]:
            return False
        elif not is_positive and l[i] < l[i+1]:
            return False
        is_positive = not is_positive
    return is_positive

