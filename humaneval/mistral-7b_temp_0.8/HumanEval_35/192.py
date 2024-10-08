

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    maximum = 0
    for i in range(len(l)):
        if l[i] > maximum:
            maximum = l[i]
    return maximum
