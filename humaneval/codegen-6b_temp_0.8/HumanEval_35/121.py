

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    max_number = l[0]
    for i in range(1, len(l)):
        if l[i] > max_number:
            max_number = l[i]
    return max_number

