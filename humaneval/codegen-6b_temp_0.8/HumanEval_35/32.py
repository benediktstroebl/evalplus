

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    if l == []:
        return None
    max_e = l[0]
    for e in l:
        if e > max_e:
            max_e = e
    return max_e

