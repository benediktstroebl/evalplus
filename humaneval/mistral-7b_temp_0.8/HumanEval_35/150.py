

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    if l == []:
        raise ValueError('Input should not be empty.')
    if l == [None]:
        raise ValueError('Input should not be empty.')
    max = l[0]
    for i in l:
        if max < i:
            max = i
    return max

