

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
        for num in l[1:]:
            if num > l[0]:
                l[0] = num
                return l[0]
        return l[0]