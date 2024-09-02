

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    n = len(l)
    d = {}
    for i in range(n):
        key = l[i]
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    prev = l[0]
    for i in range(n):
        if l[i] > prev:
            d[prev] -= 1
        prev = l[i]
    return not any(d[key] == 0 for key in d.keys())
