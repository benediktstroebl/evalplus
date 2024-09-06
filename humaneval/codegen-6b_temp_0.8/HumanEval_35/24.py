

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    max_element = None
    for elem in l:
        if max_element is None or elem > max_element:
            max_element = elem
    return max_element

