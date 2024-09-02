

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    # print(max(l))
    # print(l[l.index(max(l))])
    if not l:
        return None
    if len(l) == 1:
        return l[0]
    if l[0] > l[1]:
        return max_element([l[0]])
    else:
        return max_element([l[1]])
