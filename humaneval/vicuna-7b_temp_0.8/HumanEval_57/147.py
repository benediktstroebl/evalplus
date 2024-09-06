

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    # Use a dictionary to track the previous element in the list
    # and keep track of the monotonicity
    monotonicity = {}
    
    # Iterate over the list and update the monotonicity
    for element in l:
        if element not in monotonicity:
            monotonicity[element] = 1
        else:
            monotonicity[element] += 1
    
    return len(monotonicity) > 1
