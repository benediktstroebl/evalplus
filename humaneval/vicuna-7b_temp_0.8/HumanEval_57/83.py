

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    # sort the list
    l = sorted(l)
    
    # check if the list is monotonically increasing or decreasing
    if all(a <= b for a, b in zip(l[:-1], l[1:])) or all(b <= a for a, b in zip(l[1:], l[:-1])):
        return True
    else:
        return False
