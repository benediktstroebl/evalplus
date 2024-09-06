

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    if len(l) == 1:
        return l[0]
    maximum = l[0]
    for i in range(1, len(l)):
        maximum = max(maximum, l[i])
    return maximum
