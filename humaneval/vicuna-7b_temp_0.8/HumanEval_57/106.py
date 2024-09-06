

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    def left(x):
        return min(x-1, x-2) if x % 2 == 0 else x-2
    def right(x):
        return max(x+1, x+2) if x % 2 == 0 else x+1
    for x in l:
        for y in l:
            if y > x:
                if x+1 < y:
                    return False
                else:
                    return True
    return True
