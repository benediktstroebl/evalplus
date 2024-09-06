

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if len(l) <= 1:
        return True

    increasing = decreasing = False
    i = 0
    while i < len(l) - 1:
        if l[i] == l[i + 1]:
            i += 1
            continue

        if not increasing:
            increasing = l[i] < l[i + 1]

        if not decreasing:
            decreasing = l[i] > l[i + 1]

        if increasing and decreasing:
            return False

        i += 1

    return True
