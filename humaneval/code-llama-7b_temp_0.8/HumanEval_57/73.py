

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    # Return False if there are two values in a row that are equal.
    for index in range(len(l) - 1):
        if l[index] == l[index + 1]:
            return False
    # Compare adjacent values and return False if they change the wrong way.
    for index in range(len(l) - 1):
        if l[index] > l[index + 1] and l[index + 1] > l[index - 1]:
            return False
        if l[index] < l[index + 1] and l[index + 1] < l[index - 1]:
            return False
    return True

