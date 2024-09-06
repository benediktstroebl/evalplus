

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    # find max element with simple way
    max_element = l[0]
    for i in l:
        if max_element < i:
            max_element = i

    return max_element

