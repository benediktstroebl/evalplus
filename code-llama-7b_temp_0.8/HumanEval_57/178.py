

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    direction = 0
    for i in range(1, len(l)):
        if direction == 0:
            if l[i] < l[i - 1]:
                direction = -1
            elif l[i] > l[i - 1]:
                direction = 1
            elif l[i] == l[i - 1]:
                pass
        elif (direction == 1 and l[i] < l[i - 1]) or (direction == -1 and l[i] > l[i - 1]):
            return False
    return True
