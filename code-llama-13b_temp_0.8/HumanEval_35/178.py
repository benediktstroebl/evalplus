

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    maximum_value = None

    for element in l:
        if maximum_value is None or element > maximum_value:
            maximum_value = element

    return maximum_value

