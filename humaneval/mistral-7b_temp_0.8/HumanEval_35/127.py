

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    """Return max element in the list

    Args:
        l (list): list with integers

    Returns:
        int: max element in the list
    """
    if len(l) == 0:
        return l

    max_number = l[0]

    for number in l[1:]:
        if number > max_number:
            max_number = number

    return max_number

