

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """

    # Auxiliary function, returns 0 if equal, 1 if x greater and -1 if y greater
    def compare(x, y):
        if x == y:
            return 0
        if x > y:
            return 1
        return -1

    last_comp = 0
    for i in range(len(l) - 1):
        current_comp = compare(l[i], l[i+1])
        if last_comp == 0:
            last_comp = current_comp
        elif current_comp != last_comp:
            return False
    return True

