

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    if l == []:
        return None
    if len(l) == 1:
        return l[0]
    else:
        first = l[0]
        max = first
        for i in range(1, len(l)):
            if max < l[i]:
                max = l[i]
        return max

