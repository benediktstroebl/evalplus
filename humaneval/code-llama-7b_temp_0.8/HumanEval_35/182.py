

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    # assert isinstance(l, list), "Input must be of type list"
    # assert len(l) > 0, "List is empty"
    if len(l) == 1:
        return l[0]
    else:
        if l[0] >= l[1]:
            max_val = l[0]
            l[0] = 0
            l[1] = max_val
            return max_element(l)
        else:
            max_val = l[1]
            l[0] = l[1]
            l[1] = 0
            return max_element(l)

