

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    if len(l) == 0:
        raise ValueError("list should have at least one element")
    res = l[0]
    for i in range(1, len(l)):
        if l[i] > res:
            res = l[i]
    return
