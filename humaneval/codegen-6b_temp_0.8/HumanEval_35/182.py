

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    assert isinstance(l, list), "l must be a list"
    assert len(l) > 0, "l must have at least 1 element"

    max_val = l[0]
    for element in l:
        if element > max_val:
            max_val = element
    return max_val

