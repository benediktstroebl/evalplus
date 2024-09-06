

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    if len(l) == 0:
        return l[0]
    elif len(l) == 1:
        return l[0]
    else:
        result = l[0]
        for i in range(1, len(l)):
            if l[i] > result:
                result = l[i]
        return result

