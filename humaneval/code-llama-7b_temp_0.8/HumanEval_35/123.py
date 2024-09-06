

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    # [None]
    # Initial state of the algorithm
    maximum = None
    for element in l:
        if maximum is None:
            maximum = element
        if element > maximum:
            maximum = element
    return maximum

