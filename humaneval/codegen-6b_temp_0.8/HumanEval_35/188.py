

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    maximum_element = None
    if not l:
        raise ValueError

    for elt in l:
        if maximum_element is None or elt > maximum_element:
            maximum_element = elt

    return maximum_element
