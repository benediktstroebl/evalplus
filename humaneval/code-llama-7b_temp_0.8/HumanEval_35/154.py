

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    current_max = None
    for e in l:
        if current_max is None or e > current_max:
            current_max = e
    return current_max

