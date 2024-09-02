

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    if not l:
        raise ValueError("Argument is empty")
    # when len(l) == 1
    if len(l) == 1:
        return l[0]

    # when len(l) > 1
    max = 0
    for i in l:
        if i > max:
            max = i
    return max
