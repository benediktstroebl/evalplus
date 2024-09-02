

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    # in order to be monotonic, the list must have at least two elements
    if len(l) < 2:
        return True

    # set initial direction to monotonic
    direction = None

    # iterate over list to check if all elements are monotonic
    for i in range(len(l)-1):
        # if direction is not defined, determine direction
        if not direction:
            direction = l[i] < l[i+1]
        # check if direction has changed
        if direction and l[i] < l[i+1]:
            continue
        elif direction and l[i] > l[i+1]:
            return False
        else:
            direction = not direction

    return True

