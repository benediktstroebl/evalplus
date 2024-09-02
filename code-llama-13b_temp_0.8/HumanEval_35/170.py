

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    if not l:
        return

    max_value = l[0]

    for i in l[1:]:
        max_value = max(max_value, i)

    return max_value

