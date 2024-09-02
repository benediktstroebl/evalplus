

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    def is_ascending(a: int, b: int) -> bool:
        return a <= b

    def is_descending(a: int, b: int) -> bool:
        return a > b

    for i in range(len(l)):
        if is_ascending(l[i], l[i+1]):
            continue
        return False
    return True
