

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    # Tip: you can use list.sort() or sorted(list) to sort a list
    # https://docs.python.org/3/library/stdtypes.html?highlight=sorted#list.sort
    # https://docs.python.org/3/library/functions.html#sorted
    l.sort()
    l1 = l
    l1.reverse()
    if l == l1:
        return True
    else:
        return False

