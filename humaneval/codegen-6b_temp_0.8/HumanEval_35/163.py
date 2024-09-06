

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    max_n = None
    for n in l:
        if not max_n:
            max_n = n
        elif max_n < n:
            max_n = n
    return max_n

