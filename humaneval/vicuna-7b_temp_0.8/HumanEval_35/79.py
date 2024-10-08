

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    try:
        return l[0]
    except:
        for element in l:
            if element > l[0]:
                return element
        return l[0]