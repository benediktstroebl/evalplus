

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """

    if not isinstance(l, list):
        return "Can't operate on strings!"
    if len(l) == 1:
        return l[0]
    if len(l) == 0:
        return 'Empty list!'
    max = l[0]
    for i in l:
        if i > max:
            max = i
    return max

