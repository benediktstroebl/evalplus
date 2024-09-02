

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    """
    >>> max_element([-1, 1, 2])
    >>> max_element([-1, 1, 2])
    >>> max_element([-1, 1, 2])
    2
    """
    if len(l) == 0:
        return -999999999
    else:
        return max(l)

