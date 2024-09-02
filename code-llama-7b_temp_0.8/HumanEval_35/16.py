

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    # if list is empty
    if len(l) == 0:
        return None
    # if list has only one element
    elif len(l) == 1:
        return l[0]
    else:
        # find maximum element in a list
        # if first element is bigger then the rest of the list
        if l[0] > max_element(l[1:]):
            return l[0]
        # if the rest of the list is bigger then the first element
        else:
            return max_element(l[1:])

