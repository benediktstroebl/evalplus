

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    # Use a stack to keep track of previous values.
    stack = []
    for val in l:
        # Stack.push(val)
        if val > stack[-1]:
            return False
        stack.append(val)
    return True