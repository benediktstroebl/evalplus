

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    assert len(l) > 0, "Empty list"
    max_el = l[0]
    for x in l:
        if x > max_el:
            max_el = x
    return max_el
