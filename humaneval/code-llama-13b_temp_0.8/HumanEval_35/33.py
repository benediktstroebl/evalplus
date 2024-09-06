

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    if len(l) == 1:
        return l[0]
    elif len(l) == 2:
        return l[0] if l[0] > l[1] else l[1]

    if len(l) % 2 == 0:
        i = len(l) // 2
    else:
        i = len(l) // 2 + 1

    if l[i - 1] < l[i]:
        return max_element(l[:i])
    else:
        return max_element(l[i:])
