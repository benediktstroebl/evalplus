

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """

    if len(l) == 0:
        return False

    if len(l) == 1:
        return True

    if len(l) == 2:
        return (l[0] <= l[1]) or (l[0] >= l[1])

    # Normalize the list
    if l[0] > l[1]:
        l = [l[i] for i in range(len(l))][::-1]
    return monotonic(l[1:])

