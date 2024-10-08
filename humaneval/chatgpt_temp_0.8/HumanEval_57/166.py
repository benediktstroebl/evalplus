# CANNOT PARSE CODE SNIPPET
def monotonic(l: list) -> bool:
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
    increasing = decreasing = True
    for i in range(len(l) - 1):
        if l[i] > l[i+1]:
            increasing = False
        elif l[i] < l[i+1]:
            decreasing = False
        if not increasing and not decreasing:
            return False
    return True
