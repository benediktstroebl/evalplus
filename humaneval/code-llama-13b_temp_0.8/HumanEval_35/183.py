

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    if not l:
        return None

    max_element = l[0]

    for el in l[1:]:
        if el > max_element:
            max_element = el

    return max_element

